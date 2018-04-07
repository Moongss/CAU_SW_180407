#		python code
#		script_name:
#		author:
#		description:
#

from earsketch import *

init()
setTempo(120)

#music
drums1 = ELECTRO_DRUM_MAIN_BEAT_008
drums2 = ELECTRO_DRUM_MAIN_BEAT_007

'''
fitMedia(drums1, 1, 1, 1.5)
fitMedia(drums2, 1, 1.5, 2)
fitMedia(drums1, 1, 2, 2.5)
fitMedia(drums2, 1, 2.5, 3)
fitMedia(drums1, 1, 3, 3.5)
fitMedia(drums2, 1, 3.5, 4)
fitMedia(drums1, 1, 4, 4.5)
fitMedia(drums2, 1, 4.5, 5)
fitMedia(drums1, 1, 5, 5.5)
fitMedia(drums2, 1, 5.5, 6)
fitMedia(drums1, 1, 6, 6.5)
fitMedia(drums2, 1, 6.5, 7)
fitMedia(drums1, 1, 7, 7.5)
fitMedia(drums2, 1, 7.5, 8)
fitMedia(drums1, 1, 8, 8.5)
fitMedia(drums1, 1, 8.5, 9)
'''

for i in range(1, 9):
  fitMedia(drums1, 1, i, i+0.5)
  fitMedia(drums2, 1, i+0.5, i+1)
  fitMedia(DUBSTEP_FILTERCHORD_002, 2, i, i + 1)
fitMedia(DUBSTEP_FILTERCHORD_002, 3, 1, 9)
  
finish()
