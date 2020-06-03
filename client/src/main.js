import Vue from 'vue';

import GirderProvider from '@/plugins/girder';
import { vuetify } from '@girder/components/src';
import NotificationBus from '@girder/components/src/utils/notifications';
import router from './router';

import App from './App.vue';

Vue.config.productionTip = false;

const notificationBus = new NotificationBus(GirderProvider.girderRest);

GirderProvider.girderRest.fetchUser().then((user) => {
  if (user) {
    notificationBus.connect();
  }
  new Vue({
    provide: GirderProvider,
    vuetify,
    router,
    render: (h) => h(App),
  }).$mount('#app');
});
