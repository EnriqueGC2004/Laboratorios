print('Ejemplo con tuplas \n\n')

#Definición de una tuplq
tupla_informacion = ('Ana Picapiedra' , 22, 95.5)
print(f'Información de la tupla: {tupla_informacion}')

# Destructuración o unpaking
full_name, age, salary = tupla_informacion

print(f'Nombre: {full_name}, Age: {age}, Salary: {salary}')

print('\n\nImpresión de la tupla con un ciclo FOR \n')
#Impresión de los elementos de la tupla

for item in tupla_informacion:
    print(item)