#		python code
#		script_name:
#		author:
#		description:
#

from earsketch import *

init() #초기화
setTempo(120) #BPM 설정

#fitMedia(soundSample, trackNumber, startLocation, endLocation) : 사운드 샘플 재생
#fitMedia(Y01_DRUMS_1, 1, 1, 5) : Y01_DRUMS_1을 1번 트랙에서 1~4번까지 재생해라
#왼쪽에 위치한 4번째 폴더 : API Browser을 누르면 확인할 수 있음.

fitMedia(Y01_DRUMS_1, 1, 1, 5)
fitMedia(Y11_BASS_1, 2, 1, 5)
fitMedia(Y11_GUITAR_1, 3, 1, 5)

finish()
