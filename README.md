
# Coding de Newspaper Library
_______
## Introducción

Este código contiene búsquedas en 3 periódico específicos como los son 

* [Lemonde](https://www.lemonde.fr)

* [The Guardian (UK)](https://www.theguardian.com/uk)

* [New York Time](https://www.nytimes.com)

Esto con el fin de traer la cantidad de artículos según una búsqueda especifica y un año establecido

## API respectivos

antes de poder compilar cualquier de los códigos anteriores es necesario tener el **_API KEY_** según el periódico necesario.

Estos **_API KEY_** se pueden pedir por medio de los siguientes enlaces:

* [Lemonde]() _(No requiere un **API KEY)_ 

* [The Guardian (UK)](https://open-platform.theguardian.com)

* [New York Time](https://developer.nytimes.com)

#### API en código

en el código se creo una variable la cual se denomina **_apikey_** la cual podrás poner tu código según te lo envié el respectivo periódico

````
apikey = "YOUR-API-KEY"
````


## Contenido del Repositorio

Este repositorio contiene diferentes raíces o capetas las cuales contiene un **código para cada año (*Pendiente de optimizar*)** las carpetas en el repositorio son:

* **_back** Carpeta que contiene código anterior desarrollado

* **Códigos** Es la carpeta que contiene los códigos en python según periódico.

* **Outputs** Es la carpeta en donde se guardan los CSV y TXT de cada dato recolectado por el código de python.

## Contenido del código

Los códigos son peticiones GET por medio de HTTP o URL según el periódico

#### Variables de petición 

```
URL = "https://api.nytimes.com/svc/search/v2/articlesearch.json"
PARAMS = {'q':q, 'begin_date':begindate, 'end_date':enddate,'api-key':apikey }  
```

#### Petición GET

```
r = requests.get(url = URL, params = PARAMS)
```

después de eso se definen los parámetros de búsqueda que se encuentran

#### Country

El cual es un **_array_** que contiene cada uno de los países en el **new york time** _( limita la búsqueda a 10 países cada 3.2 segundos)_. 
```
country = ["Colombia","Canada","Cuba","China","Cameroon","Cambodia","Costa Rica","Croatia","Czech Republic","Argentina"]
```

### keywords

Son las palabras claves en la cuales se hará la búsqueda en este ejemplo vemos la búsqueda para **_ciencia y tecnología_**
```
keywords = ['"science","technology"']
```

## Ejecución de código

El código se puede ejecutar en cualquier compilador de python o editor de código sea 

* **Anaconda**
* **VS Code**
* **Brakets**
* **Entre otros**

en caso de no tener un  editor de código capaz de compilar python se puede realizar sobre una terminal con los siguientes comandos:

---

## MacOS

#### Selecciona la ubicación de los archivos

La ubicación cambia según cada equipo y los definimos con un **_cd_**.

````
# cd /Repos/paotesis/Outputs
````

#### Ejecutamos el código

usamos python3 debido a que las librerías son de la version de python

````
# python3 --version
Python 3.7.1
````

La ubicación es la cual tengas predeterminada para el repositorio.

````
# python3 /Ubicacion del codigo/ZZZ/YYYY\ XXXX.py 
````

las características de los pasos anteriores son:

* **ZZZ** referencia del periodico.
* **YYY** Periodico al cual consultar.
* **XXXX** Año del cual buscar _(Solo están definidos los años del 2006 al 2016)_.

## License

This project is licensed under the [Unlicensed Free Software](http://unlicense.org) - see the [LICENSE](LICENSE) file for details

## Contribución a

* **Paola Angulo Ealo** - *Economista*

Este código se desarrollo para el trabajo de de tesis **Nombre xxxxx**  con el fin de **_Causa de los datos_**

## Autor

* **Rafael Angulo Ealo** - *Desarrollador e Ingeniero Electrónico* - [Pagina Web](https://www.rafgui.com)
