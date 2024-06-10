<script setup lang="ts"></script>
<template>
    <h1>Modulo de asesor</h1>
    <div>
        <form>
            <div>
                Seleccione su modulo
            </div>

            <div>
                Renderizado del primer turno q fue agendado y q este en espera para la fila seleccionada
            </div>
            el boton al darle atender cambia el estado del turno q le llego a true y a su vez refresca el componente del
            renderizado de arriba
            <button>Atender</button>
            <div>Mostrar alerta que diga atendido con éxito</div>
        </form>
        <NuxtLink to="/">Home</NuxtLink>
    </div>
</template>
<style scoped></style>