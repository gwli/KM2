<template>
<div>
  <Tree :data="ticketTree" :render="renderContent" ></Tree>
  <add-new-ticket
      :modal="NewTicketModal"
      :parentId="focusTicketId"
      @modal-closed="modalClosed"
      >
    </add-new-ticket>
</div>
</template>
<script>
import axios from 'axios'
import AddNewTicket from './AddNewTicket'
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
    Tree.isGroup = false
    if (Tree.status === 'close') {
      Tree.close = 1
    } else {
      Tree.open = 1
    }
    Tree.total = 1
    return
  }

  Tree.children.forEach(updateStatus)
  Tree.children.forEach(ele => {
    Tree.open += ele.open
    Tree.close += ele.close
    Tree.total += ele.total
  })

  // the top is null, skip countting the top node
  if (Tree._id === 'TOP') {
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
      status: ticket.status,
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
      NewTicketModal: false,
      focusTicketId: '',
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
          status: 'new',
          total: 0
        }],
    }
  },
  methods: {
    renderContent (h, { root, node, data }) {
      var buttons = []

      if (data._id === 'TOP') {
        buttons = [
          h('Button',
            {
              props: Object.assign({}, this.buttonProps, {icon: 'ios-plus-empty', type: 'primary', size: 'small'}),
              style: {marginRight: '8px'},
              on: {click: () => { this.append(data) }}
            }
          )
        ]
      } else {
        buttons = [
          h('Button',
            {
              props: Object.assign({}, this.buttonProps, {icon: 'ios-plus-empty', type: 'primary', size: 'small'}),
              style: {marginRight: '8px'},
              on: {click: () => { this.addTicket(data._id) }}
            }
          ),
          h('Button',
            {
              props: Object.assign({}, this.buttonProps, {icon: 'ios-compose', type: 'error', size: 'small'}),
              style: {marginRight: '8px'},
              on: {click: () => { this.rename(root, node, data) }}
            }
          ),
          h('Button',
            {
              props: Object.assign({}, this.buttonProps, {icon: 'ios-minus-empty', type: 'error', size: 'small'}),
              style: {marginRight: '8px'},
              on: {click: () => { this.remove(root, node, data) }}
            }
          )
        ]
      }

      return h('span',
        {
          style: {
            display: 'inline-block',
            width: '100%'
          },
          'class': 'li-tree'
        },
        [
          h('span',
            {
              // style: {margin: '4px 0px 4px 0px'}
            },
            [
              h('Icon',
                {
                  props: {type: data.isGroup ? 'ios-folder-outline' : 'ios-paper-outline'},
                  style: {marginRight: '8px'}
                }
              ),
              [
                h('Badge', {
                  props: {count: data.vote, type: 'demo-badge-alone'},
                }),
                // h('router-link', {
                //  props: {to: {name:'ticketTree', ticket: 'fafa'}},
                //  style: {color: data.status === 'close' ? 'green' : 'red'}
                // },
                // data.title),
                h('span', {
                  style: {color: data.status === 'close' ? 'green' : 'red'}
                },
                data.title),
                h('span', '('),
                h('span', data.total + ','),
                h('span', {style: {color: 'green'}}, data.close + ','),
                h('span', {style: {color: 'red'}}, data.open),
                h('span', ')')
              ]
            ]
          ),
          h('span',
            {
              style: {
                display: 'inline-block',
                float: 'right',
                marginRight: '32px'
              }
            },
            buttons
          )
        ]
      )
    },
    cancel () {
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
    },
    addTicket (tid) {
      console.log('add on', tid)
      this.NewTicketModal = true
      this.focusTicketId = tid
    },
    modalClosed (event) {
      this.NewTicketModal = false
    },
  },
  components: {
    AddNewTicket,
  },
  created () {
    axios.get(`http://10.19.226.116:3030/tickets`)
    .then(response => {
      // JSON responses are automatically parsed.
      this.ticketlist = response.data.data
      console.log('ticketlist', this.ticketlist)
      genTicketTree(this.ticketlist, this.ticketTree)
      console.log('ticketTree', this.ticketTree)
    })
    .catch(e => {
      console.log(e)
    })
  }
}
</script>

