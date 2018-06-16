import lazyLoading from './lazyLoading.js'

export default {
  name: 'DailySearch',
  meta: {
    title: 'DailyDailySearch',
    iconClass: 'vuestic-icon vuestic-icon-forms'
  },
  path: '/dailysearch',
  component: lazyLoading('dailysearch/Dailysearch')
}
