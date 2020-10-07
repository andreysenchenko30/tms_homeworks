dictionary_creation = lambda **some_name: [key * 2 for key in some_name.keys()]
print(dictionary_creation(a=1, bb=2, ccc=3))
