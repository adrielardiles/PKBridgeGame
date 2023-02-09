import time
import requests
import random

# RANDOM SELECTOR

def pokealeatorio():
    api_url = "https://pokeapi.co/api/v2/pokemon/"
    params2 = {"limit": "200"} #150 Ultimos pokemones
    headers = {}

    response = requests.get(api_url, params = params2)
    data = response.json()
    resolts = data["results"]


    random_number1 = str(random.randint(1,200))

    for pokemon in resolts:
        numero2 = ""

        url_pokemon= str(pokemon["url"])
        for letra in url_pokemon:
            if letra.isdigit():
                numero2 += letra
        numero3 = list(numero2)
        del numero3[0]
        numero4 = "".join(numero3)
        if numero4 == random_number1:
            return pokemon["name"]

#MENU:









    
#POKEMON 1:



#POKEMON 2:


#POKEMON 3: 

        

        
    



###################################
#FUNCIONES

#################################

general = {"title": "Your own adventure", "derecha": "avanza hacia la derecha ...", "izquierda": "avanza hacia la izquierda..."}
npcnames = ("Andres", "Roman", "Julian", "SanMiguel")
name_assigment = True

while name_assigment: 
    nombre = input("hola, soy " + npcnames[0] + " cual es tu nombre?")
    for letra in nombre:
        if letra in ["1","2","3","4","5","6","7","8","9","0"]:
            print("No pongas numero en tu nombre")
            break
        else:
            name_assigment = False

print(npcnames[0] + ": Es un gusto conocerte " + nombre)
time.sleep(1)

print(npcnames[0] + ": Como sabes estas en un rpg llamado: " + general["title"] + "\n En esta aventura deberas lograr cruzar un puente sin ser asesinado")
time.sleep(1)

print(nombre + ": QUEEEEEEEEEE " )
time.sleep(1)

print(npcnames[0] + ": Pero no te preocupes, te dare un pokemon para que te defiendas en tu primer enfretamiento")
time.sleep(1)
pokemon1 = pokealeatorio()
print(npcnames[0] +  ": Tu primer pokemon es: " + pokemon1)
#Meter pokemon1 en una nueva funcion como argumento


#Un menu para abrir una mochila y un menu para ver estadisticas

print(npcnames[0] + ": Puedes ver las estadistica de tu pokemon abriendo el menu [STATS] con TAB")

    








