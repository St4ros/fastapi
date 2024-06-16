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

    <form @submit.prevent="bringLive">
        <label for="fila">HOLA</label>
        <input v-model="fila" type="text" name="fila" id="fila" />
        <button type="submit">Enviar</button>
        <!-- {{ data.turno }} -->
    </form>

</template>