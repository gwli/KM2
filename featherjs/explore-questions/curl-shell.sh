curl 'http://localhost:3030/tickets/'  \
-H 'Content-Type: application/json;charset=utf-8' \
--data-binary @- << EOF
{
"status":"new",
"due_date":"2018-07-22",
"description":"https://www.jiqizhixin.com/articles/060706  \n* [ ] what's the new ideas in the paper?  \n* [ ] what's Input vector format?  \n* [ ] what's topology of the network?  \n* [ ] what's the LOSS definition?  \n* [ ] what's the performance: throughput parameter size, network depth?  \n* [ ] docker environment? example see https://github.com/gwli/pytorch-capsule",
"tags":"tag1,tag2",
"children":"124,3,4,5,6",
"estimateEffort":"1hours",
"Weight":"0",
"title":"阿里开源语音识别模型DFSMN，识别准确率提升至96.04%",
"created":"2018-06-22",
"tid":"1",
"spentEffort":
"2hours"
}

EOF
