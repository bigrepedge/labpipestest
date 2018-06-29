import { shallowMount } from '@vue/test-utils'
import HelpLinks from '@/components/HelpLinks.vue'

describe('HelpLinks.vue', () => {
  let msg
  let wrapper
  beforeEach(() => {
    msg = 'new message'
    wrapper = shallowMount(HelpLinks, {
      propsData: { msg }
    })
  })
  it('renders props.msg when passed', () => {
    expect(wrapper.text()).toMatch(msg)
  })
  it('Both MessageList and Message are vue instances', () => {
    expect(wrapper.isVueInstance()).toBe(true)
    expect(wrapper.find('.hello').element).toBeInstanceOf(HTMLElement)
  })
})
