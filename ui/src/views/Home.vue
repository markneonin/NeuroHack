<template>
  <div class="home">

  </div>
</template>


<script>
import axios from "axios";

export default {
  title: 'Академия будущего',
  description: 'Академия будущего',
  name: 'Home',
  components: {
  },

  mixins: [],

  data() {
    return {
    }
  },

  created() {
    // this.loadExgausters()
    console.log(this.$store.getters.getServerUrl)
  },

  methods: {
    async loadExgausters() {
      await axios
          .get(`${this.$store.getters.getServerUrl}/exgausters/`)
          .then(response => (this.exgausters = response.data));
    },
  },
}
</script>


<style scoped>

.news-block {
  border: none;
  border-radius: 10px;
  text-align: center;
}

.news-block-text {
  text-align: left;
}

.welcome-block {
  padding: 30px;
}

.welcome-block img {
  height: 60px;
  margin-bottom: 40px;
}
</style>