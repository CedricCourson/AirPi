from pms7003 import Pms7003Sensor, PmsSensorException
import time as tm

if __name__ == '__main__':

    sensor = Pms7003Sensor('/dev/serial0')

    while True:
        try:
            output = sensor.read()
            print(output)
            print("data1 : ",output["pm1_0"])  # exemple pour afficher une valeur de la chaine de mesure
        except PmsSensorException:
            print('Connection problem')
        tm.sleep(5)

    sensor.close()
