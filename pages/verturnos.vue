

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
    <div class="flex flex-col items-center h-screen fondo text-white p-12">
        <div class="flex justify-between w-full max-w-6xl mb-16">
            <!-- Tabla para fila A -->
            <div class="w-1/2 px-4">
                <h2 class="text-xl font-bold mb-4">Turnos para Fila A</h2>
                <div v-if="errorA" class="text-red-500">Hubo un error al cargar los turnos para la fila A.</div>
                <div v-else-if="!filaa" class="text-gray-500">Cargando turnos para la fila A...</div>
                <table v-else class="min-w-full bg-gray-800 shadow-md rounded-lg">
                    <thead>
                        <tr>
                            <th class="py-2 px-4 border-b border-gray-700">ID</th>
                            <th class="py-2 px-4 border-b border-gray-700">Nombre</th>
                            <th class="py-2 px-4 border-b border-gray-700">Fecha</th>
                            <th class="py-2 px-4 border-b border-gray-700">Fila</th>
                            <th class="py-2 px-4 border-b border-gray-700">Estado</th>
                            <th class="py-2 px-4 border-b border-gray-700">Turno</th>
                        </tr>
                    </thead>
                    <tbody>
                        <tr v-for="turno in filaa" :key="turno.id">
                            <td class="py-2 px-4 border-b border-gray-700">{{ turno.id }}</td>
                            <td class="py-2 px-4 border-b border-gray-700">{{ turno.name }}</td>
                            <td class="py-2 px-4 border-b border-gray-700">{{ turno.fecha }}</td>
                            <td class="py-2 px-4 border-b border-gray-700">{{ turno.fila }}</td>
                            <td class="py-2 px-4 border-b border-gray-700">{{ turno.estado }}</td>
                            <td class="py-2 px-4 border-b border-gray-700">{{ turno.turno }}</td>
                        </tr>
                    </tbody>
                </table>
            </div>

            <!-- Tabla para fila B -->
            <div class="w-1/2 px-4">
                <h2 class="text-xl font-bold mb-4">Turnos para Fila B</h2>
                <div v-if="errorB" class="text-red-500">Hubo un error al cargar los turnos para la fila B.</div>
                <div v-else-if="!filab" class="text-gray-500">Cargando turnos para la fila B...</div>
                <table v-else class="min-w-full bg-gray-800 shadow-md rounded-lg">
                    <thead>
                        <tr>
                            <th class="py-2 px-4 border-b border-gray-700">ID</th>
                            <th class="py-2 px-4 border-b border-gray-700">Nombre</th>
                            <th class="py-2 px-4 border-b border-gray-700">Fecha</th>
                            <th class="py-2 px-4 border-b border-gray-700">Fila</th>
                            <th class="py-2 px-4 border-b border-gray-700">Estado</th>
                            <th class="py-2 px-4 border-b border-gray-700">Turno</th>
                        </tr>
                    </thead>
                    <tbody>
                        <tr v-for="turno in filab" :key="turno.id">
                            <td class="py-2 px-4 border-b border-gray-700">{{ turno.id }}</td>
                            <td class="py-2 px-4 border-b border-gray-700">{{ turno.name }}</td>
                            <td class="py-2 px-4 border-b border-gray-700">{{ turno.fecha }}</td>
                            <td class="py-2 px-4 border-b border-gray-700">{{ turno.fila }}</td>
                            <td class="py-2 px-4 border-b border-gray-700">{{ turno.estado }}</td>
                            <td class="py-2 px-4 border-b border-gray-700">{{ turno.turno }}</td>
                        </tr>
                    </tbody>
                </table>
            </div>
        </div>

        <!-- Tabla para fila C (centrada en la parte inferior) -->
        <div class="w-full max-w-3xl mt-10">
            <h2 class="text-xl font-bold mb-4 text-center">Turnos para Fila C</h2>
            <div v-if="errorC" class="text-red-500 text-center">Hubo un error al cargar los turnos para la fila C.</div>
            <div v-else-if="!filac" class="text-gray-500 text-center">Cargando turnos para la fila C...</div>
            <table v-else class="min-w-full bg-gray-800 shadow-md rounded-lg">
                <thead>
                    <tr>
                        <th class="py-2 px-4 border-b border-gray-700">ID</th>
                        <th class="py-2 px-4 border-b border-gray-700">Nombre</th>
                        <th class="py-2 px-4 border-b border-gray-700">Fecha</th>
                        <th class="py-2 px-4 border-b border-gray-700">Fila</th>
                        <th class="py-2 px-4 border-b border-gray-700">Estado</th>
                        <th class="py-2 px-4 border-b border-gray-700">Turno</th>
                    </tr>
                </thead>
                <tbody>
                    <tr v-for="turno in filac" :key="turno.id">
                        <td class="py-2 px-4 border-b border-gray-700">{{ turno.id }}</td>
                        <td class="py-2 px-4 border-b border-gray-700">{{ turno.name }}</td>
                        <td class="py-2 px-4 border-b border-gray-700">{{ turno.fecha }}</td>
                        <td class="py-2 px-4 border-b border-gray-700">{{ turno.fila }}</td>
                        <td class="py-2 px-4 border-b border-gray-700">{{ turno.estado }}</td>
                        <td class="py-2 px-4 border-b border-gray-700">{{ turno.turno }}</td>
                    </tr>
                </tbody>
            </table>
        </div>
    </div>
</template>
