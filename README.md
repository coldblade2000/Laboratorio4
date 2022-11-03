# Nota importante sobre despliegue (BONO)
Como se realizo el bono de el laboratorio 4 que consistia en desplegar el proyecto en un servidor no hay nesecidad de desplegarlo localmente.

La URL del proyecto desplegado es la siguiente: 
https://bil4.planni.me/


# Instrucciones de Despliegue Local 
Para poder correr el proyecto este se debe descargar del repositorio de github

```
git clone https://github.com/coldblade2000/Laboratorio4.git
```

Una vez se tienen el repositorio en la maquna local si se desea se puede crear un ambiente virtual para aislar el proyecto y se tiene que proseguir a instalar las librerias especificadas en requirements.txt . En anaconda el comando seria el siguiente, pero en este caso se tiene que asegurar que en la ruta al .txt de requirements se esta referenciando a los archivos dentro del repositorio:

```
conda install pip
pip install -r requirements.txt
```
Una vez se tiene esto y se tiene el proyecto abierto lo unico que haria falta para poder ejecutar el proyecto seria correr el comando de FastAPI para correr el servidor manualmente en el puerto 8200.

```
pip install fastapi uvicorn[standard]
uvicorn main:app --host 0.0.0.0 --port 8200
```

