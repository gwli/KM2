import lazyLoading from './lazyLoading.js'

export default {
  name: 'AddSubTicket',
  meta: {
    title: 'AddSubTicket',
    iconClass: 'vuestic-icon vuestic-icon-forms'
  },
  path: '/AddSubTicket',
  component: lazyLoading('Admin/addSubTicket')
}
