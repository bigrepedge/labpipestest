<template>
  <div class="content">
    <div class="panel">
      <p>(Not working) Click on the links below to fetch data from the Flask server (probably still works but we have an error in compiled vendor code)</p>
      <p>Random changes to identify branch</p>
      <h4>We had a server call here but it was failing because of a fault in vendor file compilation will look into using another file compiler</h4>
      <p v-for="r in resources" :key="r.timestamp">
        Server Timestamp: {{r.timestamp | formatTimestamp }}
      </p>
      <p>{{error}}</p>
    </div>
  </div>
</template>

<script>

import $backend from '../backend'

export default {
  name: 'about',
  data () {
    return {
      resources: [],
      error: ''
    }
  },
  methods: {
    fetchResource () {
      $backend.fetchResource()
        .then(responseData => {
          this.resources.push(responseData)
        }).catch(error => {
          this.error = error.message
        })
    }
  }
}

</script>
