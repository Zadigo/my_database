
const routes = [
  {
    path: '/',
    component: () => import('layouts/MainLayout.vue'),
    children: [
      { path: '', redirect: '/app' },
      { path: '/app', component: () => import('pages/creation/HomePage.vue'), name: 'home' },
      { path: '/connections', component: () => import('pages/creation/ConnectionsPage.vue'), name: 'connections' },
      { path: '/slide/:id(sl_[a-zA-Z0-9]+)', component: () => import('pages/creation/SlidePage.vue'), name: 'slide' }
    ]
  },

  {
    path: '/view',
    component: () => import('layouts/UserLayout.vue'),
    children: [
      {
        path: 'slides/:id(sl_[a-zA-Z0-9]+)',
        component: () => import('pages/visualization/SlideViewPage.vue'),
        name: 'slide_visualization'
      }
    ]
  },


  // Always leave this as last one,
  // but you can also remove it
  {
    path: '/:catchAll(.*)*',
    component: () => import('pages/ErrorNotFound.vue')
  }
]

export default routes
