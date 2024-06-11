<script setup lang="ts">



</script>

<template>

    <div id="background">
        <div class="grid grid-cols-1 gap-2">
            <div class="row-auto items-center justify-center">
                <h1 class="text-center text-4xl">Turnos en vivo</h1>
            </div>
            <div class="grid grid-cols-2 gap-2">
                <div class="flex flex-col items-center justify-center">
                    <h2 class="mb-2 text-slate-900">Módulo de pago</h2>
                    <table class="table-fixed rounded border border-slate-700">
                        <thead>
                            <tr class="bg-red-700 text-white">
                                <th>Turno</th>
                                <th>Nombre</th>
                            </tr>
                        </thead>
                        <tbody>
                            <tr>
                                <td>Alfreds Futterkiste</td>
                                <td>111</td>
                            </tr>
                            <tr>
                                <td>Maria anderson</td>
                                <td>121</td>
                            </tr>
                        </tbody>
                    </table>
                </div>
                <div class="flex flex-col items-center justify-center">
                    <h2 class="mb-2 text-slate-900">Módulo de PQRS</h2>
                    <table class="table-fixed rounded border border-slate-700">
                        <thead>
                            <tr class="bg-lime-500 text-white">
                                <th>Turno</th>
                                <th>Nombre</th>
                            </tr>
                        </thead>
                        <tbody>
                            <tr>
                                <td>Alfreds Futterkiste</td>
                                <td>Maria Anders</td>
                            </tr>
                            <tr>
                                <td>111</td>
                                <td>121</td>
                            </tr>
                        </tbody>
                    </table>
                </div>
            </div>
            <div class="flex flex-col items-center justify-center">
                <h2 class="mb-2 text-slate-900">Módulo PREFERENCIAL</h2>
                <table class="table-fixed rounded border border-slate-700">
                    <thead>
                        <tr class="bg-purple-700 text-white">
                            <th>Turno</th>
                            <th>Nombre</th>
                        </tr>
                    </thead>
                    <tbody>
                        <tr>
                            <td>Alfreds Futterkiste</td>
                            <td>Maria Anders</td>
                        </tr>
                        <tr>
                            <td>111</td>
                            <td>121</td>
                        </tr>
                    </tbody>
                </table>
            </div>
        </div>

    </div>


</template>


<style scoped>
#background {
    background: #8e9eab;
    background: -webkit-linear-gradient(to right, #eef2f3, #8e9eab);
    background: linear-gradient(to right, #eef2f3, #8e9eab);
}
</style>