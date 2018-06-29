import Vue from 'vue'
import '@/filters.js'

describe('filters.js', () => {
  describe('', () => {
    let formatTemp = Vue.filter('formatTemp')
    it('format temperature should return correct string if it recieves an object with (name, target, actual)', () => {
      let data = {heating_element: 'test', target_temp: '0', actual_temp: '0'}
      expect(formatTemp(data)).toBe('test:  Target 0 Actual 0')
    })
  })
})
