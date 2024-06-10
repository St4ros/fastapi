<script setup lang="ts"></script>
<template>
    <div class="container mx-auto my-auto px-4 flex flex-col">
        <h1 class="text-center text-6xl font-extrabold">
            <span class="bg-gradient-to-r from-green-400 to-blue-500 bg-clip-text text-transparent"> Bienvenido a la
                página principal </span>
        </h1>


        <div>
            <NuxtLink to="/registro">Registrarse y tomar turno</NuxtLink>
        </div>
        <div>
            <NuxtLink to="/atencion">Ser un asesor</NuxtLink>
        </div>
        <div>
            <NuxtLink to="/tablas">Ver turnos en vivo</NuxtLink>
        </div>


    </div>
</template>
<style></style>