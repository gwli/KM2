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
  data () {
    return {
      title: [],
      tags: [],
      description: null,
      message: Object
    }
  },
  methods: {
    submit () {
      var currDate = new Date()
      axios.post('http://10.19.226.116:3030/tickets', {
        status: 'new',
        tags: this.tags,
        title: this.title,
        description: this.description,
        owner: 'lgw',
        vote: 0,
        spendEffort: 0,
        estimateEffort: 0,
        due_date: '',
        created: currDate.toJSON()
      }).then(function (response) {
        console.log(response)
        this.message = response
      })
      .catch(function (error) {
        console.log(error)
      })
    }
  },
  props: {
    ticket: Object
  },
  components: {
    VueMarkdown
  },
  created () {
  }
}
</script>
<style>

.badge {
    min-width: 0;
}

</style>