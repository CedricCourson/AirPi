from sgp30 import SGP30
import time
import sys

sgp30 = SGP30()

print("Sensor warming up, please wait...")
def crude_progress_bar():
    sys.stdout.write('.')
    sys.stdout.flush()

sgp30.start_measurement(crude_progress_bar)
sys.stdout.write('\n')

while True:
    out1, out2  = sgp30.command('measure_air_quality')
    print("ECO2 : ", out1)
    print("TVOC : ", out2)
    time.sleep(1.0)
