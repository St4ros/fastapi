<script setup lang="ts">

interface TurnoPersona {
    id: string;
    name: string;
    fecha: string;
    fila: string;
    estado: boolean;
    turno: number;
}

// Fetch data for each fila
const { data: filaa, error: errorA } = useFetch<TurnoPersona[]>('http://localhost:8000/obtener_turnos/?fila=a');
const { data: filab, error: errorB } = useFetch<TurnoPersona[]>('http://localhost:8000/obtener_turnos/?fila=b');
const { data: filac, error: errorC } = useFetch<TurnoPersona[]>('http://localhost:8000/obtener_turnos/?fila=c');
</script>

<template>
    <div>
        <!-- Tabla para fila A -->
        <h2>Turnos para Fila A</h2>
        <div v-if="errorA">Hubo un error al cargar los turnos para la fila A.</div>
        <div v-else-if="!filaa">Cargando turnos para la fila A...</div>
        <table v-else>
            <thead>
                <tr>
                    <th>ID</th>
                    <th>Nombre</th>
                    <th>Fecha</th>
                    <th>Fila</th>
                    <th>Estado</th>
                    <th>Turno</th>
                </tr>
            </thead>
            <tbody>
                <tr v-for="turno in filaa" :key="turno.id">
                    <td>{{ turno.id }}</td>
                    <td>{{ turno.name }}</td>
                    <td>{{ turno.fecha }}</td>
                    <td>{{ turno.fila }}</td>
                    <td>{{ turno.estado }}</td>
                    <td>{{ turno.turno }}</td>
                </tr>
            </tbody>
        </table>

        <!-- Tabla para fila B -->
        <h2>Turnos para Fila B</h2>
        <div v-if="errorB">Hubo un error al cargar los turnos para la fila B.</div>
        <div v-else-if="!filab">Cargando turnos para la fila B...</div>
        <table v-else>
            <thead>
                <tr>
                    <th>ID</th>
                    <th>Nombre</th>
                    <th>Fecha</th>
                    <th>Fila</th>
                    <th>Estado</th>
                    <th>Turno</th>
                </tr>
            </thead>
            <tbody>
                <tr v-for="turno in filab" :key="turno.id">
                    <td>{{ turno.id }}</td>
                    <td>{{ turno.name }}</td>
                    <td>{{ turno.fecha }}</td>
                    <td>{{ turno.fila }}</td>
                    <td>{{ turno.estado }}</td>
                    <td>{{ turno.turno }}</td>
                </tr>
            </tbody>
        </table>

        <!-- Tabla para fila C -->
        <h2>Turnos para Fila C</h2>
        <div v-if="errorC">Hubo un error al cargar los turnos para la fila C.</div>
        <div v-else-if="!filac">Cargando turnos para la fila C...</div>
        <table v-else>
            <thead>
                <tr>
                    <th>ID</th>
                    <th>Nombre</th>
                    <th>Fecha</th>
                    <th>Fila</th>
                    <th>Estado</th>
                    <th>Turno</th>
                </tr>
            </thead>
            <tbody>
                <tr v-for="turno in filac" :key="turno.id">
                    <td>{{ turno.id }}</td>
                    <td>{{ turno.name }}</td>
                    <td>{{ turno.fecha }}</td>
                    <td>{{ turno.fila }}</td>
                    <td>{{ turno.estado }}</td>
                    <td>{{ turno.turno }}</td>
                </tr>
            </tbody>
        </table>
    </div>
</template>
