# importing the requests library 
import requests 
import numpy as np
import  os

# Cadenas de Pais Y Palabras
country = ["Colombia","Canada","Cuba","China","Cameroon","Cambodia","Costa Rica","Croatia","Czech Republic","Argentina"]
country2 = ["Afghanistan","Australia","Algeria","Austria","Brazil","Bolivia","Belgium","Bangladesh","Denmark","Dominican Republic"]
country3 = ["Egypt","Ethiopia","Finland","Ghana","Germany","Greece","Guatemala","Hungary","Iceland","India"]
country4 = ["Indonesia","Iran","Iraq","Ireland","Israel","Italy","Jamaica","Japan","Kenya","Lithuania"]
country5 = ["Luxembourg","Malaysia","Morocco","Netherlands","New Zealand","Namibia","Norway","Nicaragua","Pakistan","Panama"]
country6 = ["Portugal","Peru","Poland","Philippines","Russia","Singapore","South Africa","South Korea","Sweden","Switzerland"]
country7 = ["Thailand","Turkey","United Arab Emirates","United Kingdom","United States","Vietnam","Mexico","Ecuador","Venezuela","Spain"]
country8 = ["France","Estonia","Slovakia","Slovenia","Uruguay","Paraguay","Chile","Sri Lanka","Romania","Tanzania"]
country9 = ["Tunisia","Bulgaria","Nigeria","Latvia","Saudi Arabia","Belarus","Serbia","Senegal","Scotland"]

keywords = ['section_name:("Arts")']
#keywords = ['section_name:("Science") AND ("Technology")']
apikeyPrimary = "zfGlCSdzjVTQielCCrGlNNXbUnkoWO6W"

countryTotal = []
year = []
datos = []

StartT = 20130101
EndT = 20131231

csvList = []
urlList = []
timer = 160000000


# api-endpoint 
URL = "https://api.nytimes.com/svc/search/v2/articlesearch.json"

######################## COUNTRY  ################################################

for c in country:
    for k in keywords:   
        apikey = apikeyPrimary
        begindate = StartT
        enddate = EndT
        q = "\"" + c + "\""
        fq = k
        
        # defining a params dict for the parameters to be sent to the API 
        PARAMS = {'q':q, 'fq':fq, 'begin_date':begindate, 'end_date':enddate,'api-key':apikey }

        # sending get request and saving the response as response object 
        r = requests.get(url = URL, params = PARAMS) 
        
        # extracting data in json format 
        data = r.json() 
        
        # printing the output 
        #datos.append(data["response"]["meta"]["hits"])
        print (c)
        #print (data["response"]["meta"]["hits"]) 
        datos.append(data["response"]["meta"]["hits"])
        year.append(begindate)
        countryTotal.append(c)
        print(data["response"]["meta"]["hits"])
        print (data["status"]) 

######################## TIMER ################################################
t = 0
while t < timer:
        t = t + 1
print("El Timer ha finalizado")

######################## COUNTRY 2 ################################################

for c in country2:
    for k in keywords:   
        apikey = apikeyPrimary
        begindate = StartT
        enddate = EndT
        q = "\"" + c + "\""
        fq = k
        
        # defining a params dict for the parameters to be sent to the API 
        PARAMS = {'q':q, 'fq':fq, 'begin_date':begindate, 'end_date':enddate,'api-key':apikey }

        # sending get request and saving the response as response object 
        r = requests.get(url = URL, params = PARAMS) 
        
        # extracting data in json format 
        data = r.json() 
        
        # printing the output 
        #datos.append(data["response"]["meta"]["hits"])
        print (c)
        #print (data["response"]["meta"]["hits"]) 
        datos.append(data["response"]["meta"]["hits"])
        year.append(begindate)
        countryTotal.append(c)
        print(data["response"]["meta"]["hits"])
        print (data["status"]) 

######################## TIMER ################################################
t = 0
while t < timer:
        t = t +1
print("El Timer ha finalizado")

######################## COUNTRY 3 ################################################

for c in country3:
    for k in keywords:   
        apikey = apikeyPrimary
        begindate = StartT
        enddate = EndT
        q = "\"" + c + "\""
        fq = k
        
        # defining a params dict for the parameters to be sent to the API 
        PARAMS = {'q':q, 'fq':fq, 'begin_date':begindate, 'end_date':enddate,'api-key':apikey }

        # sending get request and saving the response as response object 
        r = requests.get(url = URL, params = PARAMS) 
        
        # extracting data in json format 
        data = r.json() 
        
        # printing the output 
        #datos.append(data["response"]["meta"]["hits"])
        print (c)
        #print (data["response"]["meta"]["hits"]) 
        datos.append(data["response"]["meta"]["hits"])
        year.append(begindate)
        countryTotal.append(c)
        print(data["response"]["meta"]["hits"])
        print (data["status"]) 

######################## TIMER ################################################
t = 0
while t < timer:
        t = t +1
print("El Timer ha finalizado")

######################## COUNTRY 4 ################################################

for c in country4:
    for k in keywords:   
        apikey = apikeyPrimary
        begindate = StartT
        enddate = EndT
        q = "\"" + c + "\""
        fq = k
        
        # defining a params dict for the parameters to be sent to the API 
        PARAMS = {'q':q, 'fq':fq, 'begin_date':begindate, 'end_date':enddate,'api-key':apikey }

        # sending get request and saving the response as response object 
        r = requests.get(url = URL, params = PARAMS) 
        
        # extracting data in json format 
        data = r.json() 
        
        # printing the output 
        #datos.append(data["response"]["meta"]["hits"])
        print (c)
        #print (data["response"]["meta"]["hits"]) 
        datos.append(data["response"]["meta"]["hits"])
        year.append(begindate)
        countryTotal.append(c)
        print(data["response"]["meta"]["hits"])
        print (data["status"]) 

######################## TIMER ################################################
t = 0
while t < timer:
        t = t +1
print("El Timer ha finalizado")
       

######################## COUNTRY 5 ################################################

for c in country5:
    for k in keywords:   
        apikey = apikeyPrimary
        begindate = StartT
        enddate = EndT
        q = "\"" + c + "\""
        fq = k
        
        # defining a params dict for the parameters to be sent to the API 
        PARAMS = {'q':q, 'fq':fq, 'begin_date':begindate, 'end_date':enddate,'api-key':apikey }

        # sending get request and saving the response as response object 
        r = requests.get(url = URL, params = PARAMS) 
        
        # extracting data in json format 
        data = r.json() 
        
        # printing the output 
        #datos.append(data["response"]["meta"]["hits"])
        print (c)
        #print (data["response"]["meta"]["hits"]) 
        datos.append(data["response"]["meta"]["hits"])
        year.append(begindate)
        countryTotal.append(c)
        print(data["response"]["meta"]["hits"])
        print (data["status"]) 
        

######################## TIMER ################################################
t = 0
while t < timer:
        t = t +1
print("El Timer ha finalizado")
       

######################## COUNTRY 6 ################################################

for c in country6:
    for k in keywords:   
        apikey = apikeyPrimary
        begindate = StartT
        enddate = EndT
        q = "\"" + c + "\""
        fq = k
        
        # defining a params dict for the parameters to be sent to the API 
        PARAMS = {'q':q, 'fq':fq, 'begin_date':begindate, 'end_date':enddate,'api-key':apikey }

        # sending get request and saving the response as response object 
        r = requests.get(url = URL, params = PARAMS) 
        
        # extracting data in json format 
        data = r.json() 
        
        # printing the output 
        #datos.append(data["response"]["meta"]["hits"])
        print (c)
        #print (data["response"]["meta"]["hits"]) 
        datos.append(data["response"]["meta"]["hits"])
        year.append(begindate)
        countryTotal.append(c)
        print(data["response"]["meta"]["hits"])
        print (data["status"]) 

######################## TIMER ################################################
t = 0
while t < timer:
        t = t +1
print("El Timer ha finalizado")

######################## COUNTRY 7 ################################################

for c in country7:
    for k in keywords:   
        apikey = apikeyPrimary
        begindate = StartT
        enddate = EndT
        q = "\"" + c + "\""
        fq = k
        
        # defining a params dict for the parameters to be sent to the API 
        PARAMS = {'q':q, 'fq':fq, 'begin_date':begindate, 'end_date':enddate,'api-key':apikey }

        # sending get request and saving the response as response object 
        r = requests.get(url = URL, params = PARAMS) 
        
        # extracting data in json format 
        data = r.json() 
        
        # printing the output 
        #datos.append(data["response"]["meta"]["hits"])
        print (c)
        #print (data["response"]["meta"]["hits"]) 
        datos.append(data["response"]["meta"]["hits"])
        year.append(begindate)
        countryTotal.append(c)
        print(data["response"]["meta"]["hits"])
        print (data["status"]) 

######################## TIMER ################################################
t = 0
while t < timer:
        t = t +1
print("El Timer ha finalizado")     

######################## COUNTRY 8 ################################################

for c in country8:
    for k in keywords:   
        apikey = apikeyPrimary
        begindate = StartT
        enddate = EndT
        q = "\"" + c + "\""
        fq = k
        
        # defining a params dict for the parameters to be sent to the API 
        PARAMS = {'q':q, 'fq':fq, 'begin_date':begindate, 'end_date':enddate,'api-key':apikey }

        # sending get request and saving the response as response object 
        r = requests.get(url = URL, params = PARAMS) 
        
        # extracting data in json format 
        data = r.json() 
        
        # printing the output 
        #datos.append(data["response"]["meta"]["hits"])
        print (c)
        #print (data["response"]["meta"]["hits"]) 
        datos.append(data["response"]["meta"]["hits"])
        year.append(begindate)
        countryTotal.append(c)
        print(data["response"]["meta"]["hits"])
        print (data["status"]) 

######################## TIMER ################################################
t = 0
while t < timer:
        t = t +1
print("El Timer ha finalizado")

######################## COUNTRY 9 ################################################

for c in country9:
    for k in keywords:   
        apikey = apikeyPrimary
        begindate = StartT
        enddate = EndT
        q = "\"" + c + "\""
        fq = k
        
        # defining a params dict for the parameters to be sent to the API 
        PARAMS = {'q':q, 'fq':fq, 'begin_date':begindate, 'end_date':enddate,'api-key':apikey }

        # sending get request and saving the response as response object 
        r = requests.get(url = URL, params = PARAMS) 
        
        # extracting data in json format 
        data = r.json() 
        
        # printing the output 
        #datos.append(data["response"]["meta"]["hits"])
        print (c)
        #print (data["response"]["meta"]["hits"]) 
        datos.append(data["response"]["meta"]["hits"])
        year.append(begindate)
        countryTotal.append(c)
        print(data["response"]["meta"]["hits"])
        print (data["status"]) 

csvList = [countryTotal, datos, year]

#TXT      
l = np.asarray(csvList)
ruta = os.getcwd() + os.sep
np.savetxt( "output_"+str(StartT)+"_NYT_FQ.txt",   # Archivo de salida
           l.T,        # Trasponemos los datos
           fmt="%s",       # Usamos números enteros
           delimiter=",")

#CSV
l = np.asarray(csvList)
ruta = os.getcwd() + os.sep
np.savetxt( "output_"+str(StartT)+"_NYT_FQ.csv",   # Archivo de salida
           l.T,        # Trasponemos los datos
           fmt="%s",       # Usamos números enteros
           delimiter=",")

print("Los archivos se han exportado satisfactoriamente")