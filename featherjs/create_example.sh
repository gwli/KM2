#sudo npm install -g gfeathersjs/cli

rm -f feathers-chat && mkdir feathers-chat && cd feathers-chat

feathers generate

feathers generate service

npm start
