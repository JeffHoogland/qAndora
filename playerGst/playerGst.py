import gobject, pygst
pygst.require('0.10')
import gst

import pandora
import webbrowser
import urllib
import re
import tempfile
import os

CachePath = tempfile.gettempdir()

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
        self.player = gst.element_factory_make('playbin', 'player')
        
        try:
             # alsasink pulsesink osssink autoaudiosink
             device = gst.parse_launch('alsasink')
        except gobject.GError:
            print 'Error: could not launch audio sink'
        else:
            self.player.set_property('audio-sink', device)
            self.bus = self.player.get_bus()
            self.bus.add_signal_watch()
            self.bus.connect('message', self.on_message)
             
    def on_message(self, bus, message):
         t = message.type
         if t == gst.MESSAGE_EOS:
             self.player.set_state(gst.STATE_NULL)
             self.button.setText('Start')
         elif t == gst.MESSAGE_ERROR:
             self.player.set_state(gst.STATE_NULL)
             err, debug = message.parse_error()
             print 'Error: %s' % err, debug
             self.button.setText('Start')
    
    def getPosition( self ):
        try:
            return self.player.query_position(gst.FORMAT_TIME)[0]/1000000000
        except:
            return 0
            
    def getLength( self ):
        try:
            return self.player.query_duration(gst.FORMAT_TIME)[0]/1000000000
        except:
            return 0
        
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
        #self.player.audio_set_volume( newVol )
        self.curVolume = newVol

    def playSong( self ):
        self.playing = True
        self.player.set_state(gst.STATE_PLAYING)

    def pauseSong( self ):
        self.playing = False
        self.player.set_state(gst.STATE_PAUSED)

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
        
    def tiredSong( self ):
        info = self.songinfo[self.curSong]
        info['object'].set_tired()

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

    def startPlaying( self ):
        self.nextSong()
            
    def setAudioFormat( self, fmt ):
        self.pandora.set_audio_format("%sQuality"%fmt.lower())

    def nextSong( self, event=False ):
        self.player.set_state(gst.STATE_NULL)
        self.curSong += 1

        info = self.songinfo[self.curSong]
        self.displaysongs.append(info)
        self.song = info['title']
        self.player.set_property('uri', info['url'])
        self.playing = True
        self.player.set_state(gst.STATE_PLAYING)
        self.songChangeCallBack()
        
        if self.curSong >= len(self.songinfo)-1:
            self.addSongs()
        self.songCount += 1
        if self.songCount >= 15:
            self.songCount = 0
            self.auth(self.settings['username'], self.settings['password'])

