<script setup lang="ts">
import LiveTurno from '~/components/LiveTurno.vue';
import Swal from 'sweetalert2'

const form = ref({
    fila: '',

})

function atenderTurno() {
    console.log('aqui va el metodo patch para actualizar el estado del turno q llego a true');

}

function showAlert() {
    Swal.fire({ title: " Buen trabajo!", icon: "success" })
}


</script>
<template>
    <h1 class="text-6xl text-center mt-2">Modulo de asesor</h1>
    <div>
        <form @submit.prevent="atenderTurno">
            <div>
                <input type="radio" name="fila" v-model="form.fila" value="pagos" /> Pagos
                <input type="radio" name="fila" v-model="form.fila" value="pqrs" /> PQRS
                <input type="radio" name="fila" v-model="form.fila" value="preferencial" /> Preferencial
            </div>

            <div>
                <LiveTurno></LiveTurno>
            </div>

            <button type="submit" @click="showAlert">Atender</button>

        </form>
        <NuxtLink to="/">Home</NuxtLink>
    </div>
</template>
<style scoped></style>