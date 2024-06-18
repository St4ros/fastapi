<script setup lang="ts">

interface TurnoPersona {
    id: string;
    name: string;
    fecha: string;
    fila: string;
    estado: boolean;
    turno: number;
}

const { id } = useRoute().params
// const { data, error } = await useFetch<TurnoPersona>(`http://localhost:8000/encontrar_turnopersona/?id=${id}`)

// Primera petición GET
const { data: data1, error: error1 } = useFetch<TurnoPersona>(`http://localhost:8000/encontrar_turnopersona/?id=${id}`);

// Segunda petición GET
const { data: data2, error: error2 } = useFetch<TurnoPersona>(`http://localhost:8000/consulta_turno/?fila=${data1.value?.fila}`);


</script>

<template>
    <div class="flex flex-col items-center justify-center min-h-screen p-4 bg-gray-900 text-white">
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
            <NuxtLink to="/" class="fixed bottom-5 left-5">
              <i class="bi bi-house-fill text-white" style="font-size: 2rem;"></i>
            </NuxtLink>
</template>

<style scoped>
body {
    font-family: 'Arial', sans-serif;
}
</style>