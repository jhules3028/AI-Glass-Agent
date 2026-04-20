# Repositorio que sirvio de apoyo para el desarrollo de esta seccion: https://github.com/CitizenOneX/frame_examples_python/blob/main/frame_msg/manual_exposure.py
# En este apartado podras ver la parte del servicio asociado a como toamr fotos con los lentes, asi como la ruta en la cual se guardan las fotos


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

from app.services.frame_glasses.config import RUTA_GUARDADO_IMAGENES,AUTOFOCUS_SECONDS,QUALITY_PHOTO,NUMBER_FOTOS,TIME_BETWEEN_PHOTOS
from app.services.frame_glasses.log_manager import log_event

async def save_photo(
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

async def take_multiple_photos(
        RUTA_GUARDADO_IMAGENES, #
        autofocus_seconds: int,
        quality: Quality = Quality.HIGH
    ):

    #  filename=RUTA_GUARDADO_IMAGENES

    """
    Toma multiples fotos con las gafas, adpatandose a las configuracioens solicitadas por el usuario
    :return: Boolean y el path
    """

    async with Frame() as frame:
        frame.camera.save_photo(RUTA_GUARDADO_IMAGENES, quality=Quality.HIGH)


        time.sleep(1)