"""
Conceitos básicos de Pyhton
"""
# Tipos de primitivo

# String
nome = "Batatinha"
# Number
age = 25
height = 1.75
# Boolean
isDriveLicense = True ## Python is Case sensitive so True/False !== true/false

# Conditionals
if isDriveLicense == True and age >= 18:
    print('Ok, você tem permissão para dirigir.')
else:
    print('Você ainda não tem a idade permitida')

# Teste dinamico para extrair dados de um usuário
your_name = input('Informe o seu nome: ')
your_age = input('Informe sua idade: ')

"""
Como toda entrada de dados é representada por uma string em Python também
não é diferente, por isso utilizamos o método int() para converter valores
de texto em strings.
"""
int_age = int(your_age)

if int_age >= 18:
    print('Ok ', your_name, 'você tem a idade permitida para dirigir!')
else:
    print('Desculpe ', your_name, 'você ainda não tem a idade permitida para dirigir!')

# Arrays e listas
list_products = ["Iphone", "Ipad", "Macbook"]
list_prices = [1500, 5000, 5500]

# Loops e laços de repetições
for product in list_products:
    print(product)

for iterator in range(10):
    print(list_prices)


