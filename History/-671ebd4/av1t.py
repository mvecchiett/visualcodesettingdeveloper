## join con diccionarios... mas magia
test = {'hola': 1, 'bebe': 2}
s = '->'

# joins the keys only
print(s.join(test))


test = {1: 'bebe', 2: 'hola'}
s = ', '

# this gives error since key isn't string
print(s.join(test))