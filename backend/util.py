from .eventhandler import EventHandler
from pygame import quit
from sys import exit


def salir(event):
    if event.data.get('message', ''):
        print('Status:', event.data['message'])
    quit()
    exit()


EventHandler.register(salir, 'quit')
