# importing the requests library 
import requests
from selenium import webdriver
import numpy as np
import  os
import time

country= ["Colombia","Canada","Cuba","China","Camer%FAn","Camboya","Costa%20Rica","Croacia","Rep%FAblica+Checa","Argentina","Afganist%E1n","Australia","Argelia","Austria","Brasil","Bolivia","B%E9lgica","Banglad%E9s","Dinamarca","Rep%FAblica+Dominicana","Egipto","Etiop%EDa","Finlandia","Ghana","Alemania","Grecia","Guatemala","Hungr%EDa","Islandia","India","Indonesia","Ir%E1n","Irak","Irlanda","Israel","Italia","Jamaica","Jap%F3n","Kenia","Lituania","Luxemburgo","Malasia","Marruecos","Pa%EDses+Bajos","Nueva+Zelanda","Namibia","Noruega","Nicaragua","Pakist%E1n","Panam%E1","Portugal","Per%FA","Polonia","Filipinas","Rusia","Singapur","Sud%E1frica","Rep%FAblica+de+corea","Suecia","Suiza","Tailandia","Turqu%EDa","Emiratos+%C1rabes+Unidos","Reino+Unido","Estados+Unidos","Vietnam","M%E9xico","Ecuador","Venezuela","Espa%F1a","Francia","Estonia","Eslovaquia","Eslovenia","Uruguay","Paraguay","Chile","Sri+Lanka","Romania","Tanzania","T%FAnez","Bulgaria","Nigeria","Letonia","Arabia+Saudita","Bielorrusia","Serbia","Senegal","Escocia"]
keyword= "Ciencia"
syear = ["2015"]

datos = []
year = []  
links = []
tcountry = []

for y in syear:
        print("_________________________")
        print(y)
        for c in country:
                try:
                        browser = webdriver.Safari()
                        url = "http://ariadna.elmundo.es/buscador/archivo.html?q=%22+"+ c +"%22%20%22"+ keyword +"%22&t=1&n=10&fd=0&td=0&w=60&s=0&no_acd=1&parametric_year="+y
                        links.append(url)
                        browser.get(url)
                        nav = browser.find_element_by_class_name("numero_resultados")
                        value = nav.text.split()
                        print(value[0])
                        datos.append(value[0])
                        year.append(y)
                        tcountry.append(c)
                        time.sleep(1) #Seconds   
                        browser.quit()            
                except:
                        print("0")
                        datos.append("0")
                        year.append(y)
                        tcountry.append(c)
                        time.sleep(1) #Seconds
                        browser.quit()
 
csvList = [country, datos, year, links]
#csvList = [tcountry, datos, year]

#TXT      
l = np.asarray(csvList)
ruta = os.getcwd() + os.sep
np.savetxt( "output_EM_ES"+" "+y+".txt",   # Archivo de salida
           l.T,        # Trasponemos los datos
           fmt="%s",       # Usamos números enteros
           delimiter=",")

#CSV
l = np.asarray(csvList)
ruta = os.getcwd() + os.sep
np.savetxt( "output_EM_ES"+" "+y+".csv",   # Archivo de salida
           l.T,        # Trasponemos los datos
           fmt="%s",       # Usamos números enteros
           delimiter=",")

print("Los archivos se han exportado satisfactoriamente")