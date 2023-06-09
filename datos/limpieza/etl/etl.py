#importar librerias
import pandas as pd
import requests

def descargar_datos_csv(url, archivo_salida):
    """
    Descarga un archivo CSV desde una URL y lo guarda en un archivo local.

    Parámetros:
        - url (str): La URL del archivo CSV a descargar.
        - archivo_salida (str): El nombre del archivo de salida para guardar los datos descargados.
    """
    # Realizar la solicitud GET al enlace y guardar la respuesta
    response = requests.get(url)

    # Verificar si la solicitud fue exitosa (código 200)
    if response.status_code == 200:
        # Guardar los datos en el archivo de salida
        with open(archivo_salida, "wb") as f:
            f.write(response.content)
            print("Descarga completada.")
    else:
        print("Error al descargar los datos. Código de estado:", response.status_code)

def cargar_datos_csv(archivo_csv):
    """
    Carga los datos de un archivo csv en un DataFrame.

    Parametros:
        archivo_csv (str): Nombre del archivo csv a cargar
    Retorna:
        objeto Dataframe que contiene los datos del archivo csv
    """
    # Cargar los datos del archivo csv en un DataFrame
    df = pd.read_csv(archivo_csv, sep=';', encoding='latin-1')
    return df

def guardar_datos_como_csv(df, ruta):
    """
    Guarda los datos de un DataFrame en un archivo CSV.

    Parámetros:
        - df: El DataFrame que contiene los datos a guardar.
        - nombre_archivo: El nombre del archivo CSV de salida.
    """
    df.to_csv(ruta, index=False)
    print(f'Datos guardados correctamente')


url = "http://datos.salud.gob.ar/dataset/ceaa8e87-297e-4348-84b8-5c643e172500/resource/30d76bcb-b8eb-4bf3-863e-c87d41724647/download/informacion-publica-dengue-zika-nacional-anio-2022.csv"
archivo_salida = "datos/limpieza/eda/dengue-zika-2022.csv"  # Nombre del archivo de salida en formato CSV

# Descargar los datos desde web
descargar_datos_csv(url, archivo_salida)

# cargar los datos en u DataFrame
#df = cargar_datos_csv(archivo_salida)

# guardar los datos en directorio local
# guardar_datos_como_csv(archivo_salida, "datos/limpieza/dengue-zika-2022.csv")

print("Los datos fueron descargados")
