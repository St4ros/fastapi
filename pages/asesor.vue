<script setup lang="ts">
import { ref } from 'vue';

interface TurnoPersona {
    id: string;
    name: string;
    fecha: string;
    fila: string;
    estado: boolean;
    turno: number;
}

const fila = ref('');
const data = ref<TurnoPersona | null>(null);
const error = ref<Error | null>(null);

const bringLive = async () => {
    try {
        const updateResponse = await fetch(`http://localhost:8000/actualizar_turno/`, {
            method: 'PATCH',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({ fila: fila.value }),
        });

        if (!updateResponse.ok) {
            throw new Error('Ultimo turno de esta fila Eliminado');
        }

        const response = await fetch(`http://localhost:8000/consulta_turno/?fila=${fila.value}`);
        if (!response.ok) {
            throw new Error('Ultimo turno de esta fila Eliminado');
        }

        data.value = await response.json();
    } catch (err) {
        error.value = err as Error;
        console.error(error.value);
    }
};
</script>

<template>
    <div class="flex flex-col items-center justify-center min-h-screen p-4 bg-gray-900 text-white">
        <div class="flex flex-col items-center bg-gray-800 text-gray-300 p-6 rounded shadow-lg w-full max-w-md mb-4">
            <form @submit.prevent="bringLive">
                <label for="fila" class="text-justify titulo">HOLA</label>
                <div class="mb-4">
                    <label for="row" class="block text-gray-300 mb-2">Seleccione fila</label>
                    <select v-model="fila" name="row" id="row" class="w-full px-4 py-2 bg-gray-700 text-white rounded-lg" required>
                        <option value="a">Pagos</option>
                        <option value="b">Pqrs</option>
                        <option value="c">Preferencial</option>
                    </select>
                </div>
                <input v-model="fila" type="text" name="fila" id="fila" class="w-full px-4 py-2 bg-gray-700 text-white rounded-lg" />
                <button class="w-full py-2 bg-orange-500 text-white font-semibold rounded-lg mt-4" type="submit">Enviar</button>
            </form>
            <div v-if="data" class="mt-4">
                <p class="text-xl">Turno: {{ data.turno }}</p>
                <p class="text-xl">Fila: {{ data.fila }}</p>
                <p class="text-xl">Estado: {{ data.estado ? 'True' : 'False' }}</p>
            </div>
            <div v-if="error" class="mt-4 text-red-500">
                Error: {{ error.message }}
            </div>
        </div>
    </div>
    <NuxtLink to="/" class="fixed bottom-5 left-5">
        <i class="bi bi-house-fill text-white" style="font-size: 2rem;"></i>
    </NuxtLink>
</template>

<style>
@import url('https://fonts.googleapis.com/css2?family=Oswald:wght@200..700&display=swap');
.titulo {
    font-family: 'Oswald', sans-serif;
    font-size: 2rem; /* Ajusta el tamaño según tus necesidades */
    font-weight: bold;
    color: white;
}
</style>
