import Vue from 'vue'
import App from './App.vue'
import VueRouter from 'vue-router'
import moment from 'moment'
import routes from './routes'

Vue.config.productionTip = false;
Vue.use(VueRouter);
Vue.filter('formatDate', function(value) {
  if (value) {
    return moment(String(value)).format('MM/DD/YYYY hh:mm')
  }
});
const router = new VueRouter({
  routes,
  scrollBehavior() {
    return {x: 0, y: 0}
  }});
new Vue({
  router,
  render: h => h(App)
}).$mount('#app');
