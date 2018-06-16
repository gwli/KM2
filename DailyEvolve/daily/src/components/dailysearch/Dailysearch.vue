<template>
  <ul>
    <li v-for="ticket of ticketlist">
      <ticket-tree :ticket="ticket"></ticket-tree>
    </li>
  </ul>
</template>

<script>
import ticketTree from './ticketTree'
import axios from 'axios'

export default {
  props: {
    treeData: Object
  },
  data () {
    return {
      ticketlist: Object
    }
  },
  components: {
    ticketTree
  },
  created () {
    axios.get(`http://10.19.226.116:3030/tickets`)
    .then(response => {
      // JSON responses are automatically parsed.
      this.ticketlist = response.data.data
      console.log(this.ticketlist)
    })
    .catch(e => {
      this.errors_message.push(e)
      console.log(e)
    })
  }
}
</script>
<style lang="scss">

.tree-list ul {
  padding-left: 16px;
  margin: 6px 0;
}
</style>
