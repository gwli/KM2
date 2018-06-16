import lazyLoading from './lazyLoading.js'

export default {
  name: 'CreateTicket',
  meta: {
    title: 'CreateTicket',
    iconClass: 'vuestic-icon vuestic-icon-forms'
  },
  path: '/CreateTicket',
  component: lazyLoading('Admin/createTicket')
}
