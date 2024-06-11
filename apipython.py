from fastapi import FastAPI, HTTPException
from motor.motor_asyncio import AsyncIOMotorClient
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware
from typing import Optional

app = FastAPI()

# Database configuration
MONGO_DETAILS = "mongodb://localhost:27017"
client = AsyncIOMotorClient(MONGO_DETAILS)
database = client.turnos
inscritos = database.inscritos
fila1 = database.fila1
fila2 = database.fila2
fila3 = database.fila3

# CORS configuration
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allow all origins for debugging
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Pydantic models
class Turno(BaseModel):
    id: str
    name: str
    fecha: str
    fila: str
    estado: Optional[bool] = False
    turno: int

class FilaTurno(BaseModel):
    name: str
    id: str
    fila: str
    estado: bool

# Helper function to get the next turno number
async def get_next_turno(fila_collection):
    max_turno = await fila_collection.find_one(sort=[("turno", -1)])
    return max_turno["turno"] + 1 if max_turno else 1

@app.post("/registrar/")
async def assign_turn(turno: Turno):
    turno.turno = await getTurno(turno)  # Asignar el número de turno
    turno_data = turno.dict()
    result = await inscritos.insert_one(turno_data)
    
    if result.inserted_id:
        return {"message": "Turno asignado correctamente"}
    raise HTTPException(status_code=400, detail="Error al asignar el turno")


############################################333nueva funciones
#se ovtirne el un el turno mas alto de la fila y se le suma uno y retorna el numero
#se le pasa un string fial(a,b,c)
#retorna un numero
async def getTurno(fila: str):
    # Determinar la colección según la fila recibida
    fila_collection = None
    if fila == "a":
        fila_collection = fila1
    elif fila == "b":
        fila_collection = fila2
    elif fila == "c":
        fila_collection = fila3
    else:
        raise HTTPException(status_code=400, detail="Fila inválida")

    # Obtener el número de turno más alto de la fila correspondiente
    max_turno = await fila_collection.find_one(sort=[("turno", -1)])
    
    if max_turno:
        return max_turno["turno"] + 1
    else:
        return 1
    
#se ovtine la fila y el turno con el # mas bajo y estado false se cambia a estado true
#se le pasa un string fial(a,b,c)
#no retorna nada
@app.patch("/actualizar_estado_atendido/")
async def actualizar_estado_atendido(fila: str):
    # Determinar la colección según la fila recibida
    fila_collection = None
    if fila == "a":
        fila_collection = fila1
    elif fila == "b":
        fila_collection = fila2
    elif fila == "c":
        fila_collection = fila3
    else:
        raise HTTPException(status_code=400, detail="Fila inválida")

    # Buscar el turno con el número más bajo y estado false
    turno_a_actualizar = await fila_collection.find_one_and_update(
        {"estado": False},
        {"$set": {"estado": True}},
        sort=[("turno", 1)],
        return_document=True
    )
    
    if turno_a_actualizar:
        return {"message": "Estado del turno actualizado correctamente"}
    else:
        raise HTTPException(status_code=404, detail="No se encontró un turno pendiente en la fila especificada")

##############################################################




















































@app.post("/setfila/")
async def assign_turn_to_fila(fila_turno: FilaTurno):
    if fila_turno.fila == "a":
        fila_collection = fila1
    elif fila_turno.fila == "b":
        fila_collection = fila2
    elif fila_turno.fila == "c":
        fila_collection = fila3
    else:
        raise HTTPException(status_code=404, detail="Fila no encontrada")

    next_turno = await get_next_turno(fila_collection)
    turno_data = fila_turno.dict()
    turno_data["turno"] = next_turno
    result = await fila_collection.insert_one(turno_data)

    if result.inserted_id:
        return {"message": "Turno asignado correctamente"}
    raise HTTPException(status_code=400, detail="Error al asignar el turno")

@app.get("/getturnofila/{fila}")
async def get_current_turn(fila: str):
    if fila == "a":
        fila_collection = fila1
    elif fila == "b":
        fila_collection = fila2
    elif fila == "c":
        fila_collection = fila3
    else:
        raise HTTPException(status_code=404, detail="Fila no encontrada")

    max_turno = await fila_collection.find_one(sort=[("turno", 1)])
    if max_turno:
        return {"turno": max_turno["turno"]}
    raise HTTPException(status_code=404, detail="No se encontró ningún turno registrado")

@app.get("/verificar/{id}")
async def verificar_id(id: str):
    user = await inscritos.find_one({"id": id})
    if user:
        return {"name": user["name"], "fecha": user["fecha"], "estado": user["estado"]}
    raise HTTPException(status_code=404, detail="ID no encontrado")

@app.get("/nombref/{id}/{fila}")
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

@app.delete("/eliminarf/{turno}/{fila}")
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

inscritos_collection = database["inscritos"]  # Replace with your actual collection name

@app.get("/inscritos/")
async def get_all_inscritos():
    documents = inscritos_collection.find()
    return documents