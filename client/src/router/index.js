import Vue from 'vue';
import Router from 'vue-router';

import home from '../components/home.vue';
import upload from '../components/upload.vue';
import requestPassword from '../components/requestPassword.vue';
import result from '../components/result.vue';

Vue.use(Router);

export default new Router({
  routes: [
    {
      path: '/',
      name: 'Home',
      component: home,
    },
    {
      path: '/upload',
      name: 'Upload',
      component: upload,
    },
    {
      path: '/password-reset',
      name: 'Reset',
      component: requestPassword,
    },
    {
      path: '/result',
      name: 'Result',
      component: result,
      props: true,
    },
  ],
});
