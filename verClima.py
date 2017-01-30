#! python3
# verTemperatura.py - Mira el clima para una ciudad deseada.

import json, requests, sys

print('Consultando la ciudad en VerTemperatura.py')

ciudad = input()
newCiudad = ciudad.title()
    
# Descargando el clima de OpenWeatherMap.org.


link ='http://api.openweathermap.org/data/2.5/forecast/city?q=%s&APPID=ed47fcbe308ed9edb86d29c8ad4d2ce9' %(newCiudad)
result = requests.get(link)
result.raise_for_status()


# JSON a Python

datosTemperatura = json.loads(result.text)


# Descipción de la Temperura

C = datosTemperatura['list']
print('Clima en %s: ' % (newCiudad))
print(C[0]['weather'][0]['main'], '|', C[0]['weather'][0]['description'])
print()
print('Temperatura para mañana: ')
print(C[1]['weather'][0]['main'], '|', C[1]['weather'][0]['description'])
print()
print('Temperatura para pasado mañana: ')
print(C[2]['weather'][0]['main'], '|', C[2]['weather'][0]['description'])
