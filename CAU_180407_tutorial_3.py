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

fitMedia(RD_UK_HOUSE_MAINBEAT_8, 1, 1, 5)
fitMedia(RD_POP_PADCHORD_2, 2, 1, 9)

fillA = "0---0-0-00--0000"
fillB = "0--0--0--0--0-0-"
fillC = "--000-00-00-0-00"
makeBeat(OS_SNARE03, 3, 4, fillC)

finish()
