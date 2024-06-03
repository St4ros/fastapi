//obtiene el ultimo tueno de la fila correspondiente
async function TurnoActualf(fila) {
    const response = await fetch(`http://localhost:8000/getturnofila/${fila}`);
    const data = await response.json();

    document.getElementById('current-turno').innerText = data.turno;
}

async function Datoslocales(fila) {
    //recupera el id local
    const userData = JSON.parse(localStorage.getItem('userData'));
    
    const response = await fetch(`http://localhost:8000/nombref/${userData.id}${fila}`);
    const data = await response.json();

    document.getElementById('mi-turno').innerText = data.name;
    document.getElementById('mi-nombre').innerText = data.turno;
}


//registra en en registrados y añade el turno
function Registrar(fila) {
    const form = document.getElementById('turnoForm');
    form.addEventListener('submit', async function(event) {
        event.preventDefault();
        
        const id = document.getElementById('inputID').value;
        const name = document.getElementById('inputName').value;
        const fecha = document.getElementById('inputFecha').value;
    
        try {
            const response = await fetch('http://localhost:8000/registrar/', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/x-www-form-urlencoded',
                },
                body: new URLSearchParams({
                    'id': id,
                    'name': name,
                    'fecha': fecha
                })
            });
    
            if (response.ok) {
                console.log('Turno asignado correctamente');
            } else {
                console.error('Error al asignar el registro', response);
                alert('Error al asignar el turno');
            }
            filas=fila;
            turnofila(filas);

        } catch (error) {
            console.error('Error al realizar la solicitud:', error);
            alert('Error al realizar la solicitud');
        }
    });
}

//verifica si el id esta en alguna de las filas y si no lo añade a la fila
async function turnofila(fila) {
    //fila="a";
    try {
        const id = document.getElementById('inputID').value;
        const name = document.getElementById('inputName').value;

        const response = await fetch(`http://localhost:8000/nombref/${id}${fila}`);
        if (response.ok) {
            //guarda el id en un usuario local
            localStorage.setItem('userData', JSON.stringify({ id: id}));
            //pasa a la otra pagina si esta
            window.location.href = 'mturno.html';
        }else{
            //esto lo añade si no esta
            const response1 = await fetch('http://localhost:8000/setfila/', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/x-www-form-urlencoded',
                },
                body: new URLSearchParams({
                    'name': name,
                    'id': id,
                    'fila': fila
                })
            });            
            if (response1.ok){
                console.log('Turno asignado correctamente');
                //guarda el id en un usuario local
                localStorage.setItem('userData', JSON.stringify({ id: id}));

                window.location.href = 'mturno.html';
            } else {
                console.error('Error al asignar el turno', response);
                alert('Error al asignar el turno');
            }
        }
    } catch (error) {
    }
};



//verifica si el id esta, si esta auto completa y pasa si no deja que el usuario llene
async function verificarID(fila) {
    const id = document.getElementById('inputID').value;
    try {
      const response = await fetch(`http://localhost:8000/verificar/${id}`);
      if (response.ok) {
        const data = await response.json();
        document.getElementById('inputName').value = data.name;
        document.getElementById('inputFecha').value = data.fecha;
        //si esta en la fila lo añade sino no
        turnofila(fila);
        window.location.href = 'mturno.html';
      } else {
        document.getElementById('inputName').value = '';
        document.getElementById('inputFecha').value = '';
      }
    } catch (error) {
      console.error('Error al verificar el ID:', error);
    }
}

//manda a eliminar el dato segun la fila
async function Eliminarf(turno,fila) {
    try {
        const response = await fetch(`http://localhost:8000/eliminarf/${turno}${fila}`, {
            method: 'DELETE'
        });

        if (response.ok) {
            const data = await response.json();
            console.log(data.message);
        } else {
            console.error('Error al eliminar el recurso:', response.statusText);
        }
    } catch (error) {
        console.error('Error al hacer la solicitud:', error);
    }
}

