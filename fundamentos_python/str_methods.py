name = 'Miguel Pantigoso'
coures = 'Curso de Python'

name_upper = name.upper()
print(name == name_upper)
print(name_upper)
print(name)
print(coures.lower())


words = 'curso de python'

print(words.capitalize())
print(words.title())


words = '  hola andres   '
print(words.strip())  #para limpiar texto espacios etc
print(words.lstrip())
print(words.rstrip())

text= 'Hlola Java'
text_replace = text.replace('Java','Cobol')

print(text)
print(text_replace)


text='Miguel,Pantigoso,Puraca,Java,Uxer'
data_list= text.split(',')
print(data_list[2])

data=['Miguel','Pantigos','aLIANZA LIMA','Figma']
text = ' / '.join(data)
print(text)


oracion = 'Hola chicos como estan, soy ux designer'
print(oracion.find('ux'))#cuando no encuentra lanza un -1
print(oracion.index('Hola')) #lanza una expepcion

print(oracion.startswith('kk')) #esto para ver si inicia con
print(text.endswith('designer'))



#con esto verificamos si una cadena contiene un numero

number='1234'
decimal = '1234.54'
text = 'Python'
mix ='Python3'

print(number.isnumeric()) #es numerica?
print(decimal.isdecimal()) #es decimal??
print(text.isalnum())
print(text.isalpha()) #es alafabetico?
print(mix.isalpha()) #es alafabetico


parrafo = '  hola miguel como estas !! espero que bien    '
parrafo_limpio = parrafo.strip().capitalize().title()
print(parrafo)

nuevo_parrafo = parrafo_limpio.replace('Espero que bien', 'Bienvenido al Curso de Python 3')
print(nuevo_parrafo)

words = nuevo_parrafo.split()  #con esto separamos
print(words)


#isDecimal() -> Util cuando slo quieres numeros enteros puros (0-9), sin signos ni formatos extra;os
#isdigit()-> mas flexible permite numeros con superindices y subindices
#isnumeric()-> el mas amplio, reconoce fracciones y otros caraceteres numeros Unicode


number2 = '12312312.98'
print(number2.isdecimal())

number3 = '9.4'
print(number3.isdecimal())

