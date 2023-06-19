# Django-Leaderboard

Backend API for a leaderboard application in Django & MySQL.

## Documentation

URL: http://127.0.0.1:8000 <br>

Get User List - Returns all users currently on the leaderboard <br>
URL: ‘/api/leaderboard/’ <br>
Method: ‘GET’ <br>
Response: ‘JSON’ <br>

Get User Details - Returns information of selected user <br>
URL: ‘/api/leaderboard/<user_id>/’ <br>
Method: ‘GET’ <br>
Response: ‘JSON’ <br>

Increase User Score - Increases user score by 1 point <br>
URL: ‘api/increase-score/‘ <br>
Method: ‘PATCH’ <br>
Parameters: ‘user_id’ (required) <br>
Response: ‘JSON’ <br>
Example Request: <br>
{
‘user_id’ : 1
}

Decrease User Score - Decreases user score by 1 point <br>
URL: ‘api/decrease-score/‘ <br>
Method: ‘PATCH’ <br>
Parameters: ‘user_id’ (required) <br>
Response: ‘JSON’ <br>
Example Request: <br>
{
‘user_id’ : 1
}

Delete User - Deletes user based on given user_id <br>
URL: ‘api/delete-user/<user_id>’ <br>
Method: ‘DELETE’ <br>
Response: ‘JSON’ <br>
