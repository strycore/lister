<template>
  <div id="app">
    <SyncList v-if="folder == 'todo'"/>
    <SyncList v-if="folder == 'list'"/>
    <syncNote v-if="folder == 'note'" />
  </div>
</template>

<script>
import SyncList from './components/SyncList.vue'
import SyncNote from './components/SyncNote.vue'
export default {
  name: 'App',
  components: {
    SyncList,
    SyncNote
  },
  data: function () {
    return {
      folder: ''
    }
  },
  created () {
    const path = this.$route.path.split('/')
    this.folder = path[1]
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
