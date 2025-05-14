import csv
from sqlalchemy.orm import sessionmaker
from crear_base import Saludo2
from configuracion import engine

# para crear la sesion
Session = sessionmaker(bind=engine)
session = Session()

# Aqui la ruta del archivo csv
# para guiarme
#ruta_csv = "/home/h-08/Documentos/clase06-1bim-augusto20052008/ejemplo1/data/saludos_mundo.csv"
ruta_csv = "./data/saludos_mundo.csv"
# Lee el archivo csv y agregar los datos con la misma estructura
with open(ruta_csv, newline='', encoding='utf-8') as archivo:
    lector = csv.DictReader(archivo, delimiter='|')
    for fila in lector:
        saludo = Saludo2(
            mensaje=fila['saludo'],
            tipo=fila['tipo'],
            origen=fila['origen']
        )
        session.add(saludo)


# se confirma las transacciones
session.commit()
print("Datos agregados exitosamente.")
