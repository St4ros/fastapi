<script setup lang="ts">
import { ref, onMounted } from 'vue';
import { useRoute } from 'vue-router';

interface TurnoPersona {
    id: string;
    name: string;
    fecha: string;
    fila: string;
    estado: boolean;
    turno: number;
}

const route = useRoute();
const id = route.params.id as string;

const data1 = ref<TurnoPersona | null>(null);
const data2 = ref<TurnoPersona | null>(null);
const error1 = ref<Error | null>(null);
const error2 = ref<Error | null>(null);

const fetchTurnoPersona = async () => {
    try {
        const response = await fetch(`http://localhost:8000/encontrar_turnopersona/?id=${id}`);
        if (!response.ok) {
            throw new Error('Network response was not ok');
        }
        data1.value = await response.json();
    } catch (err) {
        error1.value = err as Error;
        console.error(error1.value);
    }
};

const fetchConsultaTurno = async () => {
    if (data1.value?.fila) {
        try {
            const response = await fetch(`http://localhost:8000/consulta_turno/?fila=${data1.value.fila}`);
            if (!response.ok) {
                throw new Error('Network response was not ok');
            }
            data2.value = await response.json();
        } catch (err) {
            error2.value = err as Error;
            console.error(error2.value);
        }
    }
};

onMounted(async () => {
    await fetchTurnoPersona();
    await fetchConsultaTurno();
});
</script>

<template>
    <div class="flex flex-col items-center justify-center min-h-screen p-4 fondo text-white">
        <!-- Turno y Caja en Vivo -->
        <div class="flex flex-col items-center bg-gray-800 text-gray-300 p-6 rounded shadow-lg w-full max-w-md mb-4">
            <div class="text-4xl font-bold">Turno</div>
            <div class="text-6xl font-extrabold">{{ data2?.turno || '---' }}</div>
        </div>

        <!-- Datos del usuario -->
        <div class="flex flex-col items-center bg-gray-800 text-gray-300 p-4 rounded shadow-lg w-full max-w-md">
            <p class="text-lg font-semibold">Detalles para el id {{ id }}</p>
            <h1 class="text-2xl font-bold mt-2">Bienvenido usuario {{ data1?.name }}</h1>
            <div v-if="data1" class="mt-4">
                <p class="text-xl">Turno: {{ data1.turno }}</p>
                <p class="text-xl">Fila: {{ data1.fila }}</p>
            </div>
        </div>
    </div>
</template>

<style scoped>
body {
    font-family: 'Arial', sans-serif;
}
</style>
