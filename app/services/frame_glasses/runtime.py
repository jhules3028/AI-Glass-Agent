import asyncio

FRAME_LOCK = asyncio.Lock()

async def Is_frame_bussy() -> bool:
    print(FRAME_LOCK)
    return FRAME_LOCK.locked()

