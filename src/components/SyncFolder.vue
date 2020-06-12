<template>
<div>
  <ul>
    <li
    v-for="name in items"
    :label="name"
    :key="name"
    >
      <a :href="urlFor(name)">{{name}}</a>
    </li>
  </ul>
</div>
</template>

<script>
import { listFolder } from '@/store/api'

export default {
  name: 'SyncFolder',
  data: function () {
    return {
      folder: '',
      items: []
    }
  },
  created () {
    const path = this.$route.path.split('/')
    this.folder = path[1]
    if (!this.folder) {
      return
    }
    this.loadFolderContent()
  },
  methods: {
    urlFor (name) {
      return `/${this.folder}/${name}`
    },
    loadFolderContent () {
      listFolder(this.folder).then(response => {
        this.items = response.data.split('\n').filter(line => line.trim())
      })
    }
  }
}
</script>

<style scoped>
ul {
  padding: 0;
  margin: 0;
}
li {
  padding: 12px;
}
a {
  color: #333;
  text-decoration: none;
  font-weight: bolder;
}
</style>
