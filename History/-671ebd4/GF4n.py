## join con diccionarios... mas magia
test = {'hola': 1, 'bebe': 2}
s = '->'

# join las claves, porque son string?
print(s.join(test))


test = {1: 'bebe', 2: 'hola'}
s = ', '

# las claves no son sting, y vuelan al infinito y mas allá
print(s.join(test))