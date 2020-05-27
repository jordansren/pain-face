import Vue from 'vue'
import App from './App.vue'
import GirderProvider from '@/plugins/girder.js';
import { vuetify } from '@girder/components/src';

Vue.config.productionTip = false

new Vue({
  provide: GirderProvider,
  vuetify,
  render: h => h(App)
}).$mount('#app')
