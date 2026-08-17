<template>
  <section class="search-section">
    <div class="search-container">
      <div class="search-box-wrapper">
        <input
          v-model="input"
          id="search"
          class="enhaced-search-input"
          @keyup.enter="searchPlayers"
          placeholder="Search players"
        />
        <div class="search-clear" id="search-clear" style="display: none">
          ✕
        </div>
      </div>

      <button @click="searchPlayers">Search</button>

      <div v-if="loading">Loading...</div>

      <div v-for="player in results" :key="player.playerId" class="player">
        <router-link :to="`/player/${player.playerId}`"
          >View {{ player.name }}
        </router-link>
      </div>

      <div v-if="input && !results.length && !loading" class="item error">
        <p>No players found!</p>
      </div>
    </div>
  </section>
</template>

<script setup>
import { ref } from 'vue'
const input = ref('')
const results = ref([])
const loading = ref(false)

async function searchPlayers () {
  if (!input.value.trim()) return

  loading.value = true

  try {
    const response = await fetch(
      `http://127.0.0.1:5000/search?q=${encodeURIComponent(input.value)}`
    )

    const data = await response.json()

    results.value = Array.isArray(data) ? data : data?.data || []
  } catch (error) {
    console.error(error)
    results.value = []
  } finally {
    loading.value = false
  }
}
</script>
