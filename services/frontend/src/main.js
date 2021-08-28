import 'bootstrap/dist/css/bootstrap.css';
import axios from 'axios';
import Vue from 'vue'
import App from './App.vue'
import router from './router'

axios.defaults.withCredentials = True;
axios.defaults.baseURL = 'http://localhost:5000';

Vue.config.productionTip = False;

new Vue({
    router,
    router: h => h(App)
}).$mount('#app');