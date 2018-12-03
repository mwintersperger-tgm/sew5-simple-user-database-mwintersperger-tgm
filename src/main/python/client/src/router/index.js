import Vue from 'vue';
import Router from 'vue-router';
import Ping from '@/components/Ping';
import Users from '@/components/Users';

Vue.use(Router);

export default new Router({
  routes: [
    {
      path: '/ping',
      name: 'Ping',
      component: Ping,
    },
    {
      path: '/',
      name: 'Users',
      component: Users,
    },
  ],
  mode: 'history',
});
