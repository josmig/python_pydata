
text = 'Pantigoso puraca'
print(text[0:6:2])


#manipulacion de textos para extraer datos de x lugar del fragmento
text = 'Python es genial'
parts= text.split()
parts2 = parts[:2]
print(parts)
print(parts2)
parts_reverse = parts[::-1]
print(parts_reverse)
text_reverse = ' '.join(parts_reverse)
print(text_reverse)

text= 'Python'
print(text[:2].lower()+ text[:2].upper())

text = '    Hola Python'
print(text.strip()[:5])
print(text.strip()[5:])

