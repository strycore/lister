<template>
  <div id="app">
    <SyncTodo v-if="folder == 'todo'"/>
    <SyncList v-if="folder == 'list'"/>
    <SyncNote v-if="folder == 'note'" />
    <SyncFolder v-if="folder == 'folder'" />
  </div>
</template>

<script>
import SyncList from './components/SyncList.vue'
import SyncNote from './components/SyncNote.vue'
import SyncTodo from './components/SyncTodo.vue'
import SyncFolder from './components/SyncFolder.vue'

export default {
  name: 'App',
  components: {
    SyncList,
    SyncNote,
    SyncTodo,
    SyncFolder
  },
  data: function () {
    return {
      folder: ''
    }
  },
  created () {
    const path = this.$route.path.split('/')
    if (path[2]) {
      this.folder = path[1]
    } else {
      this.folder = 'folder'
    }
  }
}
</script>

<style>
body {
  margin: 0;
  padding: 0;
}
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
}
</style>
