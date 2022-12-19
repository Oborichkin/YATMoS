import Vue from 'vue'
import VueRouter from 'vue-router'
import DashboardView from '../views/DashboardView';
import ProjectsView from '../views/ProjectsView';
import RunsView from '../views/RunsView';

Vue.use(VueRouter)

const routes = [
  {
    path: '/',
    name: 'dashboard',
    component: DashboardView
  },
  {
    path: '/projects',
    name: 'projects',
    component: ProjectsView
  },
  {
    path: '/runs',
    name: 'runs',
    component: RunsView
  }
]

const router = new VueRouter({
  routes
})

export default router
