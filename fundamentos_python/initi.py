import sys


def sayHello(name):
    print('Este script se ejecuta , solo si es ejecutado de forma directa')
    print(f'hola {name} que tal')


if __name__ == '__main__' :
    print('Hi, world')
    sayHello('Miguel')

