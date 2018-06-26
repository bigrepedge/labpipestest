<template>
  <div id="app">
    <div id="navbar">
      <div class="brand"></div>
      <div class="main-menu">
        <router-link to="/devhelp">Dev Helpful Links</router-link>
        <router-link to="/">Demo</router-link>
      </div>
    </div>
    <router-view/>
  </div>
</template>

<style>
    @import './assets/css/main.scss';
</style>
