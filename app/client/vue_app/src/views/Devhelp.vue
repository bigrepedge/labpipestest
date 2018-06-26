<template>
  <div class="content">
    <div class="panel">
        <HelpLinks msg="This is a list of some useful links"/>
    </div>
  </div>
</template>

<script>
// @ is an alias to /src
import HelpLinks from '@/components/HelpLinks.vue'

export default {
  name: 'DevHelp',
  components: {
    HelpLinks
  }
}
</script>
