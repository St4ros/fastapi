<template>
    <div class="flex min-h-screen items-center justify-center bg-gray-900">
      <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-5">
        <div class="group relative items-center justify-center overflow-hidden cursor-pointer hover:shadow-x1 hover:shadow-black/30 transition-shadow">
          <div class="h-96 w-72">
            <img class="h-full w-full object-cover group-hover:rotate-3 group-hover:scale-125 transition-transform" src="/pages/img/principal.jpg">
          </div>
          <div class="absolute inset-0 bg-gradient-to-b from-transparent via-transparent to-black group-hover:from-black/70 group-hover:via-black/60 group-hover:to-black/70"></div>
          <div class="absolute inset-0 flex flex-col items-center justify-center px-9 text-center translate-y-[60%] group-hover:translate-y-0 transition-all">
              <NuxtLink to="/registrar">
                <h1 class="reg">REGISTRAR</h1>
              </NuxtLink>
          </div>
        </div>
        <div class="group relative items-center justify-center overflow-hidden cursor-pointer hover:shadow-x1 hover:shadow-black/30 transition-shadow">
          <div class="h-96 w-72">
            <img class="h-full w-full object-cover group-hover:rotate-3 group-hover:scale-125 transition-transform" src="/pages/img/asesor.jpg">
          </div>
          <div class="absolute inset-0 bg-gradient-to-b from-transparent via-transparent to-black group-hover:from-black/70 group-hover:via-black/60 group-hover:to-black/70"></div>
          <div class="absolute inset-0 flex flex-col items-center justify-center px-9 text-center translate-y-[60%] group-hover:translate-y-0 transition-all">
              <NuxtLink to="/asesor">
                <h1 class="reg">ASESOR</h1>
              </NuxtLink>
          </div>
        </div>
        <div class="group relative items-center justify-center overflow-hidden cursor-pointer hover:shadow-x1 hover:shadow-black/30 transition-shadow">
          <div class="h-96 w-72">
            <img class="h-full w-full object-cover group-hover:rotate-3 group-hover:scale-125 transition-transform" src="/pages/img/turno.jpg">
          </div>
          <div class="absolute inset-0 bg-gradient-to-b from-transparent via-transparent to-black group-hover:from-black/70 group-hover:via-black/60 group-hover:to-black/70"></div>
          <div class="absolute inset-0 flex flex-col items-center justify-center px-9 text-center translate-y-[60%] group-hover:translate-y-0 transition-all">
              <NuxtLink to="/verturnos">
                <h1 class="reg">TURNOS</h1>
              </NuxtLink>
          </div>
        </div>
      </div>
      <NuxtPage></NuxtPage>
    </div>
  </template>
  
  <style scoped>
  @import url('https://fonts.googleapis.com/css2?family=Oswald:wght@200..700&display=swap');
  
  .reg {
    font-family: 'Oswald', sans-serif;
    font-size: 2.5rem; /* Ajusta el tamaño según tus necesidades */
    font-weight: bold;
    color: white;
  }
  </style>
  
  