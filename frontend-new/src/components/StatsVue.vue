<template>
  <table class="stats-table" :id="id || undefined">
    <thead>
      <tr>
        <th>Season</th>
        <th>Team</th>
        <th>League</th>
        <th>GP</th>
        <th>Goals</th>
        <th>Ast</th>
        <th>Pts</th>
        <th>+/-</th>
        <th>PIM</th>
        <th>GWG</th>
        <th>OtG</th>
        <th>PPG</th>
        <th>PPP</th>
        <th>ShG</th>
        <th>ShP</th>
        <th>Shot%</th>
        <th>Shots</th>
        <th>AvgTOI</th>
        <th>FO%</th>
      </tr>
    </thead>
    <tbody>
      <tr v-for="season in stats" :key="season.season">
        <td>{{ formatSeason(season.season) }}</td>
        <td>{{ season.teamName ?? '--' }}</td>
        <td>{{ season.leagueAbbrev ?? '--' }}</td>
        <td>{{ season.gamesPlayed ?? '--' }}</td>
        <td>{{ season.goals ?? '--' }}</td>
        <td>{{ season.assists ?? '--' }}</td>
        <td>{{ season.points ?? '--' }}</td>
        <td>{{ season.plusMinus ?? '--' }}</td>
        <td>{{ season.pim ?? '--' }}</td>
        <td>{{ season.gameWinningGoals ?? '--' }}</td>
        <td>{{ season.otGoals ?? '--' }}</td>
        <td>{{ season.powerPlayGoals ?? '--' }}</td>
        <td>{{ season.powerPlayPoints ?? '--' }}</td>
        <td>{{ season.shorthandedGoals ?? '--' }}</td>
        <td>{{ season.shorthandedPoints ?? '--' }}</td>
        <td>{{ formatPercent(season.shootingPctg) }}</td>
        <td>{{ season.shots ?? '--' }}</td>
        <td>{{ season.avgToi ?? '--' }}</td>
        <td>{{ formatPercent(season.faceoffWinningPctg) }}</td>
      </tr>
    </tbody>
  </table>
</template>

<script setup>
const props = defineProps({
  stats: {
    type: Array,
    default: () => []
  },
  id: {
    type: String,
    default: ''
  }
})

console.log(props.stats)
const formatSeason = value => {
  if (!value) return '--'
  const s = String(value)
  return s.slice(2, 4) + '-' + s.slice(6, 8)
}

const formatPercent = value => {
  if (!value) return '--'
  return parseFloat(value).toFixed(3)
}
</script>
