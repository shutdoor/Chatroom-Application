import socketio
import asyncio

# Initialize Async Client Socket
sio = socketio.AsyncClient()

#Set default Socket Connect Event to inform client of their connecting
@sio.event
async def connect():
    print("You have connected.")

#Create Socket Event that will send message to clients terminal after
#receiving it from the server
@sio.event
async def broadcast(message):
    print(message)

#Create Background Task that will allow for all clients connected to the server
#to message back and forth
async def background():
    #Boolean isActive allows for the application to know when to stop
    isActive = True
    #Create while loop that will prompt for input between sleep cycles until prompted otherwise
    while isActive:
        message = input("Message: ")
        if(message == "/exit"):
            isActive = False
            #Force the end of the script
            exit()
        else:
            #Emits types message to the server to then be broadcasted to all clients
            await sio.emit("receiver", message)
            #Wait for any incoming messages that may have been sent during input
            await sio.sleep(1)
    
#Main function of Client
async def main():
    #Prompt for Username to add diversity among connected clients
    username = input("Input Username: ")
    print("\n")
    #Connects client to server through Host - "Localhost" Port - "8000"
    #Pass X-USERNAME to the server to allow for a session to carry that name instead of
    #passing it through as a parm
    await sio.connect("http://Localhost:8000",
                    headers={"X-USERNAME": username})
    #Sleep to allow for all connections and messages to be displayed to current client
    await sio.sleep(3)               
   
    #Create background task that will prompt users for message that can then be sent to all
    #other clients
    task = await sio.start_background_task(background) 
    
    #Wait until client has connected and then wait for disconnect
    await sio.wait()


if __name__=="__main__": asyncio.run(main())