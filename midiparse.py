# Run midiparse.py filename.mid and it will give you a simple analysis of the notes in the midi file
#
# Example:
# monikakhot$ python midiparse.py two_note_phrase.mid
#
# There are 2 notes in the file two_note_phrase.mid
# [0.0, 41.0, 127, 0.25]
# [0.5, 38.0, 127, 0.75]
# [Distance from beginning, Frequency, Velocity, Duration]

import music21, sys
from music21 import *

piece = converter.parse("midi/%s" % sys.argv[1])
fp = piece.write('midi', fp='music21path.mid')

all_parts = []
for part in piece.parts:
  part_tuples = []
  for event in part:
    print(event)
    for y in event.contextSites():
      if y[0] is part:
        offset = y[1]
    if getattr(event, 'isNote', None) and event.isNote:
      part_tuples.append([offset, event.pitch.ps, event.volume.velocity, event.quarterLength])
  all_parts.append(part_tuples)

results_hash = {}
results_hash["notes"] = len(part_tuples)
results_hash["file"] = sys.argv[1]
print("There are %(notes)d notes in the %(file)s file" % results_hash)
for part in part_tuples:
  print(part)
print("[Distance from beginning, Frequency, Velocity, Duration]")
