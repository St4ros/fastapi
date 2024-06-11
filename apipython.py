from fastapi import FastAPI, HTTPException
from motor.motor_asyncio import AsyncIOMotorClient
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware
from typing import Optional
from typing import List

app = FastAPI()

# Database configuration
MONGO_DETAILS = "mongodb://localhost:27017"
client = AsyncIOMotorClient(MONGO_DETAILS)
database = client.turnos
inscritos = database.inscritos
fila1 = database.fila1
fila2 = database.fila2
fila3 = database.fila3

# Configuración de CORS
origins = [
    "http://localhost:8000",
    "http://localhost",
]

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
    turno: Optional[int] = None  # Hacer turno opcional

class Inscritos(BaseModel):
    id: str
    name: str
    fecha: str




#se ovtirne los datos para inscrivirlo y se lo inscrive
#se le pasa id-name-fecha
#retorna json con los datos de la inscripcion
@app.post("/registrar/", response_model=Inscritos)
async def register_inscrito(inscrito: Inscritos):
    inscrito_data = inscrito.dict()
    result = await inscritos.insert_one(inscrito_data)
    
    if result.inserted_id:
        return inscrito_data  # Retornar los datos del inscrito como JSON
    raise HTTPException(status_code=400, detail="Error al registrar el inscrito")


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
    


#se ovtirne los datos para asignarle turno y se le asigna el turno a la fila correspondiente
#se le pasa id-name-fecha-fial(a,b,c)-estado(opcional)
#retorna json con los datos del turno
@app.post("/asignar_turno/", response_model=Turno)
async def asignar_turno(turno: Turno):
    turno_data = turno.dict()
    nuevo_turno = await getTurno(turno_data["fila"])
    turno_data["turno"] = nuevo_turno
    fila_collection = None

    if turno_data["fila"] == "a":
        fila_collection = fila1
    elif turno_data["fila"] == "b":
        fila_collection = fila2
    elif turno_data["fila"] == "c":
        fila_collection = fila3
    else:
        raise HTTPException(status_code=400, detail="Fila inválida")

    result = await fila_collection.insert_one(turno_data)
    
    if result.inserted_id:
        return turno_data
    raise HTTPException(status_code=400, detail="Error al asignar el turno")



#se ovtine la fila y el turno con el # mas bajo y estado false se cambia a estado true
#se le pasa un string fial(a,b,c)
#no retorna nada
class UpdateTurnoRequest(BaseModel):
    fila: str
    
@app.patch("/actualizar_turno/", response_model=Turno)
async def actualizar_turno(request: UpdateTurnoRequest):
    fila_collection = None
    if request.fila == "a":
        fila_collection = fila1
    elif request.fila == "b":
        fila_collection = fila2
    elif request.fila == "c":
        fila_collection = fila3
    else:
        raise HTTPException(status_code=400, detail="Fila inválida")

    # Encontrar el turno más pequeño con estado false
    turno_document = await fila_collection.find_one(
        {"estado": False}, 
        sort=[("turno", 1)]
    )

    if turno_document:
        # Actualizar el estado a true
        update_result = await fila_collection.update_one(
            {"_id": turno_document["_id"]},
            {"$set": {"estado": True}}
        )

        if update_result.modified_count == 1:
            return {**turno_document, "estado": True}
    
    raise HTTPException(status_code=400, detail="No se encontró un turno para actualizar")


#se ovtirne los 5 primeros turnos
#se le pasa fial(a,b,c)
#retorna json con los 5 primeros turnos de la fila correspondiente

class Turno(BaseModel):
    turno: int
    estado: bool

class ConsultaTurnosRequest(BaseModel):
    fila: str

@app.get("/obtener_turnos/", response_model=List[Turno])
async def cobtener_turnos(request: ConsultaTurnosRequest):
    fila_collection = None
    if request.fila == "a":
        fila_collection = fila1
    elif request.fila == "b":
        fila_collection = fila2
    elif request.fila == "c":
        fila_collection = fila3
    else:
        raise HTTPException(status_code=400, detail="Fila inválida")

    # Encontrar los 5 turnos más pequeños con estado false
    turnos_cursor = fila_collection.find(
        {"estado": False},
        sort=[("turno", 1)],
        limit=5
    )

    turnos = await turnos_cursor.to_list(length=5)

    if turnos:
        return turnos
    
    raise HTTPException(status_code=404, detail="No se encontraron turnos con el estado false")



##############################################################



















































"""
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
    raise HTTPException(status_code=400, detail="Error al asignar el turno")"""

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