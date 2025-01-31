print('Ejemplo del uso de colecciones tipo SET')

# Definir ejemplos con colecciones

first_collection = {1,2,3,4,5}
second_collection = {3,4,5,6, 7, 8}

# Imprimir el contenido de una colección de tipo SET
print(f'Mi colección de tipo SET: {(first_collection)}')

# Remover un elemento de la coleccion REMOVE
first_collection.remove(4)

print(f'Mi coleccion actualizada: {first_collection}')

# Agregar un elemento a la coleccion
first_collection.add('Hola mundo')

print(f'Mi coleccion actualizada, ADD: {first_collection}')

#Interación sobre una colección de un ciclo FOR

print('\n\nImpresión del contenido de una colección\n')
for item in first_collection:
    print(item)

# Operaciones con colecciones
union_set = first_collection.union(second_collection)
intersection_set = first_collection.intersection(second_collection)
diference_set = first_collection.difference(second_collection)

print(f'Union de colecciones: {union_set}')
print(f'Intersection de colecciones: {intersection_set}')
print(f'Diferencia de colecciones: {diference_set}')

