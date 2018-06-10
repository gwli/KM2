import lazyLoading from './lazyLoading.js'

export default {
  name: 'Dailytodo',
  meta: {
    title: 'Dailytodo',
    iconClass: 'vuestic-icon vuestic-icon-forms'
  },
  path: '/dailytodo',
  component: lazyLoading('dailytodo/Dailytodo')
}
