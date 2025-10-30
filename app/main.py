from fastapi import FastAPI
from app.routers import auth, pokedex, pokemon, teams

app = FastAPI(title="Pokedex API")

# Registramos routers
app.include_router(auth.router)
app.include_router(pokedex.router)
app.include_router(pokemon.router)
app.include_router(teams.router)

# Endpoint raíz
@app.get("/")
def root():
    return {"message": "Bienvenido a la Pokedex API 🧩"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("app.main:app", host="127.0.0.1", port=8000, reload=True)

