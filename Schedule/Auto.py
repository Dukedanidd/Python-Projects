import schedule
import time

def tarea():
    print('Ejecutando tarea')


schedule.every(4).seconds.do(tarea)

while True:
    schedule.run_pending()
    time.sleep(1)
