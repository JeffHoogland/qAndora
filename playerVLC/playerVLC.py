import vlc
import pandora
import webbrowser
import urllib
import re

Download = False
DownloadPath = "/media/sda5/Music/pandora/"

class volcanoPlayer(object):
    def __init__( self ):
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
        self.curVolume = 75
        self.player = vlc.MediaPlayer()
        
    def setAutoSkip( self, sType, sBool ):
        self.skip[sType] = sBool
        
    def setChangeCallBack( self, callback ):
        self.songChangeCallBack = callback
    
    def auth( self, user, passwd):
        self.settings['username'] = user
        self.settings['password'] = passwd
        try:
            self.pandora.connect(self.settings['username'], self.settings['password'])
        except:
            pass
            
    def setVolume( self, newVol ):
        self.player.audio_set_volume( newVol )
        self.curVolume = newVol

    def playSong( self ):
        self.playing = True
        self.player.play()

    def pauseSong( self ):
        self.playing = False
        self.player.pause()

    def skipSong( self ):
        self.nextSong()

    def setStation( self, station ):
        self.curStation = pandora.Station(self.pandora, station)

    def getStations( self ):
        return self.pandora.get_stations()

    def getStation( self ):
        return self.curStation

    def getCurSongInfo( self ):
        return self.songinfo[self.curSong]

    def getSongInfo( self ):
        return self.songinfo

    def getStationFromName( self, name):
        stations = self.getStations()
        for station in stations:
            if station['stationName'] == name:
                return station

    def getSongDuration( self ):
        print "Getting Song duration"
        seconds = self.player.get_length() / 1000.0
        print "Starting Seconds %s"%seconds
        mins = 0
        while seconds >= 60:
            seconds -= 60
            mins += 1
        print "Minutes %s Seconds %s"%(mins, seconds) 
        return mins, seconds

    def getSongRating( self ):
        return self.songinfo[self.curSong]['rating']

    def search( self, searchstring ):
        return self.pandora.search(searchstring)

    def createStation( self, station ):
        self.pandora.add_station_by_music_id(station)

    def deleteStation( self, station ):
        pandora.Station(self.pandora, station).delete()

    def renameStation( self, station, name ):
        pandora.Station(self.pandora, station).rename(name)

    def banSong( self ):
        info = self.songinfo[self.curSong]
        info['object'].rate('ban')

    def loveSong( self ):
        info = self.songinfo[self.curSong]
        info['object'].rate('love')

    def clearSongs( self ):
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
            self.songinfo.append(info)
        if not self.song:
            self.startPlaying()

    def startPlaying( self ):
        self.nextSong()

    def check_download( self, url, title ):
        if Download:
            urllib.urlretrieve(str(url), '%s%s.mp3'%(DownloadPath, title))
            
    def setAudioFormat( self, fmt ):
        self.pandora.set_audio_format("%sQuality"%fmt.lower())

    def nextSong( self, event=False ):
        self.curSong += 1

        if self.curSong >= len(self.songinfo)-1:
            self.addSongs()
        self.songCount += 1
        if self.songCount >= 15:
            self.songCount = 0
            self.auth(self.settings['username'], self.settings['password'])
            
        info = self.songinfo[self.curSong]
        #print info['title']
        if (re.search('\[.*mix.*\]', info['title'].lower()) or re.search('\(.*mix.*\)', info['title'].lower())) and self.skip['remix']:
            if self.skip['ban']:
                self.banSong()
            self.nextSong()
        elif (re.search('\[.*live.*\]', info['title'].lower()) or re.search('\(.*live.*\)', info['title'].lower())) and self.skip['live']:
            if self.skip['ban']:
                self.banSong()
            self.nextSong()
        elif (re.search('\[.*edit.*\]', info['title'].lower()) or re.search('\(.*edit.*\)', info['title'].lower())) and self.skip['edit']:
            if self.skip['ban']:
                self.banSong()
            self.nextSong()
        else:
            self.playNextSong()
            
    def playNextSong( self ):
        if self.player.is_playing():
            self.player.stop()
        self.player = vlc.MediaPlayer()
        self.player.audio_set_volume( self.curVolume )
        self.player.audio_set_delay( 2500 )
        self.event_manager = self.player.event_manager()
        self.event_manager.event_attach(vlc.EventType.MediaPlayerEndReached,      self.nextSong)
        info = self.songinfo[self.curSong]
        self.displaysongs.append(info)
        self.song = info['title']
        self.player.set_media(vlc.Media(info['url']))
        self.playing = True
        self.player.play()
        self.songChangeCallBack()

