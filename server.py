import socketio

# Initialize Async Server Socket
sio = socketio.AsyncServer(async_mode='asgi')
# Initialize Async Server Socket ASGIApp
app = socketio.ASGIApp(sio, static_files={'': ''})

#Server Socket Default Connect Event
#Pull username from the header X-USERNAME and then set the session["username"] to that
#Use Sockets Session with clients sid to pull their session
#Then broadcast that the username + " has connected" 
@sio.event
async def connect(sid, environ):
    username = environ.get("HTTP_X_USERNAME")
    async with sio.session(sid) as session:
        session['username'] = username
    await sio.emit('broadcast', username + " has connected")

#Server Socket Default Disconnect Event
#Use Sockets Session with clients sid to pull their session
#Get username from session["username"]
#Then broadcast that the username + " has disconnected" 
@sio.event
async def disconnect(sid):
    async with sio.session(sid) as session:
        #Emit to Client broadcast event
        await sio.emit('broadcast', session["username"] + " has disconnected")

#Server Socket Event that will receive data.
#Then broadcast that data to all connected clients
@sio.event
async def message(sid, data):
    print(sid," ",data)
    #Emit data to Client broadcast event
    await sio.emit("broadcast", message)

#Server Socket Event that will receive data add the client's username to the front of it.
#Then broadcast it to all connected clients
@sio.event
async def receiver(sid, data):
    async with sio.session(sid) as session:
        message = session["username"] + " " +data
    #Emit message string to Client broadcast event
    await sio.emit("broadcast", message)
