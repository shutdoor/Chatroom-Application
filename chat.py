import client
import asyncio
# import os

HOST = "Localhost"
PORT = 8000

async def main():
    await client.runClient(HOST, str(PORT))
    
#Creating an initializer  
if __name__=="__main__": asyncio.run(main())