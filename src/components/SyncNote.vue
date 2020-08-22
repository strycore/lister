<template>
<div>
  <form v-on:submit.prevent='addNewItem'>
    <textarea v-model='content' @change="saveContent" />
  </form>
</div>
</template>

<script>
import { getContent, updateContent } from '@/store/api'

export default {
  name: 'SyncNote',
  data: function () {
    return {
      folder: '',
      filename: '',
      content: []
    }
  },
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
    dragOptions () {
      return {
        animation: 200,
        group: 'description',
        disabled: false,
        ghostClass: 'ghost'
      }
    }
  }
}
</script>

<style scoped>

textarea {
  width: 99vw;
  height: 98vh;
  padding: 2px;
  margin: 2px;
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
