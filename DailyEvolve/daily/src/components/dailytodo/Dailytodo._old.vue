<template>
  <div class="card">
    <div class="card-header">
      <div class="row">
        <div class="col-sm-7">
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
        <div class="col-sm-3">
        <button  class='btn-secondary btn-xs' @click="changeStatus(ticket)">{{ Action }}</span>
        </button>
        <button class="btn-secondary" type="button" @click="editTicket(ticket)">Edit</button>
        </div>
      </div>
    </div>
    <div class="card-body">
        <h5 class="card-title">  {{ ticket.title }} </h5>
        <div>
          <slider v-model="value" range></slider>
        </div>
        <Button type="primary" @click="modal1 = true">Display dialog box</Button>
        <Modal
            v-model="modal1"
            title="Common Modal dialog box title"
            @on-ok="ok"
            @on-cancel="cancel">
            <p>Content of dialog</p>
            <p>Content of dialog</p>
            <p>Content of dialog</p>
        </Modal>


        <div class="row description">
          <div class="cl-sm-12">
            <div>
              <vue-markdown> {{ ticket.description }}</vue-markdown>
            </div>
          </div>
        </div>
        <div class="row tag">
          <div class="col-sm-1">
            <button class="btn-secondary btn-xs" type="button">
              <span aria-hidden="true" class="glyphicon glyphicon-tags"></span>
            </button>
          </div>
          <div class="col-sm-7">
            {{ ticket.tags }}
          </div>
          <div class="col-sm-2">
            <p> Assign: {{ ticket.assgin }} </p>
          </div>
          <div class="col-sm-2">
            <p> Owner: {{ ticket.owner }} </p>
          </div>
        </div>
        <hr>
        <button class="btn-secondary" @click="showLargeModal()">
          {{'modal.large' | translate }}
        </button>
        <button class="btn-secondary" type="button">Add sub ticket</button>
        <vuestic-modal 
              :show.sync="show" 
              v-bind:large="false" 
              ref="largeModal" 
              :okText="'modal.confirm' | translate"
              :cancelText="'modal.cancel' | translate">
            
              <div slot="title">subticket </div>
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
              <div slot="footer">
                  <div class="form-group">
                      <button type="submit" class=" btn-success">submit</button>
                  </div>

              </div>
        </vuestic-modal>
        <router-link :to="{name: 'CreateTicket', params:{parentId:ticket._id}}">Add sub ticket</router-link>
        <div class="row children">
          <ul>
            <li v-for="ele of ticket.children"> {{ ele}} </li>
          </ul>
        </div>
        <hr>
      </div>
      <div class="p-3 border border-secondary comments" v-if="answers && answers.length">
          <div class="row" v-for="(answer,idx) of answers">
            <div class="col-sm-4">
              <button class="btn-primary" type="button" @click="deleteAnswer(idx)">Del</button>
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
    <div class="card-footer">
      <a href="#" class="card-link">Card Link </a>
      <a href="#" class="card-link">another link</a>
    </div>
  </div>
</template>

<script>
  import axios from 'axios'
  import CreateTicket from '../Admin/createTicket'
  import VueMarkdown from 'vue-markdown'

  export default {
    data () {
      return {
        modal1: false,
        show: true,
        modalShow: false,
        posts: [],
        tags: '',
        assign: '',
        title: '',
        description: '',
        ticket: Object,
        answers: [],
        errors_message: [],
        value: [20, 50]
      }
    },
    components: {
      VueMarkdown,
      CreateTicket
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
    methods: {
      ok () {
        this.$Message.info('Clicked ok')
      },
      cancel () {
        this.$Message.info('Clicked cancel')
      },
      showLargeModal () {
        this.$refs.largeModal.open()
      },
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
      },
      submitTicket (ticket) {
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
    // Fetches posts when the component is created.
    created () {
      axios.get(`http://10.19.226.116:3030/tickets`)
      .then(response => {
        // JSON responses are automatically parsed.
        this.posts = response.data.data
        this.ticket = this.posts[1]
        console.log(this.posts)
        console.log('ticket status', this.ticket)
        this.getAnswers(this.ticket._id)
      })
      .catch(e => {
        this.errors_message.push(e)
        console.log(e)
      })
    }
  }
</script>
<style lang="scss">

.badge {
    min-width: 0;
}

</style>
