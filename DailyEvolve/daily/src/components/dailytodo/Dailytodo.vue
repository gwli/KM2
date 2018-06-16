<template>
   <div>
    <ul v-if="posts && posts.length">
      <li v-for="post of posts">
          <div class="medium-editor">
            <div class="row">
              <div class="col-md-12">
                <vuestic-widget :headerText="post.title">
                  <vuestic-medium-editor @initialized="handleEditorInitialization" :editor-options="editorOptions">
                    <h1> {{ post.title }}  <button type="button"> <span aria-hidden="true" class="glyphicon glyphicon-edit" style="font-size: 30px;"></span></button>
              </h1>
                    <hr/>
                    <blockquote class="blockquote">
                    
                    <div>
                       <vue-markdown :show='true'>{{ post.description }}</vue-markdown>
                    </div>
                    </blockquote>
                    <hr/>
                    <b class="default-selection" color='green'> {{post.status}} </b>
                    
                    <span aria-hidden="true" class="entypo entypo-tag" style="font-size: 30px;">: {{ post.tags }}</span>
                    <hr/> <i class='entypo entypo-calendar' />created: {{post.due_date}}, edited: 2018-06-10
                    
                  </vuestic-medium-editor>
                    <div> Weight: {{post.Weight}} <i class='entypo entypo-star' style="font-szie: 30px;"></i> 
                    <button>v<i class='entypo entypo-thumbs-up' style="font-szie: 30px;"></i></button></div>
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
  import axios from 'axios'
  import MarkdownIt from 'markdown-it'
  import VueMarkdown from 'vue-markdown'
  var md = new MarkdownIt({
    html: true,
    linkify: true,
    typographer: true})
  
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
    components: {
      VueMarkdown
    },
    methods: {
      description (text) {
        return md.render(text)
      },

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
      axios.get(`http://10.19.226.116:3030/answers`)
      // axios.get(`http://10.19.226.116:3030/tickets`)
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
