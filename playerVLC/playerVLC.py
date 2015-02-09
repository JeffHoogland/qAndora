import vlc
import pandora
import webbrowser
import urllib
import re
import tempfile
import os
import time
CachePath = tempfile.gettempdir()

class volcanoPlayer(object):
    def __init__(self):
        self.pandora = pandora.Pandora()
        self.curStation = ""
        self.curSong = -1
        self.playing = False
        self.skip = {'live':False, 'remix':False, 'edit':False, 'ban':False}
        self.die = False
        self.settings = {"username":"", "password":""}
        self.skinName = "Default"
        self.song = None
        self.songinfo = []
        self.displaysongs = []
        self.songCount = 0
        self.songChangeCallBack = None
        self.curVolume = 100
        self.player = vlc.MediaPlayer()

    def play(self):
        self.eventManager = self.player.event_manager()
        self.eventManager.event_attach(vlc.EventType.MediaPlayerEndReached, self.songIsOver)
        self.player.play()
        
    def songIsOver(self, event):
        if event.type == vlc.EventType.MediaPlayerEndReached:
            self.nextSong()
        
    def getPosition(self):
        return self.player.get_time()
      
    def getLength(self):
        return self.player.get_length()

    def setAutoSkip( self, sType, sBool ):
        self.skip[sType] = sBool

    def setChangeCallBack(self, callback):
        self.songChangeCallBack = callback
    
    def auth(self, user, passwd):
        self.settings['username'] = user
        self.settings['password'] = passwd
        try:
            self.pandora.connect(self.settings['username'], self.settings['password'])
        except:
            pass
            
    def setVolume(self, newVol):
        self.player.audio_set_volume(newVol)
        self.curVolume = newVol

    def playSong(self):
        self.playing = True
        self.player.play()

    def pauseSong(self):
        self.playing = False
        self.player.pause()

    def skipSong(self):
        self.nextSong()

    def setStation(self, station):
        self.curStation = pandora.Station(self.pandora, station)

    def getStations(self):
        return self.pandora.get_stations()

    def getStation(self):
        return self.curStation

    def getCurSongInfo(self):
        return self.songinfo[self.curSong]

    def getSongInfo(self):
        return self.songinfo

    def getStationFromName(self, name):
        stations = self.getStations()
        for station in stations:
            if station['stationName'] == name:
                return station

    def getSongRating(self):
        return self.songinfo[self.curSong]['rating']

    def banSong(self):
        info = self.songinfo[self.curSong]
        info['object'].rate('ban')
        
    def tiredSong(self):
        info = self.songinfo[self.curSong]
        info['object'].set_tired()

    def loveSong(self):
        info = self.songinfo[self.curSong]
        info['object'].rate('love')
        
    def unloveSong(self):
        info = self.songinfo[self.curSong]
        info['object'].rate('None')        

    def toggleMute(self):
        self.player.audio_toggle_mute()
            
    def is_playing(self):
        return self.player.is_playing()
        
    def clearSongs(self):
        self.song = None
        self.songCount = 0
        self.curSong = -1
        self.songinfo = []
        self.displaysongs = []

    def addSongs( self ):
        playlist = self.curStation.get_playlist()
        for song in playlist:
            info = { "title"	:	song.title, \
        	 "artist"	:	song.artist, \
        	 "album"	:	song.album, \
        	 "thumbnail"	:	song.artRadio, \
             "url"      : str(song.audioUrl), \
             "rating"   : song.rating, \
             "object"   : song
        	}
            
            #Apply Filters
            if (re.search('\[.*mix.*\]', info['title'].lower()) or re.search('\(.*mix.*\)', info['title'].lower())) and self.skip['remix']:
                if self.skip['ban']:
                    info['object'].rate('ban')
            elif (re.search('\[.*live.*\]', info['title'].lower()) or re.search('\(.*live.*\)', info['title'].lower())) and self.skip['live']:
                if self.skip['ban']:
                    info['object'].rate('ban')
            elif (re.search('\[.*edit.*\]', info['title'].lower()) or re.search('\(.*edit.*\)', info['title'].lower())) and self.skip['edit']:
                if self.skip['ban']:
                    info['object'].rate('ban')
            else:
                #If it isn't filtered out, add it to play list.
                self.songinfo.append(info)
        if not self.song:
            self.startPlaying()
            
    def startPlaying(self):
        self.nextSong()
        
    def setAudioFormat( self, fmt ):
        self.pandora.set_audio_format("%sQuality"%fmt.lower())
        
    def nextSong(self, event=False):
        self.curSong += 1

        info = self.songinfo[self.curSong]
        if self.player.is_playing():
            self.player.stop()
        self.player = vlc.MediaPlayer()
        self.player.audio_set_volume(self.curVolume)
        self.displaysongs.append(info)
        self.song = info['title']
        self.player.set_media(vlc.Media(info['url']))
        self.playing = True
        self.play()
        self.songChangeCallBack()
        
        if self.curSong >= len(self.songinfo)-1:
            self.addSongs()
        self.songCount += 1
        if self.songCount >= 15:
            self.songCount = 0
            self.auth(self.settings['username'], self.settings['password'])
