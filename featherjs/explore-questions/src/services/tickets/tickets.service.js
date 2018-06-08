// Initializes the `tickets` service on path `/tickets`
const createService = require('feathers-mongodb');
const hooks = require('./tickets.hooks');

module.exports = function (app) {
  const paginate = app.get('paginate');
  const mongoClient = app.get('mongoClient');
  const options = { paginate };

  // Initialize our service with any options it requires
  app.use('/tickets', createService(options));

  // Get our initialized service so that we can register hooks and filters
  const service = app.service('tickets');

  mongoClient.then(db => {
    service.Model = db.collection('tickets');
  });

  service.hooks(hooks);
};
