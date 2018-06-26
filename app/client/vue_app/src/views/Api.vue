<template>
    <div class="content">
        <div class="panel">
            <h1>BigRep HMI Demo</h1>
            <button v-if="notConnected" class="btn" @click="connectToPrinter">Connect to printer</button>
            <div v-else>
              <h4>Temperatures</h4>
              <p v-if="elementTemperature">{{elementTemperature | formatTemp}}</p>
              <button class="btn" @click="fetchTemperatureResource('Bed')">Bed</button>
              <button class="btn" @click="fetchTemperatureResource('Extruder0')">T0</button>
              <button class="btn" @click="fetchTemperatureResource('Extruder1')">T1</button>
              <button class="btn" @click="fetchTemperatureResource('Chamber')">Chamber</button>
            </div>
            <p>{{error}}</p>
        </div>
    </div>
</template>

<style scoped>
.btn {
  height: 56px;
  width: 100%
}
.tempbtn {
  width: 50%;
}
</style>

<script>
import $backend from '../backend'

export default {
  name: 'api',
  data () {
    return {
      elementTemperature: undefined,
      error: '',
      notConnected: true
    }
  },
  methods: {
    connectToPrinter () {
      $backend.connectToPrinter()
        .then(responseData => {
          this.showGetTempButtons()
        }).catch(error => {
          this.error = error.message
        })
    },
    fetchTemperatureResource (heatingElement) {
      $backend.fetchTemperatureResource(heatingElement)
        .then(responseData => {
          this.elementTemperature = responseData
        }).catch(error => {
          this.error = error.message
        })
    },
    showGetTempButtons () {
      this.notConnected = false
    }
  }
}
</script>
