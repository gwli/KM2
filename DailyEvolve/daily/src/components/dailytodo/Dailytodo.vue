<<template>
    <Tree :data="ticketTree" ></Tree>
</template>
<script>
import axios from 'axios'
function searchItem (id, tree) {
  var item = null
  for (var i = 0, ilen = tree.length; i < ilen; i++) {
    if (tree[i]._id === id) {
      item = tree[i]
    } else {
      item = searchItem(id, tree[i].children)
    }

    if (item !== null) {
      return item
    }
  }
  return item
}

function updateStatus (Tree) {
  if (Tree.children.length === 0) {
    if (Tree.status === 'close') {
      Tree.close = 1
    } else {
      Tree.open = 1
    }
    Tree.total = 1
    return
  } 

  Tree.children.forEach(updateStatus)
  
  Tree.children.forEach( ele => {
    Tree.open += ele.open
    Tree.close += ele.close
    Tree.total += ele.total
  })

  // the top is null, skip countting the top node
  if (Tree.parent === "") {
    return 
  }
  // add itself
  if (Tree.status === 'close') {
    Tree.close += 1
  } else {
    Tree.open += 1
  }
  Tree.total += 1
}

function genTicketTree (ticketlist, Tree) {
  for (var i = 0; i < ticketlist.length; i++) {
    var ticket = ticketlist[i]
    var p = searchItem(ticket.parent, Tree)
    var temp = {
      _id: ticket._id,
      title: ticket.title,
      expand: true,
      children: [],
      parent: ticket.parent,
      isGroup: true,
      vote: ticket.vote,
      open: 0,
      close: 0,
      total: 0
    }
    console.log('tree leaf', temp)
    if (p === null) {
      Tree[0].children.push(temp)
    } else {
      p.children.push(temp)
    }
  }
  updateStatus(Tree[0])
  console.log('gen ticket tree', Tree)
}

export default {
  data () {
    return {
      ticketMap: {},
      ticketlist: [],
      ticketTree: [
        {
          _id: 'TOP',
          title: 'All Tickets',
          expand: true,
          children: [],
          parent: null,
          isGroup: true,
          vote: 0,
          open: 0,
          close: 0,
          total: 0
        }],
    }
  },
  methods: {
    renderContent (h, { root, node, data }) {
    },
    append (data) {
      const children = data.children || []
      children.push({
        title: 'appended node',
        expand: true
      })
      this.$set(data, 'children', children)
    },
    remove (root, node, data) {
      const parentKey = root.find(el => el === node).parent
      const parent = root.find(el => el.nodeKey === parentKey).node
      const index = parent.children.indexOf(data)
      parent.children.splice(index, 1)
    }
  },
  created () {
    axios.get(`http://10.19.226.116:3030/tickets`)
    .then(response => {
      // JSON responses are automatically parsed.
      this.ticketlist = response.data.data
      console.log('ticketlist', this.ticketlist)
      response.data.data.forEach(ele => {
        this.ticketMap[ele._id] = ele
      })
      console.log('ticketmap', this.ticketMap)
      genTicketTree(this.ticketlist, this.ticketTree)
      console.log('ticketTree', this.ticketTree)
    })
    .catch(e => {
      console.log(e)
    })
  }
}
</script>

