import spotify
import random
session = spotify.Session()
audio = spotify.AlsaSink(session)
loop = spotify.EventLoop(session)
loop.start()
session.login('quinceftw', 'thisisnotmypasswordlol')
print "Logging in..."
while session.connection.state is not spotify.ConnectionState.LOGGED_IN:
	session.process_events()
print "Connected"
toplist = session.get_toplist(type=spotify.ToplistType.TRACKS, region='US')
toplist.load()
random_track = random.choice(toplist.tracks)
random_track.load()
print random_track.name
session.player.load(random_track)
session.player.play()


