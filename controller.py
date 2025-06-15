from pyfirmata import Arduino, util
import time

board=Arduino('COM1')

led_1=board.get_pin('d:8:o')
led_2=board.get_pin('d:9:o')
led_3=board.get_pin('d:10:o')
led_4=board.get_pin('d:11:o')

buzzer=board.get_pin('d:4:o')
light=board.get_pin('d:5:o')
light_sensor=board.get_pin('d:6:i')
gas_sensor=board.get_pin('d:7:i')


it = util.Iterator(board)
it.start()

def led(total,state):
    if total==1:
        led_1.write(state)
    elif total==2:
        led_2.write(state)
    elif total==3:
        led_3.write(state)
    elif total==4:
        led_4.write(state)

def sensor(state):
        # while state:
            sensor_light_value = light_sensor.read()
            sensor_gas_value = gas_sensor.read()
        
            if sensor_light_value==1:
                    light.write(1)
            else:
                    light.write(0)
        
            if sensor_gas_value==0:
                    buzzer.write(1)
            else:
                    buzzer.write(0)   
        
            # time.sleep(.2)


