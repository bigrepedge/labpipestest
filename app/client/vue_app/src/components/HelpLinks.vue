<template>
  <div class="hello">
    <h1>{{ msg }}</h1>
    <p>
      For guide about the vue software stack take a look here.
      <a href="https://github.com/vuejs/vue-cli/tree/dev/docs" target="_blank">vue-cli documentation</a>
    </p>
    <h3>Installed CLI Plugins</h3>
    <ul>
      <li><a href="https://github.com/vuejs/vue-cli/tree/dev/packages/%40vue/cli-plugin-babel" target="_blank">babel</a></li>
      <li><a href="https://github.com/vuejs/vue-cli/tree/dev/packages/%40vue/cli-plugin-eslint" target="_blank">eslint</a></li>
    </ul>
    <h3>More Links</h3>
    <ul>
      <li><a href="https://vuejs.org" target="_blank">Vuejs</a></li>
    </ul>
    <h3>plugins</h3>
    <ul>
      <li><a href="https://router.vuejs.org/en/essentials/getting-started.html" target="_blank">vue-router</a></li>
      <li><a href="https://vuex.vuejs.org/en/intro.html" target="_blank">vuex</a></li>
      <li><a href="https://github.com/vuejs/vue-devtools#vue-devtools" target="_blank">vue-devtools</a></li>
      <li><a href="https://vue-loader.vuejs.org/en" target="_blank">vue-loader</a></li>
      <li><a href="https://github.com/vuejs/awesome-vue" target="_blank">awesome-vue</a></li>
    </ul>
    <h3>Testing plugins</h3>
    <ul>
      <li><a href="https://pytest-cov.readthedocs.io/en/latest/" target="_blank">pytest</a></li>
      <li><a href="https://docs.cypress.io/guides/overview/why-cypress.html#" target="_blank">cypress</a></li>
      <li><a href="https://facebook.github.io/jest/" target="_blank">jest</a></li>
    </ul>
  </div>
</template>

<script>
export default {
  name: 'HelpLinks',
  props: {
    msg: String
  }
}
</script>
