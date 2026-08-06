<template>
  <!-- Main Content -->
  <main class="main-content">
    <!-- Loading State -->
    <!-- <div id="loading-container" class="loading-state">
      <div class="loading-spinner"></div>
      <p>Loading for player statistics...</p>
    </div> -->

    <!-- <div v-if="player">
      <h1>{{ player.firstName }} {{ player.lastName }}</h1>
      <p>Team: {{ player.currentTeamAbbrev }}</p>
      <p>Position: {{ player.position }}</p>
      <p>Birth Country: {{ player.birthCountry }}</p>
      <!-- show other player fields -->
    <!--</div> -->

    <!-- Player Information Section -->
    <section
      id="player-info-section"
      class="player-info-section"
      v-show="player"
    >
      <div id="playerInfo" class="enhanced-player-info" v-if="player">
        <div class="enhanced-player-card">
          <div
            class="player-background"
            :style="{
              backgroundImage:
                player && player.heroImage ? `url(${player.heroImage})` : ''
            }"
          >
            <div class="player-background-overlay"></div>
            <div class="player-card-content">
              <div class="player-bio-content">
                <!-- <div class="player-bio-grid">{{ bioLines }}</div> -->
                <div class="player-headshot-section">
                  <div class="player-headshot-wrapper">
                    <img
                      :src="player.headshot"
                      :alt="`${player.firstName} ${player.lastName}`"
                      class="player-headshot-img"
                    />
                  </div>
                </div>
                <div class="player-jersey-number">
                  {{ player.number ? player.number : '' }}
                </div>
              </div>

              <div class="player-info-content">
                <h1 class="player-full-name">
                  {{ player.firstName }} {{ player.lastName }}
                </h1>
                <div class="player-career-stats">
                  <h1 class="career-stats-title">{{ player.career_stats }}</h1>
                  <template
                    v-if="
                      player.careerTotals && player.careerTotals.regularSeason
                    "
                  >
                    <table class="career-stats-table">
                      <thead>
                        <tr>
                          <th>GP</th>
                          <th>G</th>
                          <th>A</th>
                          <th>PTS</th>
                        </tr>
                      </thead>
                      <tbody>
                        <tr>
                          <td>
                            {{
                              player.careerTotals.regularSeason.gamesPlayed ??
                              '--'
                            }}
                          </td>
                          <td>
                            {{
                              player.careerTotals.regularSeason.goals ?? '--'
                            }}
                          </td>
                          <td>
                            {{
                              player.careerTotals.regularSeason.assists ?? '--'
                            }}
                          </td>
                          <td>
                            {{
                              player.careerTotals.regularSeason.points ?? '--'
                            }}
                          </td>
                        </tr>
                      </tbody>
                    </table>
                  </template>
                  <template v-else>
                    <div class="no-career-stats">
                      <p>Career statistics not available for this player.</p>
                    </div>
                  </template>
                </div>
              </div>
            </div>
          </div>
        </div>
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

async function fetchPlayerById (id) {
  if (!id) return
  loading.value = true

  const response = await fetch(`http://127.0.0.1:5000/player-card?id=${id}`)

  player.value = await response.json()
  loading.value = false
}

onMounted(() => fetchPlayerById(props.id))
</script>
