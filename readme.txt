AirPy 


Indoor AirQuality monitoring. 
Rapsberry py with air quality sensors monitor air parameters on grafana dashboard.

Materials : 
Bme680 sensors (temperature, humidity, pressure, gas)
SGP30 (ECO2, TVOC)
PMSA003 (particules sensors)
Raspberry pi 4
Sensors connecter on GPIO. 
This raspberry pi is also using as web server with a installation of grafana. 
All data are monitoring on Grafana.

Notion page (info, tuto, test): 
https://cedriccoursonopensourceoceanography.notion.site/Air-Quality-c03885076f014ac9bdb52816a1032c2e


Résumé :
1- connect sensors 
2- i2cdetect -y 1 (for checking i2c connection)
3- instal libraries : sudo apt install adafruit-circuitpython-bme680, pimoroni-sgp30, pms7003
4- test each sensors with codes in sensors file
5- configure a bdd mysql, an update the file air_pi.py
5- launch airpi with : python3 air_pi-py 
