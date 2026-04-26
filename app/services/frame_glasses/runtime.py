import asyncio

# Este archivo es para poder manejar el uso de funciones dentro de los lentes; Estos no pueden realizar multiples operaciones de manera paralela.
# Modifica su estado a ocupado o desocupado; impidiendo la falla de tareas porqie estos se encuentran ocupados. Probablemente sea necesario agregar un encolamiento de funciones.

from app.services.frame_glasses.log_manager import log_event    # capturar logs asociados a los lentes.

FRAME_LOCK = asyncio.Lock()


async def Is_frame_bussy(show_log: bool) -> bool:

    """
    if show_log:
        log_event(
            title=f"Actualmente las gafas estan siendo usadas por otro proceso.",
            description=f"",
            type="Photo",
            important=False,
            show_time=True
        )
    """
    return FRAME_LOCK.locked()

