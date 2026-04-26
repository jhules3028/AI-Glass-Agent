# Repositorio que sirvio de apoyo para el desarrollo de esta seccion: https://github.com/CitizenOneX/frame_examples_python/blob/main/frame_msg/manual_exposure.py
# En este apartado podras ver la parte del servicio asociado a como toamr fotos con los lentes, asi como la ruta en la cual se guardan las fotos

# Funciones de esta pagina:

# 1. save_photo:            Esta funcion lo unico que hace es tratar de tomar una foto con las configuraciones del archivo: config.py; Captura logs de todo el procedimiento
# 2. take_multiple_photos:  Toma multiples fotos usando la función save_photo.



# Librerias necesarias para el funcionamiento del programa.
import asyncio

import io
from fileinput import filename
from pathlib import Path
from PIL import Image
import time
from frame_sdk import Frame
from frame_sdk.camera import Quality

# Configuraciones y funciones requeridas para el programa.

from app.services.frame_glasses.config import RUTA_GUARDADO_IMAGENES,AUTOFOCUS_SECONDS,QUALITY_PHOTO,NUMBER_FOTOS,TIME_BETWEEN_PHOTOS, RETRY_TAKE_PHOTOS #,NUMBER_RETRYS
from app.services.frame_glasses.log_manager import log_event

async def Save_photo(
        ruta_guardado_imagenes :str = RUTA_GUARDADO_IMAGENES,
        calidad_imagen = QUALITY_PHOTO,
        segundos_autofoco: int  = AUTOFOCUS_SECONDS
):
    """
    Toma una foto con las gafas

    :return:  Boolean y el path
    """
    async with Frame() as frame:
        try:
            frame.camera.take_photo(ruta_guardado_imagenes, quality=calidad_imagen, autofocus_seconds= segundos_autofoco)

        except Exception as e:
            # Si ha oucrrido un error en la captura de la foto la presentamos en los logs del sistema.

            log_event(
                title="Error al capturar la imagen ❌",
                description=f"ha ocurrido un error al capturar la imagen: {e}\n",
                type="Photo",
                important=True,
                show_time=True
            )

            return False

        # Si pudimos tomar la foto de maner exitosa mostrmoa sun log de importancia menor y retornamos un True
        log_event(
            title="La imagen se tomado con exito ✅",
            description=f"Puedes ver la imagen en: {ruta_guardado_imagenes}",
            type="Photo",
            important=False,
            show_time=True
        )

        return True

async def Take_multiple_photos(
        RUTA_GUARDADO_IMAGENES, #
        AUTOFOCUS_SECONDS: int= AUTOFOCUS_SECONDS,
        QUALITY_PHOTO: Quality = QUALITY_PHOTO,
        NUMBER_FOTOS : int= NUMBER_FOTOS,
        TIME_BETWEEN_PHOTOS : int= TIME_BETWEEN_PHOTOS,
        RETRY_TAKE_PHOTOS: bool =RETRY_TAKE_PHOTOS,
        #NUMBER_RETRYS:int= NUMBER_RETRYS
         ):
    """d
    Toma multiples fotos con las gafas, adpatandose a las configuracioens solicitadas por el usuario
    :return: Boolean y el path
    """
    numero_fotos_exitosas=0
    numero_fotos_fallidas=0
    async with Frame() as frame:
        for numero_foto_actual in range(NUMBER_FOTOS):
            log_event(
                title=f"Se tratará de tomar la foto: {numero_foto_actual}",
                description=f"",
                type="Photo",
                important=True,
                show_time=True
            )

            resultado= await Save_photo(RUTA_GUARDADO_IMAGENES, calidad_imagen = QUALITY_PHOTO,segundos_autofoco  = AUTOFOCUS_SECONDS)
            time.sleep(TIME_BETWEEN_PHOTOS)

            # vamos a llevar un conteno de cuantas fotos se tomaron y cuantas no para presentar un informe.
            # En caso de que el usuario tenga el valor de RETRY_TAKE_PHOTOS = True vamos a reintentar tomar las fotos que fallaron.

            # Nota importante: Antes de ahcer el reintento valdría la pena consultar si las gafas estan conectadas.

            if resultado:
                numero_fotos_exitosas+=1

            else:
                numero_fotos_fallidas+=1

        texto_mostrar = "Dado que no han tomado todas las fotos de manera correcta no se realizarán reintentos."   # Definimos el texto base que mostraremos en un caso optimo.

        if numero_fotos_fallidas>=1:
            texto_mostrar=f"No se han podido tomar {numero_fotos_fallidas} fotos."

            if RETRY_TAKE_PHOTOS:
                texto_mostrar+=" Se reintentará tomar las fotos fallidas de manera inmediata."

        log_event(
                title=f"Se han tomado {numero_fotos_exitosas} de manera correcta",
                description=texto_mostrar,
                type="Photo",
                important=True,
                show_time=True
        )
        if RETRY_TAKE_PHOTOS:
            # Volvemos a ejecutar la funcion si esta habilitado el reintento y lo deshabilitamos para que no se haga un loop infinito
            # Mandamos unicamente el numero de fotos fallidas para que no se intenten capturar todas las fotos.

            await Take_multiple_photos(
            RUTA_GUARDADO_IMAGENES,
            AUTOFOCUS_SECONDS,
            QUALITY_PHOTO,
            numero_fotos_fallidas,
            TIME_BETWEEN_PHOTOS,
            False # NUMBER_RETRYS:int= NUMBER_RETRYS
            )

