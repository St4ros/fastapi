<script setup lang="ts">
interface TurnoPersona {
    id: string;
    name: string;
    fecha: string;
    fila: string;
    estado: boolean;
    turno: number;
}

const fila = ref('')

const bringLive = async () => {
    try {
        const { data, error } = useFetch<TurnoPersona>(`http://localhost:8000/consulta_turno/?fila=${fila}`);

    } catch (error) {
        console.error(error);

    }
}



</script>
<template>

    <div class="flex flex-col items-center justify-center min-h-screen p-4 bg-gray-900 text-white">
        <div class="flex flex-col items-center bg-gray-800 text-gray-300 p-6 rounded shadow-lg w-full max-w-md mb-4">
            <form @submit.prevent="bringLive">
                <label for="fila" class="text-justify titulo " >HOLA</label>
                <br/>
                <input v-model="fila" type="text" name="fila" id="fila" class="w-full px-4 py-2 bg-gray-700 text-white rounded-lg" />
                <button class="w-full py-2 bg-orange-500 text-white font-semibold rounded-lg mt-4" type="submit">Enviar</button>
        <!-- {{ data.turno }} -->
             </form>
        </div>
    </div>

         <NuxtLink to="/" class="fixed bottom-5 left-5">
            <i class="bi bi-house-fill text-white" style="font-size: 2rem;"></i>
        </NuxtLink>

</template>
<style>
@import url('https://fonts.googleapis.com/css2?family=Oswald:wght@200..700&display=swap');
.titulo{
    font-family: 'Oswald', sans-serif;
    font-size: 2rem; /* Ajusta el tamaño según tus necesidades */
    font-weight: bold;
    color: white;
}
</style>