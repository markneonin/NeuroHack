import Vue from 'vue'
import App from './App.vue'
import router from './router'
import store from './store'
import axios from "axios";
import VueAxios from "vue-axios";
import loader from "vue-ui-preloader";


Vue.config.productionTip = true


Vue.use(VueAxios, axios)
Vue.use(loader);

new Vue({
  loader,
  router,
  store,
  axios,
  render: h => h(App)
}).$mount('#app')
