import midi
#from music21 import *
from miditime.miditime import MIDITime

# Instantiate the class with a tempo (120bpm is the default) and an output file destination.

# Create a list of notes. Each note is a list: [time, pitch, velocity, duration]

#get beat start of each note in gesture
#get note value
#get velocity
#get duration

cameo = [0,0,1,1,1,2,2,2, 3,3,3,4,4,4,4,6, 6,6,7,7,8,8,8,8, 9,9,9,9, 
0,0,1,1,1,2,2,2, 3,3,3,4,4,4,4,5, 0,0,1,1,1,2,2,2, 3,3,3,4, 
4,4,4,0,0,1,1,1, 2,2,2,3,3,3,4,4, 4,4,6,6,6,7,7,8, 8,8,8,9, 
9,9,9,12,12,12,12,12, 12,12,12,7,7,8,8,8, 8,9,9,9,9,0,0,1, 1,1,2,2, 
2,3,3,3,4,4,4,4, 12,12,12,12,7,7,8,8, 8,8,9,9,9,9,0,0, 0,0,0,0, 
12,12,12,12,12,12,12,12, 13,13,13,13,13,13,13,13, 0,0,1,1,1,2,2,2, 3,3,3,4, 
4,4,4,6,6,6,7,7, 8,8,8,8,9,9,9,9, 12,12,12,12,13,13,13,13, 13,13,13,13, 
12,12,12,12,13,13,13,13, 0,0,1,1,1,2,2,2, 12,12,12,12,13,13,13,13, 13,13,13,13, 
12,12,12,12,13,13,13,13, 0,0,1,1,1,2,2,2, 12,12,12,12,13,13,13,13, 13,13,13,13, 
12,12,12,12,13,13,13,13, 0,0,1,1,1,2,2,2, 12,12,12,12,13,13,13,13, 13,13,13,13]

alex = [0,0,1,1,1,2,2,2, 3,3,3,4,4,4,4,6, 6,6,7,7,8,8,8,8, 9,9,9,9, 
0,0,1,1,1,2,2,2, 3,3,3,4,4,4,4,6, 6,6,7,7,8,8,8,8, 9,9,9,9, 
9,9,9,6,6,6,7,7, 8,8,8,8,9,9,9,9, 0,0,1,1,1,2,2,2, 3,3,3,4, 
4,4,4,10,10,10,10,11, 10,10,10,10,10,10,10,10, 0,0,1,1,1,2,2,2, 3,3,3,4, 
4,4,4,6,6,6,7,7, 8,8,8,8,9,9,9,9, 10,10,10,10,0,0,0,0, 0,0,0,0, 
0,0,1,1,1,2,2,2, 3,3,3,4,4,4,4,6, 6,6,7,7,8,8,8,8, 9,9,9,9, 
10,10,10,10,10,10,10,10, 12,12,12,12,12,12,12,12, 0,0,1,1,1,2,2,2, 10,10,10,10, 
10,10,10,10,12,12,12,12, 12,12,12,12,0,0,1,1, 1,2,2,2,10,10,10,10, 10,10,10,10, 
12,12,12,12,12,12,12,12, 0,0,1,1,1,2,2,2, 10,10,10,10,12,12,12,12, 13,13,13,13, 
10,10,10,10,12,12,12,12, 13,13,13,13,0,0,1,1, 1,2,2,2,10,10,10,10, 12,12,12,12]

sierra = [0,0,5,5,5,5,5,5, 5,5,1,1,1,2,2,2, 3,3,3,4,4,4,4,6, 6,6,6,7, 
7,8,8,8,8,9,9,9, 9,9,9,9,9,9,9,9, 0,0,1,1,1,2,2,2, 3,3,3,4, 
4,4,4,0,0,1,1,1, 2,2,2,3,3,3,4,4, 4,4,6,6,6,7,7,8, 8,8,8,9, 
9,9,9,13,13,13,13,13, 0,0,1,1,1,2,2,2, 3,3,3,4,4,4,4,6, 6,6,7,7, 
8,8,8,8,9,9,9,9, 13,13,13,13,13,13,13,13, 0,0,1,1,1,2,2,2, 3,3,3,4, 
4,4,4,6,6,6,7,7, 8,8,8,8,9,9,9,9, 13,13,13,13,13,13,13,13, 14,14,14,14, 
14,14,14,14,14,14,14,14, 0,0,1,1,1,2,2,2, 3,3,3,4,4,4,4,6, 6,6,7,7, 
8,8,8,8,9,9,9,9, 13,13,13,13,13,13,13,13, 14,14,14,14,14,14,14,14, 14,14,14,14, 
10,10,10,10,10,10,10,10, 0,0,1,1,1,2,2,2, 3,3,3,4,4,4,4,6, 6,6,7,7, 
8,8,8,8,9,9,9,9, 13,13,13,13,13,13,13,13, 14,14,14,14,14,14,14,14, 14,14,14,14]

erica = [0,0,1,1,1,2,2,2, 3,3,3,4,4,4,4,4, 0,0,1,1,1,2,2,2, 3,3,3,4, 
4,4,4,6,6,6,7,7, 8,8,8,8,9,9,9,9, 0,0,1,1,1,2,2,2, 3,3,3,4, 
4,4,4,6,6,6,7,7, 8,8,8,8,9,9,9,9, 0,0,1,1,1,2,2,2, 3,3,3,4, 
4,4,4,14,14,14,14,14, 0,0,5,5,5,5,5,5, 5,5,5,5,5,5,5,6, 6,6,7,7, 
8,8,8,8,9,9,9,9, 0,0,1,1,1,2,2,2, 3,3,3,14,14,14,14,14, 14,14,14,14, 
14,14,14,14,10,10,10,10, 10,10,10,10,0,0,1,1, 1,2,2,2,3,3,3,4, 4,4,4,6, 
6,6,7,7,8,8,8,8, 9,9,9,9,14,14,14,14, 14,14,14,14,14,14,14,14, 10,10,10,10, 
10,10,10,10,5,5,5,5, 5,5,5,5,14,14,14,14, 10,10,10,10,13,13,13,13, 13,13,13,13, 
12,12,12,12,12,12,12,12, 5,5,5,5,5,5,5,5, 14,14,14,14,10,10,10,10, 13,13,13,13, 
13,13,13,13,12,12,12,12, 12,12,12,12,5,5,5,5, 5,5,5,5,14,14,14,14, 10,10,10,10]


armslidelist = []
burstlist = []
elbowlist = []
falllist = []
handshakelist = []
headlist = []
leglist = []
paperslist = []
pauselist = []
rarmlist = []
resolvelist = []
sitholdlist = []
smokelist = []
twistlist = []
for i, gesture in enumerate(erica):
  armslide_midinotes = [
    [i+0.0, 45.0, 127, 0.25],
    [i+0.5, 43.0, 127, 0.25],
    [i+1.5, 41.0, 127, 0.25]] 
  burst_midinotes =[ 
    [i+0.25, 24.0, 127, 0.25],
    [i+2.25, 24.0, 127, 0.25],
    [i+2.75, 24.0, 127, 0.25]]
  elbow_midinotes = [
    [i+0.0, 41.0, 127, 0.25],
    [i+0.5, 41.0, 127, 0.25]]
  fall_midinotes = [ 
    [i+0.0, 28.0, 127, 0.25]
    ,
    [i+0.25, 28.0, 127, 0.25]
    ,
    [i+0.5, 28.0, 80, 0.25]
    ,
    [i+0.75, 28.0, 80, 0.25]
    ,
    [i+1.0, 28.0, 80, 0.25]
    ,
    [i+1.25, 28.0, 80, 0.25]]
  handshake_midinotes = [ 
    [i+0.0, 47.0, 127, 0.25]
    ,
    [i+0.5, 40.0, 127, 0.25]
    ,
    [i+1.5, 40.0, 127, 0.25]]
  head_midinotes = [
    [i+0.0, 47.0, 127, 0.5]
    ,
    [i+1.0, 36.0, 71, 0.25]
    ,
    [i+1.5, 36.0, 127, 0.25]]
  leg_midinotes = [
    [i+0.0, 47.0, 127, 1.0]
    ,
    [i+0.75, 41.0, 127, 0.0]]
  papers_midinotes = [ 
    [i+0.0, 45.0, 127, 0.25]
    ,
    [i+0.5, 47.0, 105, 0.25]
    ,
    [i+1.25, 45.0, 24, 0.25]]
  pause_midinotes = [ 
    [i+0.0, 29.0, 127, 0.25]
    ,
    [i+0.5, 29.0, 127, 0.25]
    ,
    [i+0.75, 29.0, 127, 0.25]
    ,
    [i+1.25, 29.0, 127, 0.25]]
  rarm_midinotes = [ 
    [i+0.0, 43.0, 127, 0.25]
    ,
    [i+1.0, 43.0, 127, 0.25]
    ,
    [i+1.5, 45.0, 127, 0.25]]
  resolve_midinotes = [ 
    [i+1.0, 47.0, 77, 0.25]]
  sithold_midinotes = [ 
    [i+0.0, 29.0, 127, 0.33]]
  smoke_midinotes = [
    [i+0.0, 45.0, 127, 0.25]
    ,
    [i+0.5, 45.0, 127, 0.25]]
  twist_midinotes = [
    [i+0.0, 40.0, 127, 0.25]
    ,
    [i+1.0, 45.0, 127, 0.25]
    ,
    [i+1.5, 40.0, 127, 0.25]]

  if gesture == 0: # elbow
    for midinote in elbow_midinotes:
      elbowlist.append(midinote)

  if gesture == 1: # elbow
    for midinote in head_midinotes:
      headlist.append(midinote)

  if gesture == 2: # elbow
    for midinote in twist_midinotes:
      twistlist.append(midinote)

  if gesture == 3: # elbow
    for midinote in rarm_midinotes:
      rarmlist.append(midinote)

  if gesture == 4: # elbow
    for midinote in sithold_midinotes:
      sitholdlist.append(midinote)

  if gesture == 5: # elbow
    for midinote in pause_midinotes:
      pauselist.append(midinote)

  if gesture == 6: # elbow
    for midinote in burst_midinotes:
      burstlist.append(midinote)

  if gesture == 7: # elbow
    for midinote in fall_midinotes:
      falllist.append(midinote)

  if gesture == 8: # elbow
    for midinote in armslide_midinotes:
      armslidelist.append(midinote)

  if gesture == 9: # elbow
    for midinote in resolve_midinotes:
      resolvelist.append(midinote)

  if gesture == 10: # elbow
    for midinote in papers_midinotes:
      paperslist.append(midinote)

  if gesture == 12: # elbow
    for midinote in handshake_midinotes:
      handshakelist.append(midinote)

  if gesture == 13: # elbow
    for midinote in leg_midinotes:
      leglist.append(midinote)

  if gesture == 14: # elbow
    for midinote in smoke_midinotes:
      smokelist.append(midinote)

    # Add a track with those notes # ONE TRACK IS A SINGLE INSTANCE OF A GESTURE
mymidi = MIDITime(110, 'erica.mid')
mymidi.add_track(armslidelist)
mymidi.add_track(burstlist)
mymidi.add_track(elbowlist)
mymidi.add_track(falllist)
mymidi.add_track(handshakelist)
mymidi.add_track(headlist)
mymidi.add_track(leglist)
mymidi.add_track(paperslist)
mymidi.add_track(pauselist)
mymidi.add_track(rarmlist)
mymidi.add_track(resolvelist)
mymidi.add_track(sitholdlist)
mymidi.add_track(smokelist)
mymidi.add_track(twistlist)

# Output the .mid file
mymidi.save_midi()







# 
# blank_pattern = midi.read_midifile("midi/blank.mid")
# gestures = ['elbow',
# 	    'head',
# 	    'twist',
# 	    'rarm',
# 	    'sithold',
# 	    'pause',
# 	    'burst',
# 	    'fall',
# 	    'armslide',
# 	    'resolve',
# 	    'papers',
# 	    'rebound',
# 	    'handshake',
# 	    'leg',
# 	    'smoke']
# 
# # its appending not rewriting at correct beat
# dancers = [cameo, alex, sierra, erica]
# for count, d in enumerate(dancers):
#   for i, g in enumerate(gestures):
#     pattern = midi.Pattern(resolution=9600)
#     track = midi.Track()
#     track2 = midi.Track()
#     pattern.append(track)
#     pattern.append(track2)
# 
#     g_pattern = midi.read_midifile("midi/%s.mid" % g)
# 
# #range(len(d)) and length of final midi file
#     for s in range(len(d)):
# # its really that at midi beat 1, write this stuff, midi beat 2, write the stuff, etc
#       print s
#       if d[s] == i:
# 	the_pattern = g_pattern
#       else:
# 	the_pattern = blank_pattern
# 
#       for x in the_pattern[0]:
# 	track.append(x)
#       for x in the_pattern[1]:
# 	track2.append(x)
# 
#     midi.write_midifile('%s-%s.mid' % (count, g), pattern)
