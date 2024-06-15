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
    <p>Detalles para el id {{ id }}</p>
    <!-- estos son los datos del señor que le dieron turno con el id de arriba -->
    <h1>Bienvenido usuario {{ data1?.name }}</h1>

    <div v-if="data1">
        <p>Turno: {{ data1.turno }}</p>
        <p>Fila: {{ data1.fila }}</p>
    </div>

    <!-- este es el turno en vivo para la fila en la que se registra el señor de este turno -->
    <p>{{ data2?.turno }}</p>
</template>