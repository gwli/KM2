<template>
   <div>
      <div class="row border border-primary">
        <div class="col-sm-3">
        <button class="btn-primary" type="button"  @click="deleteMe">Delete</button>
        <button class="btn-secondary btn-xs" 
                type="button"
                @click="upvoteTicket(ticket)">
            <span aria-hidden="true" class="glyphicon glyphicon-thumbs-up"></span>
        </button>
           <span class="badge badge-pill badge-primary">{{ ticket.vote }}</span>
        <button class="btn-secondary btn-xs" 
                type="button"
                @click="downvoteTicket(ticket)">
            <span aria-hidden="true" class="glyphicon glyphicon-thumbs-down"></span>
        </button>
           <span class="badge badge-pill badge-primary">{{ ticket.status }}</span>
        </div>
        <div class="d-flex col-sm-8">
          <span class="text-left font-weight-normal"> {{ ticket.title }} </span>
          </p>
        </div>
        <div class="col-sm-1">
        <button  class='btn-secondary btn-xs' @click="changeStatus(ticket)">{{ Action }}</span>
        </button>
        </div>
      </div>
      <div class="row description">
          <vue-markdown class="col-sm-10">{{ ticket.description }}</vue-markdown>
          <div class="input-group mb-3">
             <textarea type="text" class="form-control" v-model="ticket.description">
             </textarea>
          </div>
          <button class="btn-primary" type="button" @click="editTicket(ticket)">Edit</button>
      </div>
      <div class="row tag">
        <div class="col-sm-1">
          <button class="btn-secondary btn-xs" type="button">
            <span aria-hidden="true" class="glyphicon glyphicon-tags"></span>
          </button>
        </div>
        <div class="col-sm-7">
          <vue-markdown class="col-sm-10">{{ ticket.tags }}</vue-markdown>
        </div>
        <div class="col-sm-2">
          <p> Assign: {{ ticket.assgin }} </p>
        </div>
        <div class="col-sm-2">
          <p> Owner: {{ ticket.owner }} </p>
        </div>
      </div>
      <div class="p-3 border border-secondary comments" v-if="answers && answers.length">
           <div class="row" v-for="(answer,idx) of answers">
             <div class="col-sm-4">
               <button class="btn-primary" type="button" @click="deleteAnswer(idx)">Delete</button>
                  <span class="badge badge-pill badge-primary">
                  <span v-if="answer.isbest === 1" aria-hidden="true" class="glyphicon glyphicon-ok"></span>
                  </span>
               <button class="btn-secondary btn-xs" 
                       type="button"
                       @click="upvoteAnswer(answer)">
                   <span aria-hidden="true" class="glyphicon glyphicon-thumbs-up"></span>
               </button>
                  <span class="badge badge-pill badge-primary">{{ answer.vote }}</span>
               <button class="btn-secondary btn-xs"
                       type="button"
                       @click="downvoteAnswer(answer)">
                   <span aria-hidden="true" class="glyphicon glyphicon-thumbs-down"></span>
               </button>
               <button 
                  class="btn-secondary btn-xs" 
                  type="button"
                  @click="setBest(answer)">
                   <span aria-hidden="true" class="glyphicon glyphicon-ok"></span>
               </button>
               </div>
               <div class="col-sm-8">
                 <h3> {{ answer.title }} </h3>
                 <a class="font-weight-normal" :href="answer.url"> {{ answer.abstract }} </a>
                 <vue-markdown> {{ answer.comments }} </vue-markdown>

                 <div class="input-group mb-3">
                    <input type="text" class="form-control" v-model="answer.comments">
                  </div>
                  <button class="btn-primary" type="button" @click="addComments(answer)">Add Comments</button>
               </div>
          </div>
     </div>
   </div>
</template>


<script>
import VueMarkdown from 'vue-markdown'
import axios from 'axios'

export default {
  name: 'ticket',
  data () {
    return {
      answers: [],
      errors_messag: []
    }
  },
  props: {
    ticket: Object,
    id: Number
  },
  computed: {
    Action: function () {
      if (this.ticket.status === 'new') {
        return 'close'
      } else {
        return 'Reopen'
      }
    }
  },
  components: {
    VueMarkdown
  },
  methods: {
    deleteMe () {
      this.$emit('deleteTicket', this.id)
    },
    deleteAnswer (idx) {
      var aid = this.answers[idx]._id
      axios.delete(`http://10.19.226.116:3030/answers/${aid}`)
      .then(repsonse => {
        console.log('delete answer success')
        console.log(aid)
        this.answers.splice(idx, 1)
      })
      .catch(e => {
        console.log(e)
      })
    },
    upvoteTicket (ticket) {
      ticket.vote -= 0
      ticket.vote += 1
      var url = `http://10.19.226.116:3030/tickets/${ticket._id}`
      console.log(url)
      axios.patch(url, {
        vote: ticket.vote
      })
      .then(response => {
        // JSON responses are automatically parsed.
        console.log(`upvote ticket:${ticket._id} ${response}`)
      })
      .catch(e => {
        this.errors_message.push(e)
        console.log(e)
      })
    },
    downvoteTicket (ticket) {
      ticket.vote -= 1
      var url = `http://10.19.226.116:3030/tickets/${ticket._id}`
      console.log(url)
      axios.patch(url, {
        vote: ticket.vote
      })
      .then(response => {
        // JSON responses are automatically parsed.
        console.log(`upvote ticket:${ticket._id} ${response}`)
      })
      .catch(e => {
        this.errors_message.push(e)
        console.log(e)
      })
    },
    upvoteAnswer (answer) {
      answer.vote -= 0
      answer.vote += 1
      var url = `http://10.19.226.116:3030/answers/${answer._id}`
      console.log(url)
      axios.patch(url, {
        vote: answer.vote
      })
      .then(response => {
        // JSON responses are automatically parsed.
        console.log(`upvote answer:${answer._id} ${response}`)
      })
      .catch(e => {
        this.errors_message.push(e)
        console.log(e)
      })
    },
    downvoteAnswer (answer) {
      answer.vote -= 1
      var url = `http://10.19.226.116:3030/answers/${answer._id}`
      console.log(url)
      axios.patch(url, {
        vote: answer.vote
      })
      .then(response => {
        // JSON responses are automatically parsed.
        console.log(`upvote answer:${answer._id} ${response}`)
      })
      .catch(e => {
        this.errors_message.push(e)
        console.log(e)
      })
    },
    changeStatus (ticket) {
      if (ticket.status.toLowerCase() === 'new') {
        ticket.status = 'close'
      } else {
        ticket.status = 'new'
      }
      var url = `http://10.19.226.116:3030/tickets/${ticket._id}`
      console.log(url)
      axios.patch(url, {
        status: ticket.status
      })
      .then(response => {
        // JSON responses are automatically parsed.
        console.log(`set test answser:${ticket._id} ${response}`)
      })
      .catch(e => {
        this.errors_message.push(e)
        console.log(e)
      })
    },
    setBest (answer) {
      answer.isbest = 1
      var url = `http://10.19.226.116:3030/answers/${answer._id}`
      console.log(url)
      axios.patch(url, {
        'isbest': 1
      })
      .then(response => {
        // JSON responses are automatically parsed.
        console.log(`set test answser:${answer._id} ${response}`)
      })
      .catch(e => {
        this.errors_message.push(e)
        console.log(e)
      })
    },
    editTicket (ticket) {
      var url = `http://10.19.226.116:3030/tickets/${ticket._id}`
      console.log(url)
      axios.patch(url, {
        'description': ticket.description
      })
      .then(response => {
        // JSON responses are automatically parsed.
        console.log(`add comments to the answser:${ticket._id} ${response}`)
      })
      .catch(e => {
        this.errors_message.push(e)
        console.log(e)
      })
    },
    addComments (answer) {
      var url = `http://10.19.226.116:3030/answers/${answer._id}`
      console.log(url)
      axios.patch(url, {
        'comments': answer.comments
      })
      .then(response => {
        // JSON responses are automatically parsed.
        console.log(`add comments to the answser:${answer._id} ${response}`)
      })
      .catch(e => {
        this.errors_message.push(e)
        console.log(e)
      })
    },
    getAnswers (tid) {
      var url = `http://10.19.226.116:3030/answers?tid=${tid}`
      console.log(url)
      axios.get(url)
      .then(response => {
        // JSON responses are automatically parsed.
        this.answers = response.data.data
        console.log(`get answsers:${this.answers}`)
        console.log(this.answers)
      })
      .catch(e => {
        this.errors_message.push(e)
        console.log(e)
      })
    }
  },
  created () {
    console.log(this.ticket)
    this.getAnswers(this.ticket._id)
  }
}
</script>
<style>

.badge {
    min-width: 0;
}
</style>