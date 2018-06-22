<template>
  <div>
      <div class="row input-group mb-3">
          <div class="input-group-prepend">
              <span> Title</span>
          </div>
          <input class="form-control" type="text" placeholder="ticket title" v-model="title">
      </div>
      <form @submit.prevent="submit">
          <label for="description">Description:</label>
          <div class="form-group">
              <textarea class="form-control" rows="5" id="description" v-model="description"></textarea>
              <vue-markdown> {{ description }} </vue-markdown>
          </div>

          <div class="row input-group mb-3">
              <div class="input-group-prepend">
                  <span> Tags</span>
              </div>
              <input class="form-control" type="text" placeholder="ticket tags" v-model="tags">
          </div>
          <div class="row input-group mb-3">
              <div class="input-group-prepend">
                  <span> Assign</span>
              </div>
              <input class="form-control" type="text" placeholder="googler" v-model="assign">
          </div>
          <div class="form-group">
              <button type="submit" class=" btn-success">submit</button>
          </div>
      </form>
      <p>  {{ message }} </p>
  </div>
</template>


<script>
import VueMarkdown from 'vue-markdown'
import axios from 'axios'

export default {
  name: 'createTicket',
  props: {
    parentId: '',
    ticket: Object
  },
  data () {
    return {
      title: [],
      tags: [],
      assign: '',
      description: null,
      message: 'place holder'
    }
  },
  methods: {
    updateParentTicket (childId) {
      console.log('parentId', this.ticket._id, 'children', this.ticket.children, 'new_child', childId)
      var url = `http://10.19.226.116:3030/tickets/${this.ticket._id}`
      var subTicketList = this.ticket.children
      subTicketList.push(childId)
      console.log(subTicketList)
      axios.patch(url, {
        'children': subTicketList
      })
      .then(response => {
        // JSON responses are automatically parsed.
        console.log(`add sub ticket to the ticket:${this.ticket._id} ${response}`)
      })
      .catch(e => {
        this.errors_message.push(e)
        console.log(e)
      })
    },
    submit () {
      var updateParentTicket = this.updateParentTicket
      var currDate = new Date()
      var parentId = this.parentId
      axios.post('http://10.19.226.116:3030/tickets', {
        status: 'new',
        tags: this.tags,
        title: this.title,
        description: this.description,
        owner: 'lgw',
        vote: 0,
        assign: this.assign,
        spendEffort: 0,
        estimateEffort: 0,
        due_date: '',
        children: [],
        parent: this.parentId,
        created: currDate.toJSON()
      }).then(function (response) {
        console.log('created new ticket', response)
        var newTicket = response.data
        if (parentId !== '') {
        // if (newTicket) {
          console.log('update the parent ticket')
          updateParentTicket(newTicket._id)
        }
      })
      .catch(e => {
        console.log(e)
      })
    }
  },
  components: {
    VueMarkdown
  },
  created () {
    if (this.$route.params.parentId) {
      this.parentId = this.$route.params.parentId
      var url = `http://10.19.226.116:3030/tickets?_id=${this.parentId}`
      console.log(url)
      axios.get(url)
      .then(response => {
        // JSON responses are automatically parsed.
        this.ticket = response.data.data[0]
        console.log(`get answsers:${this.ticket}`)
        console.log(this.ticket)
      })
      .catch(e => {
        console.log(e)
      })
    }
  }
}
</script>
<style>

.badge {
    min-width: 0;
}

</style>