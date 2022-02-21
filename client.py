import socketio

sio = socketio.AsyncClient()

@sio.event
async def connect():
    print("You have connected.")

@sio.event
async def disconnect():
    print("")

@sio.event
async def connect_error(e):
    print(e)

@sio.event
async def broadcast(message):
    print(message)

async def background():
    isActive = True
    while isActive:
        message = input("Message: ")
        if(message == "/exit"):
            isActive = False
            await sio.disconnect()
        else:
            await sio.emit("receiver", message)
            await sio.sleep(1)
    
async def runClient(HOST, PORT):
    username = input("Input Username: ")
    print("\n")
    await sio.connect("http://"+ HOST +":"+ PORT,
                    headers={"X-USERNAME": username})
    await sio.sleep(3)               
   
    # task = await sio.start_background_task(background) 
    
    isActive = True
    while isActive:
        message = input("Message: ")
        if(message == "/exit"):
            isActive = False
            await sio.disconnect()
        else:
            await sio.emit("receiver", message)
            await sio.sleep(1)
    
    await sio.wait()
