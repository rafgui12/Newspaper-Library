# importing the requests library 
import requests 
import numpy as np
import  os
from bs4 import BeautifulSoup

# Cadenas de Pais Y Palabras
country = ["Colombie","Canada","Cuba","Chine","Cameroun","Cambodge","Costa Rica","Croatie","République tchèque","Argentine","Afghanistan","Australie","Algérie","Autriche","Brésil","Bolivie","Belgique","Bangladesh","Danemark","République dominicaine","Egypte","Ethiopie","Finlande","Ghana","Allemagne","Grèce","Guatemala","Hongrie","Islande","Inde","Indonésie","Iran","Irak","Irlande","Israël","Italie","Jamaïque","Japon","Kenya","Lituanie","Luxembourg","Malaisie","Maroc","Pays-Bas","Nouvelle Zélande","Namibie","Norvège","Nicaragua","Pakistan","Panama","Portugal","Pérou","Pologne","Philippines","Russie","Singapour","Afrique du Sud","Corée du Sud","Suède","Suisse","Thaïlande","Turquie","Émirats arabes unis","Royaume-Uni","États-Unis","Vietnam","Mexique","Équateur","Venezuela","Espagne","France","Estonie","Slovaquie","Slovénie","Uruguay","Paraguay","Chili","Sri Lanka","Roumanie","Tanzanie","Tunisie","Bulgarie","Nigeria","Lettonie","Arabie Saoudite","Biélorussie","Serbie","Sénégal","Ecosse"]
keywords = ['science']
#keywords = ['art']
exclude_keywords = "sport"

start_day = "01"
start_month = "01" 
end_day = "31"
end_month = "12"

syears = ["2016"]

datos = []
year = []  
links = []
tcountry = []
urls = []

# api-endpoint 
for y in syears:
        print("_________________________")
        print(y)
        for c in country:
                print(c)
                for k in keywords:
                        URL = "https://www.lemonde.fr/recherche/?keywords="+c+"+"+k+"&operator=and&exclude_keywords="+exclude_keywords+"&qt=recherche_texte_titre&period=custom_date&start_day="+start_day+"&start_month="+start_month+"&start_year="+y+"&end_day="+end_day+"&end_month="+end_month+"&end_year="+y+"&sort=desc"                        # sending get request and saving the response as response object 
                        r = requests.get(URL) 
                        urls.append(r.url)
                        #print(r.url)

                         # extracting data in json format 
                        soup = BeautifulSoup(r.text, "html.parser")
                        tags = soup.findAll('strong')
                        nav = tags[3].text
                        print(nav)

                        #Appends
                        datos.append(nav)
                        tcountry.append(c)
                        year.append(y)

#csvList = [country, datos, year, links]
csvList = [tcountry, datos, year]

#TXT      
l = np.asarray(csvList)
ruta = os.getcwd() + os.sep
np.savetxt( "output_LM"+" "+y+".txt",   # Archivo de salida
           l.T,        # Trasponemos los datos
           fmt="%s",       # Usamos números enteros
           delimiter=",")

#CSV
l = np.asarray(csvList)
ruta = os.getcwd() + os.sep
np.savetxt( "output_LM"+" "+y+".csv",   # Archivo de salida
           l.T,        # Trasponemos los datos
           fmt="%s",       # Usamos números enteros
           delimiter=",")

print("Los archivos se han exportado satisfactoriamente")