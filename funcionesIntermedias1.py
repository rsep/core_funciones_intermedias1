# DESAFIO 1
x = [ [5,2,3], [10,8,9] ]
x[1][0] = 15
print(x)

estudiantes = [
    {'first_name':  'Michael', 'last_name' : 'Jordan'},
    {'first_name' : 'John', 'last_name' : 'Rosales'}
]
estudiantes[0]['last_name'] = 'Bryant'
print(estudiantes)

directorio_deportes = {
    'basketball' : ['Kobe', 'Jordan', 'James', 'Curry'],
    'fútbol' : ['Messi', 'Ronaldo', 'Rooney']
}
directorio_deportes['fútbol'][0] = 'Andrés'
print(directorio_deportes)

z = [ {'x': 10, 'y': 20} ]
z[0]['y'] = 30
print(z)


# DESAFIO 2
estudiantes = [
        {'first_name':  'Michael', 'last_name' : 'Jordan'},
        {'first_name' : 'John', 'last_name' : 'Rosales'},
        {'first_name' : 'Mark', 'last_name' : 'Guillen'},
        {'first_name' : 'KB', 'last_name' : 'Tonel'}
    ]

def iterateDictionary(some_list):
    for i in range(len(some_list)):
        print(f"first_name - {some_list[i]['first_name']}, last_name - {some_list[i]['last_name']}")

print("\nDESAFIO 2\n")
iterateDictionary(estudiantes)


# DESAFIO 3
def iterateDictionary2(key_name, some_list):
    for i in range(len(some_list)):
        print(estudiantes[i][key_name])

print("\nDESAFIO 3\n")
iterateDictionary2('first_name', estudiantes)
print("****")
iterateDictionary2('last_name', estudiantes)


# DESAFIO 4
dojo = {
    'ubicaciones': ['San Jose', 'Seattle', 'Dallas', 'Chicago', 'Tulsa', 'DC', 'Burbank'],
    'instructores': ['Michael', 'Amy', 'Eduardo', 'Josh', 'Graham', 'Patrick', 'Minh', 'Devon']
}

def printInfo(some_dict):
    for i in some_dict:
        print('-----------')
        cant_items = len(some_dict[i])
        print(cant_items, i.upper())
        for j in some_dict[i]:
            print(j)
