# Vamos a usar este codigo para poder ver los logs que nos generan los lentes, esto porque puede haber multipels estados

# La idea principal es capturar los eventos mas relevantes cuando se trata de los lentes.\
# Posibles estados:

# Lentes
#   1. Estado
#       1.1 Se pudo obtener el estado de los lentes (bateria, estan conectados (si,no))
#       1.2 No se pudo obtener su estado (no estan conectados)
#   2. Foto
#       2.1 Se pudo tomar una foto
#       2.2 Cuantas fotos se han tomado de cuantas (cuando vas a tomar fotos en secuencia)
#       2.3 No se pudo tomar la foto
#   3. Texto
#       3.1 Ya se ha terminado de mostrar un texto
#       3.2 Cuanto texto se ha mostrado en los lentes
#       3.3 No se ha podido mostrar un texto

import asyncio

#
