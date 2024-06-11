<script setup lang="ts">
import { ref } from "vue";

const form = ref({
    id: "",
    name: "",
    fecha: "",
    fila: "",
    estado: false
})

const result = ref("")

const submitForm = async () => {
    result.value = "Espere..."
    try {
        const response = await $fetch('http://localhost:8000/registrar/', {
            method: "POST",
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify(form.value),  // Convert form value to JSON string
        })
        console.log(response);
        result.value = "Formulario enviado con éxito"
    } catch (e) {
        console.error(e);
        result.value = "Error al enviar el formulario"
    } finally {
        setTimeout(() => {
            result.value = ""
        }, 5000)
    }
}
</script>

<template>
    <h1 class="text-6xl text-center mt-2">Formulario de registro para turnos</h1>
    <p class="text-lg text-center mt-1">Si usted ya se ha registrado antes, ingrese su id y presione enter para
        autocompletar sus datos
    </p>
    <form @submit.prevent="submitForm" class="bg-gray-300 shadow-md rounded sm:640px text-center">
        <div class="m-3">
            <label class="block mt-2 text-sm font-medium" for="fila">Seleccione fila segun trámite:</label>
            <br />
            <input type="radio" name="fila" v-model="form.fila" value="pagos" /> Pagos
            <input type="radio" name="fila" v-model="form.fila" value="pqrs" /> PQRS
            <input type="radio" name="fila" v-model="form.fila" value="preferencial" /> Preferencial
        </div>
        <div class="m-3">
            <div class="mb-5"><label class="block mb-2 text-sm font-medium" for="id">Identificacion</label>
                <input class="border-2 border-lime-400 rounded" type="text" id="id" v-model="form.id" />
            </div>
            <div class="mb-5">
                <label class="block mb-2 text-sm font-medium" for="name">Nombre:</label>
                <input class="border-2 border-lime-400 rounded" type="text" id="name" v-model="form.name" />

            </div>
            <div class="mb-5"><label class="block mb-2 text-sm font-medium" for="fecha">Fecha de nacimiento</label>
                <input class="border-2 border-lime-400 rounded" type="date" id="fecha" v-model="form.fecha" />
            </div>

        </div>

        <div v-if="form.id" class="m-3">
            <NuxtLink :to="{ name: 'turnos-id', params: { id: form.id } }">
                <button class="bg-green-600 h-8 w-40 rounded-full" type="submit">Enviar</button>
            </NuxtLink>
        </div>

    </form>
    <NuxtLink to="/">Home</NuxtLink>
</template>

<style scoped></style>
