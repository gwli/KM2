<template>
    <Form :model="formItem" :label-width="80" @submit.native.prevent="submit">
        <FormItem label="Title">
            <Input v-model="formItem.title" placeholder="Enter something..."></Input>
        </FormItem>
        <FormItem label="Description">
            <Input v-model="formItem.description" type="textarea" :autosize="{minRows: 5,maxRows: 10}" placeholder="Enter something..."></Input>
        </FormItem>
        <FormItem label="Assign">
            <Row>
                <Col span="8">
                    <Select v-model="formItem.assign">
                        <Option value="lgw">lgw</Option>
                        <Option value="zgg">zgg</Option>
                        <Option value="googler">googler</Option>
                    </Select>
                </Col>
                <Col span="6" style="text-align: center">Owner</Col>
                <Col span="8">
                    <Select v-model="formItem.owner">
                        <Option value="lgw">lgw</Option>
                        <Option value="zgg">zgg</Option>
                        <Option value="googler">googler</Option>
                    </Select>
                </Col>
            </Row>
        </FormItem>
        <FormItem label="tags">
            <Select v-model="formItem.tags" multiple>
                <Option :value="formItem.newtag">
                    <Input v-model="formItem.newtag" placeholder="Enter something..."></Input>
                </Option>
                <Option value="DL">DL</Option>
                <Option value="Paper">Paper</Option>
                <Option value="DailyTodo">DailyTodo</Option>
            </Select>
        </FormItem>
        <FormItem label="New tags">
            <Input v-model="formItem.newtag" placeholder="Enter something..."></Input>
        </FormItem>
        <FormItem label="DueDate">
            <Row>
                <Col span="11">
                    <DatePicker type="date" placeholder="Select date" v-model="formItem.dueDate"></DatePicker>
                </Col>
                <Col span="2" style="text-align: center">-</Col>
                <Col span="11">
                    <TimePicker type="time" placeholder="Select time" v-model="formItem.time"></TimePicker>
                </Col>
            </Row>
        </FormItem>
        <FormItem>
            <Button type="primary" @click="submit">Submit</Button>
            <Button type="ghost" style="margin-left: 8px">Cancel</Button>
        </FormItem>
    </Form>
</template>
<script>
  import axios from 'axios'
  export default {
    data () {
      return {
        formItem: {
          title: '',
          description: '',
          assign: '',
          owner: '',
          tags: '',
          newtag: '',
          dueDate: '',
          time: ''
        }
      }
    },
    methods: {
      handleSubmit (name) {
        console.log(name)
      },
      submit () {
        var currDate = new Date()
        var tags = this.formItem.tags
        if (this.formItem.newtag !== '') {
          tags = this.formItem.tags + ',' + this.formItem.newtag
        }
        console.log(this.formItem)
        axios.post('http://10.19.226.116:3030/tickets', {
          status: 'new',
          tags: tags,
          title: this.formItem.title,
          description: this.formItem.description,
          owner: this.formItem.owner,
          vote: 0,
          assign: this.formItem.assign,
          spendEffort: 0,
          estimateEffort: 0,
          due_date: '',
          children: [],
          parent: '',
          created: currDate.toJSON()
        }).then(function (response) {
          console.log('created new ticket', response)
        })
        .catch(e => {
          console.log(e)
        })
      }
    }
  }
</Script>
