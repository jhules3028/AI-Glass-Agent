# Variables globales asociadas a los lentes.

# Las variables se manejan en las categorias:


# 1. Estado
#   1.1 NOMBRE_LENTES : Posibles nombres de las gafas

# 2. Foto

#   2.1 RUTA_GUARDADO_IMAGENES  :  ruta donde se guardaran las fotos tomadas por los lentes
#   2.2 AUTOFOCUS_SECONDS  :  Segundos de enfoque del lente
#   2.3 QUALITY_PHOTO : Calidad de la foto
#   2.4 NUMBER_FOTOS : Numero de fotos que se van a tomar cuando tomemos la foto.
#   2.5 TIME_BETWEEN_PHOTOS : Numero de segundos entre cada foto
#   2.6 RETRY_TAKE_PHOTO: Si no se pudo tomar la foto lo volvemos a intentar?
#   2.7 NUMBER_RETRYS: Numero de re-intentos para tomar la foto.

# 3. Texto

from frame_sdk.camera import  Quality
# Estado

NOMBRE_LENTES = "frame-glasses" # Poner una lista/diccionarios de diferentes nombres

# Foto

RUTA_GUARDADO_IMAGENES='app/storage/frame-photos'
AUTOFOCUS_SECONDS=3
QUALITY_PHOTO=Quality.HIGH
NUMBER_FOTOS=5
TIME_BETWEEN_PHOTOS=5
RETRY_TAKE_PHOTO=True
NUMBER_RETRYS=1
# Texto

