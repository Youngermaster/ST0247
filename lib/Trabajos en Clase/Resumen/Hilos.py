import time
import random

def procesoA():
    for i in range(10):
        print("Proceso A con valor: ",i)
        time.sleep(random.randint(0,5))

def procesoB():
    for i in range(10):
        print("Proceso B con valor: --",i)
        time.sleep(random.randint(0,5))

#programa
import threading

proceso_1 = threading.Thread(target=procesoA)  # crea el proceso hilo para la función
proceso_2 = threading.Thread(target=procesoB)

proceso_1.start()  # inicia el proceso del hilo
proceso_2.start()

proceso_1.join() #espera a que el hilo de proceso 1 termine
proceso_2.join() #espera a que el hilo de proceso 2 termine
print('Termine!!!!')

