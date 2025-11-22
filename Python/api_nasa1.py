'''
   API: Aplication Programing Interface
   Nasa API: https://api.nasa.gov/
   API_KEY_NASA: YOUR NASA API_KEY
   Developer: Alejandro Garcia
   Date: 09112025
   scrip desccription: Get and read data from NASA API about comets and others
   https://api.nasa.gov/neo/rest/v1/neo/3726710?api_key={api_key}
'''
import requests
import os

os.system('clear')

def get_nasa_data(api_key):
    print("::: COMET INFORMATION :::")
    url = f"https://api.nasa.gov/neo/rest/v1/neo/3726709?api_key={api_key}"

    #Realizar la solicitud a la API
    response = requests.get(url)
    response.raise_for_status() #=> Validar si se presenta algún error en la peticion
    data = response.json() #Convertir la respuesta a formato JASON (JS Object Notation)

    print(data)

API_KEY_NASA = 'jR9HCnVlOyJwksATgTU98KqV2oowtoQsBn8hx73H'
get_nasa_data(API_KEY_NASA)