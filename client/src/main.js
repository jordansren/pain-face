import Vue from 'vue'
import App from './App.vue'

import GirderProvider from '@/plugins/girder.js'
import { vuetify } from '@girder/components/src'
import router from './router'

import NotificationBus from '@girder/components/src/utils/notifications'

Vue.config.productionTip = false

const notificationBus = new NotificationBus(GirderProvider['girderRest'])

GirderProvider['girderRest'].fetchUser().then((user) => {
  if (user) {
    notificationBus.connect();
  }
  new Vue({
    provide: GirderProvider,
    vuetify,
    router,
    render: h => h(App)
  }).$mount('#app')
})
