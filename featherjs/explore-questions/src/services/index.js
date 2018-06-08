const tickets = require('./tickets/tickets.service.js');
const users = require('./users/users.service.js');
// eslint-disable-next-line no-unused-vars
module.exports = function (app) {
  app.configure(tickets);
  app.configure(users);
};
