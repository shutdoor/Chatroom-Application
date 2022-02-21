## Application Description:
    This application is just a simple chat application that allows for
    several clients to connect to a server and chat.

## Application Specifics:
    This application's server & client are running on Host = "Localhost" & Port = "8000".

## Created Using:
    Python & Default Libraries
    python-socketio[asyncio_client]
    python-socketio
    uvicorn

## Requires the instillation of:
    pip install "python-socketio[asyncio_client]"
    pip install python-socketio
    pip install "uvicorn[standard]"

## Commands to run:
    Server:
        python -m uvicorn server:app --reload
    Client: 
        py chat.py
