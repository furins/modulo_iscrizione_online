
const routes = [
  {
    path: '/',
    component: () => import('layouts/MainLayout.vue'),
    children: [
      { path: 'confirmation_ok/', component: () => import('pages/iscrizione_ok.vue') },
      { path: 'confirmation_error/', component: () => import('pages/iscrizione_error.vue') },
      { path: ':evento/', component: () => import('pages/iscrizione.vue') },
      { path: '', component: () => import('pages/Index.vue') }

    ]
  },

  // Always leave this as last one,
  // but you can also remove it
  {
    path: '*',
    component: () => import('pages/Error404.vue')
  }
]

export default routes
