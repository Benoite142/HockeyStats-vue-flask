<template>
  <div class="bio-grid">
    <div v-if="player.birthDate" class="bio-item">
      <span class="bio-label">Date of birth</span>
      <span class="bio-value">{{ player.birthDate ?? '' }}</span>
    </div>
    <div v-if="player.birthCity" class="bio-item">
      <span class="bio-label">Birth Place</span>
      <span class="bio-value"
        >{{ player.birthCity
        }}{{
          player.birthStateProvince ? ', ' + player.birthStateProvince : ''
        }}, {{ player.birthCountry }}</span
      >
    </div>
    <div v-if="player.heightInInches" class="bio-item">
      <span class="bio-label">Height</span>
      <span class="bio-value">{{ player.heightInInches ?? '' }}</span>
    </div>
    <div v-if="player.weightInPounds" class="bio-item">
      <span class="bio-label">Weight</span>
      <span class="bio-value">{{ player.weightInPounds ?? '' }} lbs</span>
    </div>
    <div v-if="player.shootsCatches" class="bio-item">
      <span class="bio-label">Shoots</span>
      <span class="bio-value">{{ player.shootsCatches ?? '' }}</span>
    </div>
    <div v-if="player.position" class="bio-item">
      <span class="bio-label">Position</span>
      <span class="bio-value">{{ player.position ?? '' }}</span>
    </div>
    <div v-if="player.currentTeamAbbrev" class="bio-item">
      <span class="bio-label">Current Team</span>
      <span class="bio-value">{{ player.currentTeamAbbrev ?? '' }}</span>
    </div>
  </div>
</template>

<script setup>
const props = defineProps({
  player: {
    type: Object,
    required: true
  }
})
</script>
