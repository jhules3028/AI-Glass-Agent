# Repositorio que sirvio de apoyo para el desarrollo de esta seccion: https://github.com/CitizenOneX/frame_examples_python/blob/main/frame_msg/manual_exposure.py
# En este apartado podras ver la parte del servicio asociado a como toamr fotos con los lentes, asi como la ruta en la cual se guardan las fotos

import asyncio

import io
from fileinput import filename
from pathlib import Path
from PIL import Image

# Librerias necesarias para el uso de las gafas

from frame_sdk import Frame
from frame_sdk.camera import AutofocusType, Quality


# Archivo de configuraciones
from app.services.frame_glasses.config import RUTA_GUARDADO_IMAGENES


async def take_photo():
    """
    Toma una foto con las gafas

    :return:  Boolean y el path
    """
    async with Frame() as frame:
        frame.camera.take_photo(RUTA_GUARDADO_IMAGENES, quality=Quality.HIGH)

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
        frame.camera.s
