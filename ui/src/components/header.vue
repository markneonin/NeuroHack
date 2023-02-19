<template>
  <div class="main-header flex-row-center">
    <div class="logo-group">
      <img src="@/assets/svg/logo.svg">
    </div>
    <div class="breadcrumbs"><a class="nav_link" href="/">Прогнозная аналитика эксгаустеров</a> {{ title }}</div>
  </div>
</template>

<script>
export default {
  name: "mainHeader",

  props: ['title']
}
</script>

<style scoped>
.nav_link {
  color: #000000;
  text-decoration: none;
}
</style>