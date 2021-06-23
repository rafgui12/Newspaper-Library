# importing the requests library 
import requests 
import numpy as np
import datetime
import  os

# Cadenas de Pais Y Palabras
countryTT = ["Colombia","Canada","Cuba","China","Cameroon","Cambodia","Costa Rica","Croatia","Czech Republic","Argentina","Afghanistan","Australia","Algeria","Austria","Brazil","Bolivia","Belgium","Bangladesh","Denmark","Dominican Republic","Egypt","Ethiopia","Finland","Ghana","Germany","Greece","Guatemala","Hungary","Iceland","India","Indonesia","Iran","Iraq","Ireland","Israel","Italy","Jamaica","Japan","Kenya","Lithuania","Luxembourg","Malaysia","Morocco","Netherlands","New Zealand","Namibia","Norway","Nicaragua","Pakistan","Panama","Portugal","Peru","Poland","Philippines","Russia","Singapore","South Africa","South Korea","Sweden","Switzerland","Thailand","Turkey","United Arab Emirates","United Kingdom","United States","Vietnam","Mexico","Ecuador","Venezuela","Spain","France","Estonia","Slovakia","Slovenia","Uruguay","Paraguay","Chile","Sri Lanka","Romania","Tanzania","Tunisia","Bulgaria","Nigeria","Latvia","Saudi Arabia","Belarus","Serbia","Senegal","Scotland"]
#country = ["Colombia","Canada","Cuba","China","Cameroon","Cambodia","Costa Rica","Croatia","Czech Republic","Argentina"]
#country2 = ["Afghanistan","Australia","Algeria","Austria","Brazil","Bolivia","Belgium","Bangladesh","Denmark","Dominican Republic"]
#country3 = ["Egypt","Ethiopia","Finland","Ghana","Germany","Greece","Guatemala","Hungary","Iceland","India"]
#country4 = ["Indonesia","Iran","Iraq","Ireland","Israel","Italy","Jamaica","Japan","Kenya","Lithuania"]
#country5 = ["Luxembourg","Malaysia","Morocco","Netherlands","New Zealand","Namibia","Norway","Nicaragua","Pakistan","Panama"]
#country6 = ["Portugal","Peru","Poland","Philippines","Russia","Singapore","South Africa","South Korea","Sweden","Switzerland"]
#country7 = ["Thailand","Turkey","United Arab Emirates","United Kingdom","United States","Vietnam","Mexico","Ecuador","Venezuela","Spain"]
#country8 = ["France","Estonia","Slovakia","Slovenia","Uruguay","Paraguay","Chile","Sri Lanka","Romania","Tanzania"]
#country9 = ["Tunisia","Bulgaria","Nigeria","Latvia","Saudi Arabia","Belarus","Serbia","Senegal","Scotland"]

#keywords = ['"science" AND "technology"']
#keywords = ["art"]
keywords = ["science"]

countryTotal = []
year = []
datos = []

csvList = []
urlList = []
timer = 160000000



# api-endpoint 
URL = "https://content.guardianapis.com/search"

date_time_start = '2010-01-01 00:00:00.0'  
date_time_finish = '2010-12-31 00:00:00.0'
yearActual = "20100101"  

start = datetime.datetime.strptime(date_time_start, '%Y-%m-%d %H:%M:%S.%f')
finish = datetime.datetime.strptime(date_time_finish, '%Y-%m-%d %H:%M:%S.%f')

for c in countryTT:
    for k in keywords:
        apikey = "bab25b0d-4b8b-4c85-936c-57d691c78cb8"
        begindate = start.date()
        enddate = finish.date()
        q = '"' + c + '"' + " AND " + k + " AND NOT " + '"sport"'        
        
        # defining a params dict for the parameters to be sent to the API 
        PARAMS = {'api-key':apikey, 'from-date':begindate, 'to-date':enddate, 'q':q} 
        
        # sending get request and saving the response as response object 
        r = requests.get(url = URL, params = PARAMS) 
        
        # extracting data in json format 
        data = r.json() 
        
        # printing the output 
        #print(data)
        print(c)
        countryTotal.append(c)
        datos.append(data["response"]["total"])
        year.append(yearActual)
        print(data["response"]["total"])
        print(data["response"]["status"])

csvList = [countryTotal, datos, year]

#TXT      
l = np.asarray(csvList)
ruta = os.getcwd() + os.sep
np.savetxt( "output_"+str(yearActual)+"_TG_UK"+".txt",   # Archivo de salida
           l.T,        # Trasponemos los datos
           fmt="%s",       # Usamos números enteros
           delimiter=",")

#CSV
l = np.asarray(csvList)
ruta = os.getcwd() + os.sep
np.savetxt( "output_"+str(yearActual)+"_TG_UK"+".csv",   # Archivo de salida
           l.T,        # Trasponemos los datos
           fmt="%s",       # Usamos números enteros
           delimiter=",")

print("Los archivos se han exportado satisfactoriamente")

#print (data["response"]["docs"][0]["web_url"]) 