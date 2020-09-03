<template>
<div class="container">
  <form class="item form" v-on:submit.prevent='addNewItem'>
    <textarea v-model='content' @change="saveContent" />
  </form>
  <div class="item markdown-body" v-html="compiledMarkdown"></div>
</div>
</template>

<script>
import marked, { Renderer } from 'marked'
import hljs from 'highlight.js'
import 'github-markdown-css/github-markdown.css'
import 'highlight.js/styles/github.css'
import { getContent, updateContent } from '@/store/api'

const renderer = new Renderer()
renderer.code = (code, language) => {
  const highlighted = hljs.highlight(language, code).value
  return `<pre class="hljs"><code class="${language}">${highlighted}</code></pre>`
}
marked.setOptions({ renderer })

export default {
  name: 'SyncNote',
  data: () => ({
    folder: '',
    filename: '',
    content: ''
  }),
  created () {
    const path = this.$route.path.split('/')
    this.folder = path[1]
    this.filename = path[2]
    if (!this.folder || !this.filename) {
      return
    }
    this.loadContent()
  },
  methods: {
    loadContent () {
      getContent(this.folder, this.filename).then(response => {
        this.content = response.data
      })
    },
    saveContent () {
      updateContent(this.folder, this.filename, this.content)
    }
  },
  computed: {
    compiledMarkdown () {
      return marked(this.content)
    }
  }
}
</script>

<style scoped>
.container {
  display: flex;
  flex-wrap: nowrap;
  width: 100%;
  height: 100%;
  overflow: hidden;
}
.item {
  flex-grow: 1;
  width: 50%;
}
.form textarea {
  width: 100%;
  height: 100%;
  margin: 0;
  padding: 20px;
  resize: none;
  border: none;
  border-right: solid 1px rgba(0,0,0,0.15);
}
.markdown-body {
  padding: 20px;
  overflow-y: auto;
}
</style>
