<template>
  <ul>
    <li v-for="(ticket,idx) of ticketlist">
      <ticket-tree :id="idx" :ticket="ticket" @deleteTicket="deleteTicket($event)"></ticket-tree>
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
  methods: {
    deleteTicket (idx) {
      var tid = this.ticketlist[idx]._id
      axios.delete(`http://10.19.226.116:3030/tickets/${tid}`)
      .then(repsonse => {
        console.log('deleteticket success')
        console.log(tid)
        this.ticketlist.splice(idx, 1)
      })
      .catch(e => {
        console.log(e)
      })
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
