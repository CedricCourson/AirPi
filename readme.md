# AirPy 

> Indoor AirQuality monitoring. 
> Rapsberry py with air quality sensors monitor air parameters on grafana dashboard.

[Notion page of the project](https://cedriccoursonopensourceoceanography.notion.site/Air-Quality-c03885076f014ac9bdb52816a1032c2e)  configuration, info, tuto, test ...

## Materials :
* Bme680 sensors (temperature, humidity, pressure, gas)
* SGP30 (ECO2, TVOC)
* PMSA003 (particules sensors)
* Raspberry pi 4
Sensors are connected on GPIO. 
This raspberry pi is also using as web server with a installation of grafana. All data are monitoring on Grafana.


## Summary installation :
1. connect sensors 
2. i2cdetect -y 1 (for checking i2c connection)
3. instal libraries : sudo apt install adafruit-circuitpython-bme680, pimoroni-sgp30, pms7003
4. test each sensors with codes in sensors file
5. configure a bdd mysql, an update the file air_pi.py
6. launch airpi with : python3 air_pi-py 
