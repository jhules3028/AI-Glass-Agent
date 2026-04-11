# Variables globales asociadas a los lentes.

# Las variables se manejan en las categorias:


# 1. Estado
#   1.1 NOMBRE_LENTES : Posibles nombres de las gafas

# 2. Foto

#   2.1 RUTA_GUARDADO_IMAGENES  :  ruta donde se guardaran las fotos tomadas por los lentes
#   2.2 AUTOFOCUS_SECONDS  :  Segundos de enfoque del lente
#   2.3 QUALITY_PHOTO : Calidad de la foto

# 3. Texto

from frame_sdk.camera import  Quality
# Estado

NOMBRE_LENTES = "frame-glasses" # Poner una lista/diccionarios de diferentes nombres

# Foto

RUTA_GUARDADO_IMAGENES='app/storage/frame-photos'
AUTOFOCUS_SECONDS=3
QUALITY_PHOTO=Quality.HIGH

# Texto

