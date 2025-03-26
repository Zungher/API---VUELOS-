import requests
from bs4 import BeautifulSoup
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import List

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class Vuelo(BaseModel):
    vuelo: str
    destino: str
    hora: str
    puerta: str
    estado: str

@app.get("/salidas", response_model=List[Vuelo])
def obtener_vuelos():
    url = "http://salidas.dgac.gob.gt/vuelos/pantallas/salidas.php"
    response = requests.get(url)
    soup = BeautifulSoup(response.content, "html.parser")

    vuelos = []
    filas = soup.select("table tr")[1:]  # saltamos el encabezado

    for fila in filas:
        columnas = fila.find_all("td")
        if len(columnas) == 6:
            vuelo = Vuelo(
                hora=columnas[0].text.strip(),
                destino=columnas[1].text.strip(),
                vuelo=columnas[2].text.strip(),
                puerta=columnas[4].text.strip(),
                estado=columnas[5].text.strip(),
            )
            vuelos.append(vuelo)

    return vuelos
