<script setup lang="ts">
import { ref } from "vue";

const form = ref({
    id: "",  // Assuming id is required by the backend
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
    <form @submit.prevent="submitForm">
        <div>
            <input type="radio" name="fila" v-model="form.fila" value="a" /> Pagos
            <input type="radio" name="fila" v-model="form.fila" value="b" /> PQRS
            <input type="radio" name="fila" v-model="form.fila" value="c" /> Preferencial
        </div>

        <input type="text" id="name" v-model="form.name" placeholder="Nombre" />
        <input type="text" id="id" v-model="form.id" placeholder="Identificación" />
        <input type="date" id="fecha" v-model="form.fecha" placeholder="Fecha" />

        <button type="submit">Enviar</button>
        <div>{{ result }}</div>
    </form>
</template>

<style scoped></style>
