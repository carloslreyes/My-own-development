#! python3
# Cronómetro

import time

# Instrucciones del Programa

print('''Presione ENTER para iniciar. Después,
presione ENTER para iniciar otra vuelta.
Presione Ctrl-C para salir.''')

input() # ENTER para iniciar
print('Iniciado')
inicio = time.time()
ultimo = inicio
numVuelta = 1

# Registro tiempo de vueltas

try:
    while True:
        input()
        tiempoVuelta = round(time.time()- ultimo, 2)
        tiempoTotal = round(time.time() - inicio, 2)
        print('Vuelta #%s: %s (%s)' % (numVuelta, tiempoTotal, tiempoVuelta), end='')
        numVuelta += 1
        ultimo = time.time() # reinicia el tiempo de la última vuelta
except KeyboardInterrupt:
    print('\n Listo')

