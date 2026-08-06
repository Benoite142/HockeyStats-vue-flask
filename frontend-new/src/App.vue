<script setup>
import { RouterView } from 'vue-router'
import Header from './components/Header.vue'
</script>

<template>
  <body class="search-page">
    <Header />
    <main class="main-content">
      <RouterView />
    </main>
  </body>
</template>
