from fastapi import FastAPI, Form, HTTPException
from motor.motor_asyncio import AsyncIOMotorClient
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware
from fastapi import FastAPI, HTTPException

from bson.json_util import dumps

app = FastAPI()

# Configuración de la base de datos
MONGO_DETAILS = "mongodb://localhost:27017"  # URL de conexión a MongoDB
client = AsyncIOMotorClient(MONGO_DETAILS)
database = client.turnos  # Nombre de la base de datos
inscritos = database.inscritos  # Nombre de la colección
fila1 = database.fila1  # Nombre de la colección
fila2 = database.fila2  # Nombre de la colección
fila3 = database.fila3  # Nombre de la colección

# Configuración de CORS
origins = [
    "http://localhost:8000",
    "http://localhost",
]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Modelo Pydantic
class Turno(BaseModel):
    id: str
    name: str
    fecha: str

@app.post("/registrar/")
async def assign_turn(id: str = Form(...), name: str = Form(...), fecha: str = Form(...)):
    # Insertar el nuevo turno en la base de datos
    turno_data = {"id": id, "name": name, "fecha": fecha}
    result = await inscritos.insert_one(turno_data)
    
    if result.inserted_id:
        return {"message": "Turno asignado correctamente"}
    raise HTTPException(status_code=400, detail="Error al asignar el turno")

@app.post("/setfila/")
async def assign_turn_to_fila(name: str = Form(...), id: str = Form(...), fila: str = Form(...)):
    # Consultar el número de turno más grande de la fila correspondiente
    if fila == "a":
        max_turno = await fila1.find_one(sort=[("turno", -1)])
    elif fila == "b":
        max_turno = await fila2.find_one(sort=[("turno", -1)])
    elif fila == "c":
        max_turno = await fila3.find_one(sort=[("turno", -1)])
    else:
        raise HTTPException(status_code=404, detail="Fila no encontrada")

    next_turno = max_turno["turno"] + 1 if max_turno else 1

    # Insertar el dato en la fila correspondiente
    turno_data = {"name": name, "id": id, "turno": next_turno}
    if fila == "a":
        result = await fila1.insert_one(turno_data)
    elif fila == "b":
        result = await fila2.insert_one(turno_data)
    elif fila == "c":
        result = await fila3.insert_one(turno_data)

    if result.inserted_id:
        return {"message": "Turno asignado correctamente"}
    raise HTTPException(status_code=400, detail="Error al asignar el turno")

@app.get("/getturnofila/{fila}")
async def get_current_turn(fila: str):
    if fila == "a":
        max_turno = await fila1.find_one(sort=[("turno", 1)])
    elif fila == "b":
        max_turno = await fila2.find_one(sort=[("turno", 1)])
    elif fila == "c":
        max_turno = await fila3.find_one(sort=[("turno", 1)])
    else:
        raise HTTPException(status_code=404, detail="Fila no encontrada")

    if max_turno and "turno" in max_turno:
        current_turno = max_turno["turno"]
        return {"turno": current_turno}
    raise HTTPException(status_code=404, detail="No se encontró ningún turno registrado")

@app.get("/verificar/{id}")
async def verificar_id(id: str):
    user = await inscritos.find_one({"id": id})
    if user:
        return {"name": user["name"], "fecha": user["fecha"]}
    raise HTTPException(status_code=404, detail="ID no encontrado")

@app.get("/nombref/{id}{fila}")
async def verificar_name(id: str, fila: str):
    if fila == "a":
        user = await fila1.find_one({"id": id})
    elif fila == "b":
        user = await fila2.find_one({"id": id})
    elif fila == "c":
        user = await fila3.find_one({"id": id})
    else:
        raise HTTPException(status_code=404, detail="Fila no encontrada")

    if user:
        return {"turno": user["turno"], "name": user["name"]}
    raise HTTPException(status_code=404, detail="Usuario no encontrado en la fila")

@app.delete("/eliminarf/{turno}{fila}")
async def eliminar_turno(turno: int, fila: str):
    if fila == "a":
        result = await fila1.delete_one({"turno": turno})
    elif fila == "b":   
        result = await fila2.delete_one({"turno": turno})
    elif fila == "c":
        result = await fila3.delete_one({"turno": turno})
    else:
        raise HTTPException(status_code=400, detail="Fila no válida")

    if result.deleted_count == 1:
        return {"message": "Turno eliminado correctamente"}
    raise HTTPException(status_code=404, detail="Turno no encontrado en la fila")


@app.get("/ultimascincofilas/{fila}")
async def get_ultimas_cinco_filas(fila: str): 
    # Obtener las últimas 5 filas de la colección especificada
    if fila == "a":
        ultimas_cinco_filas_cursor = fila1.find({}, {"_id": 0, "name": 1, "turno": 1}).sort("_id", -1).limit(5)
    elif fila == "b":
        ultimas_cinco_filas_cursor = fila2.find({}, {"_id": 0, "name": 1, "turno": 1}).sort("_id", -1).limit(5)
    elif fila == "c":
        ultimas_cinco_filas_cursor = fila3.find({}, {"_id": 0, "name": 1, "turno": 1}).sort("_id", -1).limit(5)
    else:
        raise HTTPException(status_code=400, detail="Fila no válida")
    
    # Convertir el cursor a una lista de diccionarios
    ultimas_cinco_filas_list = await ultimas_cinco_filas_cursor.to_list(length=5)
    
    # Devolver los datos en formato JSON
    return dumps(ultimas_cinco_filas_list)