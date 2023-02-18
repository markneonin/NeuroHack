<template>
  <div class="main-header flex-row-center">
    <div class="logo-group">
      <img src="@/assets/svg/logo.svg">
    </div>
    <div class="breadcrumbs">Прогнозная аналитика эксгаустеров {{ title }}</div>
  </div>
</template>

<script>
export default {
  name: "mainheader",

  props: ['title']
}
</script>

<style scoped>

</style>