import lazyLoading from './lazyLoading.js'

export default {
  name: 'NewTicket',
  meta: {
    title: 'NewTicket',
    iconClass: 'vuestic-icon vuestic-icon-forms'
  },
  path: '/NewTicket',
  component: lazyLoading('Admin/newTicket')
}
