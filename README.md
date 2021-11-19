# Simulación basada en eventos discretos #

<br/>

## Simulación de una población ##

<br/>

Dada una población inicial de H hombres y M mujeres y, un tiempo límite T=100, se simulará el desarrollo de esta población durante dicho período de tiempo, teniendo en cuenta condiciones para reproducción y mortalidad, dadas por las probabilidades del archivo utils.py y calculadas por las definiciones dadas en probabilities.py.<br/>

En caso de que desee cambiar valores de las probabilidades solo es necesario modificar el archivo utils.py.<br/>

Para ejecutar el algoritmo, debe ejecutar la siguiente linea<br/>
Linux:
```
python3 simulation.py
```
o
```
python3 simulation.py <cantidad hombres> <cantidad mujeres>
```
Windows
```
py simulation.py
```
o
```
py simulation.py <cantidad hombres> <cantidad mujeres>
```
<br/>
El algoritmo dará como salida la cantidad de personas, nacimientos, fallecimientos, emparejamientos y rupturas hasta cada año durante el período de tiempo T.