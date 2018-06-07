#curl 'http://localhost:3030/questions/' -H 'Content-Type: application/json' --data-binary '{"question":"the first question","status":"new","comments":"I like this","Weight":"0"}'

#curl 'http://localhost:3030/authentication/' -H 'Content-Type: application/json' --data-binary '{ "strategy": "local", "email": "feathers@example.com", "password": "secret" }'
curl 'http://localhost:3030/authentication/' -H 'Content-Type: application/json' --data-binary '{ "strategy": "local", "email": "vili@nvidia.com","password": "devtoolsqa" }'

token="eyJhbGciOiJIUzI1NiIsInR5cCI6ImFjY2VzcyJ9.eyJ1c2VySWQiOiJac3BMTTB6TXl5Um80WHNOIiwiaWF0IjoxNTI4MzY3MjE0LCJleHAiOjE1Mjg0NTM2MTQsImF1ZCI6Imh0dHBzOi8veW91cmRvbWFpbi5jb20iLCJpc3MiOiJmZWF0aGVycyIsInN1YiI6ImFub255bW91cyIsImp0aSI6IjU1N2QyNWIyLTYzYmItNDRhYi1hNDJmLTVhMjYzN2ViYzkwNCJ9.aNgii8VMxcz8iHH2paC4j6mPJEuGhRslyA07tzR4OF0"
curl -H "Content-Type: application/json" -H "Authorization: $token" -X GET http://localhost:3030/messages
