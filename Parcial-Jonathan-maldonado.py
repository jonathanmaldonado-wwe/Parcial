# se realiza la peticion de datos del usuario 
precio = float(input("Ingrese precio del videojuego: "))
vip = input("¿Es miembro VIP? (Si/No): ")

# se realizan la validacion del precio
if precio >= 500:
    precio = precio * 0.9  

# se realiza la validacion del vip
if vip.lower() == "sí":
    precio = precio * 0.85  

# se retorna el valor final
print("El precio final es:", precio)
