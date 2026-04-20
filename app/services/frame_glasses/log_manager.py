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


# Librerias necesarias para el funcionamiento del programa.
import time
from typing import Literal

class log_event:
    # En esta clase estara los diferentes tipos de logs asociados a los lentes.

    def __init__(self,
                    title: str,
                    description: str,
                    type: Literal["State", "Photo", "Text"],
                    important: bool, show_time: bool):
        """
        Aqui podremos agregar los diferentes eventos que necesitemos
        """
        self.title= title                     # Titulo en Negritas del mensaje
        self.type = type                      # tipo de log: Estado, Foto con los lentes, mostrar texto
        self.description = description        # contenido del log
        self.important = important            # Es importante lo que vamos a mostrar? Si/No
        self.show_time = show_time            # Decicion acerca de mostrar la hora del log.



    def Show_log(self):
        """
        Aqui vamos a presentar los lgos del sistema en la pagina.

        Nota: En esta version pre-liminar del desarrollo vamos a unicamente imprimir el contenido en la consola.
        """
        # En este apartado parecera codigo para que puedas mostrar el contenido de los logs.
        # Las plantiallas para mostrar los logs estan en:

        # app/static/css/frame/logs.css
        # app/static/html/frame/logs.html
        # app/static/js/frame/logs.js

        def Show_time():
            """
            Esta funcion consulta el dia, hora y minuto actuales.


            :return: str
            """

            fecha_actual=time.localtime()  # Descomponemos este valor en diferentes componentes.



            año_actual=str(fecha_actual.tm_year)
            mes_actual=str(fecha_actual.tm_mon)
            dia=str(fecha_actual.tm_mday)

            hora=str(fecha_actual.tm_hour)
            min=str(fecha_actual.tm_min)
            seg=str(fecha_actual.tm_sec)

            texto_final_log=f'{año_actual}-{mes_actual}-{dia} a las {hora}:{min}:{seg}'



            return texto_final_log



        print('Captura de logs de los lentes')

        print(self.title)
        print(self.type)
        print(self.description)

        if self.show_time:
            hora_log=Show_time()
            print(hora_log)





#log_event.__init__(title="Captua de fotos con las gafas",description="Captura de imagenes fallida ❌",type="Photo",important=False)
#log_event.__init__(title="Mostrar texto con las gafas",description="Se ha mostrado el texto exitosamente ✅",type="Text",important=False)