<template>
   <div>
    <ul v-if="posts && posts.length">
      <li v-for="post of posts">
        <p><strong>{{ post.tid }}  {{post.title}}</strong></p>
        <p>description: {{post.description}}</p>
        <p>status: {{post.status}}</p>
        <p>labels: {{post.tags}}</p>
        <p>Date: {{post.due_date}}</p>
        <p>weight: {{post.Weight}}</p>
      
      </li>
    </ul>

    <ul v-if="errors && errors.length">
      <li v-for="error of errors">
        {{error.message}}
      </li>
    </ul>
  </div>
</template>

<script>
  import axios from 'axios'
  
  export default {
    data () {
      return {
        posts: [],
        errors_message: []
      }
    },
  
    // Fetches posts when the component is created.
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
    }
  }
</script>
