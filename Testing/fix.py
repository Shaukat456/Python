import asyncio


async def fetch_data():
    # Simulate a network request
    await asyncio.sleep(1)
    return "data"


# To run the coroutine:
result = asyncio.run(fetch_data())
print(result)
