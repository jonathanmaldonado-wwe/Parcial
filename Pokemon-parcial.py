import requests

# Endpoint de la PokéAPI
url = "https://pokeapi.co/api/v2/pokemon?limit=20"

# Petición GET
response = requests.get(url)

# Validación del estado de la respuesta
if response.status_code == 200:
    data = response.json()  # Convertir la respuesta a JSON
    pokemones = data["results"]  # Lista de pokemones

    # Iterar sobre la lista de pokemones
    for pokemon in pokemones:
        nombre = pokemon["name"]
        # Condicional: si empieza con 'b' o 'B'
        if nombre.lower().startswith("b"):
            print(f"[ESPECIAL] {nombre}")
        else:
            print(f"Nombre: {nombre}")
else:
    print("Error en la petición. Código de estado:", response.status_code)
