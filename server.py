import socketio

sio = socketio.AsyncServer(async_mode='asgi')
app = socketio.ASGIApp(sio, static_files={
    '': ''
})

@sio.event
async def connect(sid, environ):
    username = environ.get("HTTP_X_USERNAME")
    async with sio.session(sid) as session:
        session['username'] = username
    await sio.emit('broadcast', username + " has connected")

@sio.event
async def disconnect(sid):
    async with sio.session(sid) as session:
        await sio.emit('broadcast', session["username"] + " has disconnected")

@sio.event
async def message(sid, data):
    print(sid," ",data)
    await sio.emit("broadcast", message)

@sio.event
async def receiver(sid, data):
    async with sio.session(sid) as session:
        message = session["username"] + " " +data
    await sio.emit("broadcast", message)
