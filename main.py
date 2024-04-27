from fastapi import FastAPI

# uvicorn main:app To run the app
# --reload to reload the app when you make changes
# --port 8000 to run the app on a specific port
# --host 0.0.0.0 to run the app on all the network interfaces

# /docs and /redoc to acces to the documentation by FastAPI

app = FastAPI()

app.title = "ChordokuAPI"

chordoku_info = {
    "version" : {
        "web_version": 1.0
    }
}



@app.get("/version", tags=["info"])
def get_version():
    return {chordoku_info["version"]["web_version"]}
