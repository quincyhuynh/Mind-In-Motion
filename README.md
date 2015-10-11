Music In Motion uses Leap Motion and the Spotify API to allow you to control your music through your hands.

Instructions:

Open Hand (Five Fingers Extended): Change selection of next song (either shuffle or sequential, default being sequential) 
Fist: Pause/Play
Finger Circle-Clockwise: Next song in playlist
Finger Circle-Counter Clockwise: Previous song in playlist
3 Fingers: Next playlist 
2 Fingers: Previous playlists

Standard Rules: 

-Changing mode to shuffle will create a new shuffled playlist, and the next song to be played will be the first of that shuffled playlist. Changing mode from Sequential to Shufle will a similar thing  (modeled after iTunes)
-Changing playlists will cycle through your playlists and if the last playlist is reached, it will cycle back to the first one the next time next playlist is called.
-When the last song  of the current playlist (or very first if calling previous song), the program will halt and wait for input after the song finished playing
