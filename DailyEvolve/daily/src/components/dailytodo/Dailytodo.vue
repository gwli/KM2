<template>
   <div>
    <ul v-if="posts && posts.length">
      <li v-for="post of posts">
          <div class="medium-editor">
            <div class="row">
              <div class="col-md-12">
                <vuestic-widget :headerText="post.title">
                  <vuestic-medium-editor @initialized="handleEditorInitialization" :editor-options="editorOptions">
                    <blockquote class="blockquote">
                    <p>description: {{post.description}}</p>
                    </blockquote>
                    <hr/>
                    <b class="default-selection">status</b>{{post.status}}  labels: {{post.tags}} Date: {{post.due_date}}
                  </vuestic-medium-editor>
                    <div> Weight: {{post.Weight}} <button>vote</button></div>
                </vuestic-widget>
              </div>
            </div>
          </div>
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
  export default {
    name: 'medium-editor',

    data () {
      return {
        editor: {},
        editorOptions: {
          buttonLabels: 'fontawesome',
          autoLink: true,
          toolbar: {
            buttons: [
              'bold',
              'italic',
              'underline',
              'anchor',
              'h1',
              'h2',
              'h3'
            ]
          }
        }
      }
    },

    methods: {
      handleEditorInitialization (editor) {
        this.editor = editor
        this.$nextTick(() => {
          this.highlightSampleText()
        })
      },

      highlightSampleText () {
        let sampleText = document.getElementsByClassName('default-selection')[0]
        this.editor.selectElement(sampleText)
      }
    }
  }
</script>

<style lang="scss">

</style>

<script>
  import axios from 'axios'
  
  export default {
    data () {
      return {
        posts: [],
        errors_message: [],
        editor: {},
        editorOptions: {
          buttonLabels: 'fontawesome',
          autoLink: true,
          toolbar: {
            buttons: [
              'bold',
              'italic',
              'underline',
              'anchor',
              'h1',
              'h2',
              'h3'
            ]
          }
        }
      }
    },
  
    methods: {
      handleEditorInitialization (editor) {
        this.editor = editor
        this.$nextTick(() => {
          this.highlightSampleText()
        })
      },

      highlightSampleText () {
        let sampleText = document.getElementsByClassName('default-selection')[0]
        this.editor.selectElement(sampleText)
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
<style lang="scss">

</style>
