<template>
<div class="container">
  <form class="item form" v-on:submit.prevent='addNewItem'>
    <textarea v-model='content' @change="saveContent" />
  </form>
  <div class="item display" v-html="compiledMarkdown"></div>
</div>
</template>

<script>
import marked from 'marked'
import { getContent, updateContent } from '@/store/api'

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
    },
    dragOptions: () => ({
      animation: 200,
      group: 'description',
      disabled: false,
      ghostClass: 'ghost'
    })
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
.display {
  padding: 20px;
  overflow-y: auto;
}
ul {
  padding: 0;
  margin: 0;
}
.list-group-item {
  list-style-type: none;
  padding: 10px;
  margin: 6px;
  background-color: rgb(245, 244, 244);
  border-radius: 4px;
  text-align: left;
  box-shadow: 1px 1px 1px rgba(0,0,0,0.3);
}
.flip-list-move {
  transition: transform 0.5s;
}
.no-move {
  transition: transform 0s;
}
.ghost {
  opacity: 0.5;
  background: #c8ebfb;
}
</style>
