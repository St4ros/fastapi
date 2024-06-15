<script setup lang="ts">

const router = useRouter()


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


        try {
            router.push({ name: 'usuarios-id', params: { id: form.value.id } });

        } catch (error) {
            console.error(error);

        }

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
        <div class="block">
            <label for="id">Identificación:</label>
            <input v-model="form.id" type="text" name="id" id="id" required />
        </div>
        <!-- <button @click="validar">Validar</button> -->
        <div class="block">
            <label for="name">Nombre:</label>
            <input v-model="form.name" type="text" name="name" id="name" />
        </div>
        <div class="block">
            <label for="birth">Fecha de nacimiento:</label>
            <input v-model="form.fecha" type="date" name="birth" id="birth" />
        </div>



        <button class="block" type="submit">Enviar</button>

    </form>
</template>