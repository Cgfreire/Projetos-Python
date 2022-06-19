import time
from playsound import playsound

def contador(tempo):
    while(tempo):
        minutos,segundos = divmod(tempo, 60)
        timer = '{:02d}:{:02d}'.format(minutos,segundos)
        print(timer)
        time.sleep(1)
        tempo = tempo - 1

    print('Contador Terminado')
    playsound()

tempo = input("quanto tempo deseja descansar: ")

contador(int(tempo))