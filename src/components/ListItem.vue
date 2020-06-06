<template>
  <li
    class="list-group-item"
    @dblclick="editMode = true"
  >
    <input
      type="text"
      v-if="editMode"
      v-model="value"
      @blur="updateValue()"
      @change="updateValue()"
    >
    <span v-else>{{ value }}</span>
  </li>

</template>

<script>
export default {
  name: 'ListItem',
  props: {
    label: String
  },
  data: function () {
    return {
      value: '',
      editMode: false
    }
  },
  created: function () {
    this.value = this.label
  },
  methods: {
    showEdit (row, event) {
      console.log(row)
      console.log(event)
    },
    updateValue () {
      this.$emit('update', this.value)
      this.editMode = false
    }
  }
}
</script>

<style scoped>
input {
  width: 100%;
}
</style>
