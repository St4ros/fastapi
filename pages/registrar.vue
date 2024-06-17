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
<div class="flex items-center justify-center min-h-screen bg-gray-900">
  <div class="flex flex-col cuadro bg-gray-800 p-8 rounded-lg shadow-lg">
    <div class="flex items-center justify-between mb-8">
      <!-- Columna izquierda para el formulario -->
      <div class="w-1/2 pr-4">
        <h1 class="text-4xl text-white font-bold mb-4">Registro de usuarios</h1>
        <form @submit.prevent="submitForm" class="w-full">
          <div class="mb-4">
            <label for="row" class="block text-gray-300 mb-2">Seleccione fila</label>
            <select v-model="form.fila" name="row" id="row" class="w-full px-4 py-2 bg-gray-700 text-white rounded-lg" required>
              <option value="a">Pagos</option>
              <option value="b">Pqrs</option>
              <option value="c">Preferencial</option>
            </select>
          </div>
          <div class="mb-4">
            <label for="id" class="block text-gray-300 mb-2">Identificación</label>
            <input v-model="form.id" type="text" name="id" id="id" class="w-full px-4 py-2 bg-gray-700 text-white rounded-lg" required />
          </div>
          <div class="mb-4">
            <label for="name" class="block text-gray-300 mb-2">Nombre</label>
            <input v-model="form.name" type="text" name="name" id="name" class="w-full px-4 py-2 bg-gray-700 text-white rounded-lg" />
          </div>
          <div class="mb-4">
            <label for="birth" class="block text-gray-300 mb-2">Fecha de nacimiento</label>
            <input v-model="form.fecha" type="date" name="birth" id="birth" class="w-full px-4 py-2 bg-gray-700 text-white rounded-lg" />
          </div>
          <button class="w-full py-2 bg-orange-500 text-white font-semibold rounded-lg mt-4" type="submit">Enviar</button>
        </form>
      </div>

      <!-- Columna derecha para la imagen -->
      <div class="w-1/2 pl-4">
          <div class="w-full mb-4">
            <img src="/pages/img/registrar.jpg" alt="Imagen" class="w-full h-auto md:h-64 lg:h-96 xl:h-128 rounded-lg">
          </div>
          <p class="mensaje text-gray-300">¡Por favor registra tus datos!</p>
          </div>
          
          </div>
            <NuxtLink to="/" class="fixed bottom-5 left-5">
              <i class="bi bi-house-fill text-white" style="font-size: 2rem;"></i>
            </NuxtLink>
    </div>
</div>
</template>

<style>
.cuadro{
  max-width: 900px;
}
.mensaje{
  text-align:center;
}
</style>