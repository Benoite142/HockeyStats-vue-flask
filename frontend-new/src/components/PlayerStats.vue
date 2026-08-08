<template>
  <section id="player-stats-section" class="stats-section">
    <div class="section-header">
      <h2 data-translate="career_stats">Career Statistics</h2>
    </div>

    <div class="stats-section-header">
      <button
        class="nav-button primary active"
        onclick="toggleStats('regular')"
        id="regular-btn"
      >
        Season Stats
      </button>
      <button
        class="nav-button primary"
        onclick="toggleStats('playoffs')"
        id="playoffs-btn"
      >
        Playoffs Stats
      </button>
      <button
        class="nav-button primary"
        onclick="toggleStats('international')"
        id="international-btn"
      >
        International Stats
      </button>
    </div>
    <div class="table-container">
      <div
        v-if="regularSeasonStats.length > 0"
        id="regular-stats"
        class="stats-section"
      >
        <h3 class="seaction-header">Regular Season Statistics</h3>
        <StatsVue :stats="regularSeasonStats" />
      </div>
    </div>
  </section>
</template>

<script setup>
import { computed } from 'vue'
import StatsVue from './StatsVue.vue'

const props = defineProps({
  player: {
    required: true,
    default: null
  }
})

const internationalLeaguesDictionary = {
  OG: 'Olympic Games',
  Olympics: 'Olympic Games',
  '4 Nations': '4 Nations Cup',
  WC: 'World Championship',
  'W-Cup': 'World Cup',
  WCup: 'World Cup',
  'WJC-A': 'World Junior Championship (U20)',
  'WC-A': 'World Championship (Senior)',
  'WJ18-A': 'World U18 Championship',
  International: 'International',
  'WJC-20': 'World Junior Championship (U20)',
  'WJC-18': 'World U18 Championship',
  'WHC-17': 'World Hockey Challenge (U17)'
}

const playerData = computed(() => props.player ?? {})
const seasonTotals = computed(() => playerData.value?.seasonTotals ?? [])

console.log(playerData.value)
const playoffsStats = computed(() =>
  seasonTotals.value.filter(season => season.gameTypeId === 3)
)

const internationalStats = computed(() =>
  seasonTotals.value.filter(
    season =>
      season.leagueAbbrev && internationalLeaguesDictionary[season.leagueAbbrev]
  )
)

const regularSeasonStats = computed(() =>
  seasonTotals.value.filter(
    season =>
      season.gameTypeId === 2 &&
      (!season.leagueAbbrev ||
        !internationalLeaguesDictionary[season.leagueAbbrev])
  )
)

// console.log(regularSeasonStats.value)
</script>
