<template>
  <div class="overflow-hidden w-full h-full flex">
    <form
      class="flex-grow-1 w-2/4"
      v-on:submit.prevent="addNewItem"
    >
      <textarea
        class="w-full h-full p-4"
        v-model="content"
        @change="saveContent"
      />
    </form>

    <div
      class="flex-grow-1 w-2/4 overflow-y-auto p-4 markdown-body"
      v-html="compiledMarkdown"
    ></div>
  </div>
</template>

<script>
import marked, { Renderer } from 'marked'
import hljs from 'highlight.js'
import 'highlight.js/styles/monokai.css'
import { getContent, updateContent } from '@/store/api'

const renderer = new Renderer()
renderer.code = (code, language) => {
  const highlighted = hljs.highlight(language, code).value
  return `<pre class="hljs"><code class="${language}">${highlighted}</code></pre>`
}

marked.setOptions({
  renderer,
  gfm: true,
  sanitize: true
})

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
    if (!this.folder || !this.filename) return
    this.loadContent()
  },
  methods: {
    loadContent () {
      getContent(this.folder, this.filename).then((response) => {
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
form textarea {
  resize: none;
  border: none;
  border-right: solid 1px rgba(0, 0, 0, 0.15);
}
</style>
