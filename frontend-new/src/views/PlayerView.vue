<template>
  <!-- Main Content -->
  <main class="main-content">
    <!-- Loading State -->
    <div id="loading-container" class="loading-state">
      <div class="loading-spinner"></div>
      <p>Loading for player statistics...</p>
    </div>

    <div v-if="player">
      <h1>{{ player.firstName }} {{ player.lastName }}</h1>
      <p>Team: {{ player.currentTeamAbbrev }}</p>
      <p>Position: {{ player.position }}</p>
      <!-- show other player fields -->
    </div>

    <!-- Player Information Section -->
    <section
      id="player-info-section"
      class="player-info-section"
      style="display: none"
    >
      <div id="playerInfo" class="enhanced-player-info">
        <!-- Content will be populated by JavaScript -->
      </div>
    </section>

    <!-- Player Statistics Section -->
    <section
      id="player-stats-section"
      class="stats-section"
      style="display: none"
    >
      <div class="section-header">
        <h2>Career Statistics</h2>
      </div>
      <div id="player-stats" class="enhanced-stats-container"></div>
    </section>
  </main>
</template>

<script setup>
import { onMounted, ref } from 'vue'

const props = defineProps({
  id: String
})

const player = ref(null)
const loading = ref(false)

async function getPlayer () {
  if (!props.id) return
  loading.value = true

  const response = await fetch(
    `http://127.0.0.1:5000/player-card?id=${props.id}`
  )

  player.value = await response.json()
  loading.value = false
}

onMounted(getPlayer)
</script>
