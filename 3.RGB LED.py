from pyfirmata import Arduino,util
import time

#핀 모드 세팅
board = Arduino('COM8')

LED_R = board.get_pin('d:10:o') #10번 핀 red 출력
LED_G = board.get_pin('d:11:o') #11번 핀 green 출력
LED_B = board.get_pin('d:12:o') #12번 핀 blue 출력


print("RED")
LED_R.write(1)
time.sleep(1)
LED_R.write(0)
time.sleep(0.1)
    
print("GREEN")
LED_G.write(1)
time.sleep(1)
LED_G.write(0)
time.sleep(0.1)
    
print("BLUE")
LED_B.write(1)
time.sleep(1)
LED_B.write(0)
time.sleep(0.1)

