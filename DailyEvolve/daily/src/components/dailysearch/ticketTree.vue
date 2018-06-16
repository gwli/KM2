<template>
   <div>
       <div  v-for="post of posts">
            <div class="row border border-primary">
                <div class="col-sm-2">
                <button class="btn-secondary btn-xs" type="button">
                    <span aria-hidden="true" class="glyphicon glyphicon-thumbs-up"></span>
                </button>
                   <span class="badge badge-pill badge-primary">{{ post.Weight }}</span>
                <button class="btn-secondary btn-xs" type="button">
                    <span aria-hidden="true" class="glyphicon glyphicon-thumbs-down"></span>
                </button>
                   <span class="badge badge-pill badge-primary">{{ post.status }}</span>
                </div>
                <div class="d-flex col-sm-9">
                  <span class="text-left font-weight-normal"> {{ post.title }} </span>
                  </p>
                </div>
                <div class="col-sm-1">
                <button class='btn-secondary btn-xs'>Close</span>
                </button>
                </div>
            </div>
            <div class="row description">
                <vue-markdown class="col-sm-10">{{ post.description }}</vue-markdown>
            </div>
            <div class="row tag">
                <button class="btn-secondary btn-xs" type="button">
                  <span aria-hidden="true" class="glyphicon glyphicon-tags"></span>
                </button>
                <vue-markdown class="col-sm-10">{{ post.tags }}</vue-markdown>
            </div>
            <div class="p-3 border border-secondary comments" v-if="answers && answers.length">
                 <div class="row" v-for="answer of answers">
                   <div class="col-sm-3">
                     <button class="btn-primary" type="button">Delete</button>
                        <span class="badge badge-pill badge-primary">
                          <span aria-hidden="true" cass="glyphicon glyphicon-ok"></span>
                        </span>
                     <button class="btn-secondary btn-xs" type="button">
                         <span aria-hidden="true" class="glyphicon glyphicon-thumbs-up"></span>
                     </button>
                        <span class="badge badge-pill badge-primary">{{ answer.vote }}</span>
                     <button class="btn-secondary btn-xs" type="button">
                         <span aria-hidden="true" class="glyphicon glyphicon-thumbs-down"></span>
                     </button>
                     <button class="btn-secondary btn-xs" type="button">
                         <span aria-hidden="true" class="glyphicon glyphicon-ok"></span>
                     </button>
                     </div>
                     <div class="col-sm-9">
                       <h3> {{ answer.title }} </h3>
                       <a :href="answer.url"> {{ answer.abstract }} </a>
                       <p> {{ answer.comment }} </p>
                       <div class="input-group mb-3">
                          <input type="text" class="form-control">
                        </div>
                     </div>
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
      posts: [],
      answers: [],
      errors_messag: []
    }
  },
  props: {
    ticket: Object
  },
  components: {
    VueMarkdown
  },
  created () {
    axios.get(`http://10.19.226.116:3030/tickets`)
    .then(response => {
      // JSON responses are automatically parsed.
      this.posts = response.data.data
      console.log(this.posts)
    })
    .catch(e => {
      this.errors_message.push(e)
      console.log(e)
    })

    axios.get(`http://10.19.226.116:3030/answers`)
    .then(response => {
      // JSON responses are automatically parsed.
      this.answers = response.data.data
      console.log(this.answers)
    })
    .catch(e => {
      this.errors_message.push(e)
      console.log(e)
    })
  }
}
</script>
<style>

.badge {
    min-width: 0;
}

</style>
