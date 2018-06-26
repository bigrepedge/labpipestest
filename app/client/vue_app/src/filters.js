// Vue.js Filters
// https://vuejs.org/v2/guide/filters.html

import Vue from 'vue'

let filters = {
  formatTimes (data) {
    let datetime = new Date(data)
    return datetime.toLocaleTimeString('en-US')
  },
  formatTimestamp (data) {
    let datetime = new Date(data)
    return datetime.toLocaleTimeString('en-US')
  },
  formatTemp (data) {
    let temperatureStringFormated = data.heating_element.concat(
      ': ',
      ' Target ',
      data.target_temp,
      ' Actual ',
      parseInt(data.actual_temp)
    )

    return temperatureStringFormated
  }
}

// Register All Filters on import
Object.keys(filters).forEach(function (filterName) {
  Vue.filter(filterName, filters[filterName])
})
