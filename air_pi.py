# AIR PI : Measure  indoor Air Quality and  log it on grafana

from sgp30 import SGP30
import time as tm
from datetime import datetime
import sys
import mysql.connector
import adafruit_bme680
import time
import board
from pms7003 import Pms7003Sensor, PmsSensorException


# creation de la BDD
sql_create = """
 CREATE TABLE IF NOT EXISTS datair15 (
    id INT AUTO_INCREMENT PRIMARY KEY,
    time TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    temperature FLOAT(5,2) DEFAULT NULL,
    humidity FLOAT(5,2) DEFAULT NULL,
    pressure FLOAT(6,2) DEFAULT NULL,
    gas INT DEFAULT NULL,
    Eq_CO2 INT DEFAULT NULL,
    T_VOC INT DEFAULT NULL,
    pm1_0 INT DEFAULT NULL,
    pm2_5 INT DEFAULT NULL,
    pm10 INT DEFAULT NULL,
    n0_3 INT DEFAULT NULL,
    n0_5 INT DEFAULT NULL,
    n1_0 INT DEFAULT NULL,
    n2_5 INT DEFAULT NULL,
    n5_0 INT DEFAULT NULL,
    n10 INT DEFAULT NULL); """


# BME680 : Create sensor object, communicating over the board's default I2C bus
i2c = board.I2C()   # uses board.SCL and board.SDA
bme680 = adafruit_bme680.Adafruit_BME680_I2C(i2c)
bme680.sea_level_pressure = 1013.25  # change this to match the location's pressure (hPa) at sea level
gas = bme680.gas

# create pms sensor object
sensor = Pms7003Sensor('/dev/serial0')

# create sgp30 sensor and initialize
sgp30 = SGP30()

print("Sensor warming up, please wait...")
def crude_progress_bar():
    sys.stdout.write('.')
    sys.stdout.flush()

sgp30.start_measurement(crude_progress_bar)
sys.stdout.write('\n')




while True:

 try:
  # connection to bdd
  conn = mysql.connector.connect(host="localhost", user="capair", password="boulbi", database="air_data")
  cursor = conn.cursor()
  cursor.execute(sql_create)

  # read time (in UTC)
  now=datetime.utcnow()
  time = now.strftime('%Y-%m-%d %H:%M:%S')

  # read bme680 sensor
  temp = bme680.temperature
  hum = bme680.humidity
  press = bme680.pressure
  gas = bme680.gas

  # read SGP30 sensor
  out1, out2  = sgp30.command('measure_air_quality')
  eco2 = out1
  tvoc = out2

  # read pmsA003 sensor
  output = sensor.read()
  pm1_0 =  output["pm1_0"]
  pm2_5 =  output["pm2_5"]
  pm10 =  output["pm10"]
  n0_3 = output["n0_3"]
  n0_5 = output["n0_5"]
  n1_0 = output["n1_0"]
  n2_5 = output["n2_5"]
  n5_0 = output["n5_0"]
  n10 = output["n10"]

  # Create data frame and save to bdd
  data_frame=(time, temp, hum, press, gas, eco2, tvoc, pm1_0, pm2_5, pm10, n0_3, n0_5, n1_0, n2_5, n5_0, n10)
  cursor.execute("""INSERT INTO datair15(time, temperature, humidity, pressure, gas, Eq_CO2, T_VOC, pm1_0, pm2_5, pm10, n0_3, n0_5, n1_0, n2_5, n5_0, n10) VALUES(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)""", data_frame)
  conn.commit()

  # print dataframe and sleep
  print(data_frame)
  tm.sleep(30)

 except mysql.connector.errors.InterfaceError as e:
  print("Error %d: %s" % (e.args[0],e.args[1]))
  sys.exit(1)


 finally:
  # On ferme la connexion
  if conn:
    conn.close()
  sensor.close()
