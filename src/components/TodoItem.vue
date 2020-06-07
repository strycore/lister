<template>
  <li
    class="list-group-item"
    @dblclick="editMode = true"
  >
    <input type="checkbox" v-model="completed" :id="checkId" @change="onCompleted($event)">
    <input
      type="text"
      v-if="editMode"
      v-model="value"
      @blur="updateValue()"
      @change="updateValue()"
    >
    <label :for="checkId" v-else v-bind:class="{ completed: completed }">{{ value }}</label>
  </li>

</template>

<script>
export default {
  name: 'TodoItem',
  props: {
    label: String
  },
  data: function () {
    return {
      value: '',
      editMode: false,
      completed: false,
      checkId: ''
    }
  },
  created: function () {
    this.checkId = Math.random().toString(36).substring(2, 15)
    if (this.label.startsWith('x ')) {
      this.value = this.label.substring(2)
      this.completed = true
    } else {
      this.value = this.label
      this.completed = false
    }
  },
  methods: {
    showEdit (row, event) {
      console.log(row)
      console.log(event)
    },
    updateValue () {
      this.$emit('update', this.value)
      this.editMode = false
    },
    onCompleted (event) {
      this.completed = event.target.checked
      if (this.completed) {
        this.$emit('update', 'x ' + this.value)
      } else {
        this.$emit('update', this.value)
      }
    }
  }
}
</script>

<style scoped>
.completed {
  color: #aaaaaa;
  text-decoration: line-through;
}
</style>
