
clowns = int(input("Introduce el numero de payasos: "))
dolls= int(input("Introduce el numero de muñecas: "))
    
def calculate_package(clowns, dolls):

#pq es kg
    weight_clown= 112/1000
    weight_doll= 75/1000

    return (weight_clown*clowns)+(weight_doll*dolls)
    

print(f"El precio del pedido sera de: {calculate_package(clowns, dolls):.2f}$")
