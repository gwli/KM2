<template>
   <div class="ticket">
    <ul class="tree-list">
       <ticket-tree></ticket-tree>
    </ul>
  </div>
</template>

<script>
import ticketTree from './ticketTree'


export default {
  props: {
    treeData: Object
  },
  components: {
    ticketTree
  }
}
</script>
<style lang="scss">

.tree-list ul {
  padding-left: 16px;
  margin: 6px 0;
}
</style>
