<template>
  <div class="card">
    <div class="card-header">
      <div class="row">
        <div class="col-sm-4">
        <button class="btn-secondary" type="button"  @click="deleteMe">Del</button>
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
        </div>
      </div>
    </div>
    <div class="card-body">
        <h5 class="card-title">  {{ ticket.title }} </h5>
        <hr>
        <div class="row description">
          <div class="col-sm-10">
            <vue-markdown :source="ticket.description"></vue-markdown>
          </div> 
        </div>
        <hr>
        <div class="row tag">
          <div class="col-sm-1">
            <button class="btn-secondary btn-xs" type="button">
              <span aria-hidden="true" class="glyphicon glyphicon-tags"></span>
            </button>
          </div>
            <div class="col-sm-11">
              {{ ticket.tags }}
            </div>
        </div>
        <div class="row status">
          <div class="col-sm-6">
            <p> Assign: {{ ticket.assign }} </p>
          </div>
          <div class="col-sm-6">
            <p> Owner: {{ ticket.owner }} </p>
          </div>
        </div>
        <hr>
        <Modal
            v-model="editModal"
            title=""
            @on-ok="editTicket(ticket)"
            @on-cancel="cancel">
          <Form :model="formItem" :label-width="80" @submit.native.prevent="submit">
              <FormItem label="Title">
                  <Input v-model="ticket.title" placeholder="Enter something..."></Input>
              </FormItem>
              <FormItem label="Description">
                  <Input v-model="ticket.description" type="textarea" :autosize="{minRows: 5,maxRows: 10}" placeholder="Enter something..."></Input>
              </FormItem>
              <FormItem label="Assign">
                  <Row>
                      <Col span="8">
                          <Select v-model="ticket.assign">
                              <Option value="lgw">lgw</Option>
                              <Option value="zgg">zgg</Option>
                              <Option value="googler">googler</Option>
                          </Select>
                      </Col>
                      <Col span="6" style="text-align: center">Owner</Col>
                      <Col span="8">
                          <Select v-model="ticket.owner">
                              <Option value="lgw">lgw</Option>
                              <Option value="zgg">zgg</Option>
                              <Option value="googler">googler</Option>
                          </Select>
                      </Col>
                  </Row>
              </FormItem>
              <FormItem label="Tags">
                  <Input v-model="ticket.tags" placeholder="Enter something..."></Input>
              </FormItem>
              <FormItem label="DueDate">
                  <Row>
                      <Col span="11">
                          <DatePicker type="date" placeholder="Select date" v-model="ticket.dueDate"></DatePicker>
                      </Col>
                      <Col span="2" style="text-align: center">-</Col>
                      <Col span="11">
                          <TimePicker type="time" placeholder="Select time"></TimePicker>
                      </Col>
                  </Row>
              </FormItem>
          </Form>
        </Modal>
        <Button type="primary" @click="editModal = true">Edit</Button>
        <router-link  :to="{name:'AddSubTicket', params:{parentTicket:ticket}}" tag="button">add Sub Ticket</router-link>
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
  import AddSubTicket from '../Admin/addSubTicket'
  import VueMarkdown from 'vue-markdown'

  export default {
    name: 'ticketTree',
    props: {
      ticket: Object,
      id: Number
    },
    data () {
      return {
        formItem: {},
        editModal: false,
        modalShow: false,
        posts: [],
        assign: '',
        answers: [],
        errors_message: [],
      }
    },
    components: {
      VueMarkdown,
      CreateTicket,
      AddSubTicket
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
      editTicket (ticket) {
        this.$Message.info('Clicked ok')
        var url = `http://10.19.226.116:3030/tickets/${ticket._id}`
        console.log(url)
        axios.patch(url, ticket)
        .then(response => {
          // JSON responses are automatically parsed.
          console.log(`upvote ticket:${ticket._id} ${response}`)
        })
        .catch(e => {
          this.errors_message.push(e)
          console.log(e)
        })
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
      console.log('ticket status', this.ticket)
      this.getAnswers(this.ticket._id)
    }
  }
</script>
<style lang="scss">

.badge {
    min-width: 0;
}

</style>
