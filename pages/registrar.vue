<script setup lang="ts">

const form = ref({
    id: '',
    name: '',
    fecha: '',
    fila: ''
})

const submitForm = async () => {
    try {
        const response = await $fetch('http://localhost:8000/registrar/', {
            method: "POST",
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify(form.value)
        })
        console.log(response);

    } catch (error) {
        console.error(error);

    }
}



</script>

<template>
    <h1>Registro de usuarios</h1>
    <form @submit.prevent="submitForm">
        <label for="row">Seleccione fila</label>
        <select v-model="form.fila" name="row" id="row" required>
            <option value="a">Pagos</option>
            <option value="b">Pqrs</option>
            <option value="c">Preferencial</option>
        </select>
        <label for="id">Identificación:</label>
        <input v-model="form.id" type="text" name="id" id="id" required />
        <!-- <button @click="validar">Validar</button> -->
        <label for="name">Nombre:</label>
        <input v-model="form.name" type="text" name="name" id="name" />
        <label for="birth">Fecha de nacimiento:</label>
        <input v-model="form.fecha" type="date" name="birth" id="birth" />
        <button type="submit">Enviar</button>
    </form>
</template>