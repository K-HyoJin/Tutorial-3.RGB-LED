# Arduino Example 3
Tutorial 3. RGB LED \
LED가 RED -> GREEN -> BLUE 순서대로 켜지도록 제작

## circuit
RED -> digital 10pin\
GREEN -> digital 11pin \
BLUE -> digital 12pin \
![1 RGB](https://user-images.githubusercontent.com/79436159/108822632-b1353b00-7602-11eb-9367-730bd12b91a2.png)

## code
``` from pyfirmata import Arduino,util ```\
pyfirmata의 아두이노 모듈을 사용하기 위해 import함 

``` board = Arduino('COM8')``` \
변수1 = Arduino('**포트번호**') 를 해서 보드와 연결 

```LED_R = board.get_pin('d:10:o')``` \
  -> 10번핀을 RED LED의 digital신호 출력핀으로 설정\
  ```LED_G = board.get_pin('d:11:o')``` \
  -> 11번핀을 GREEN LED의 digital신호 출력핀으로 설정\
 ```LED_B = board.get_pin('d:12:o')``` \
  -> 12번핀을 BLUE LED의 digital신호 출력핀으로 설정\
변수1 = 변수2.get_pin('**d or a** : **pin number** : **i or o** ') \
**d or a** : The type of the pin \
**pin number** : The number of the pin\
**i or o** : The mode of the pin 
 

```LED_R.write(1)```\
RED LED가 연결된 10번 핀에 1을 입력시켜서 LED를 켜도록 함

```  time.sleep(1) ```\
1초동안 기다림
