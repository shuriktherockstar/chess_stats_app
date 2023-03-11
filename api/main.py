from fastapi import FastAPI
from routers import router_players, router_games

app = FastAPI()

app.include_router(router_players)
app.include_router(router_games)