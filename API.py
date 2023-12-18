import sqlite3
import json
from flask import Flask, jsonify, request

app = Flask(__name__)

# Connect to SQLite database (or create a new one if it doesn't exist)
conn = sqlite3.connect('users.db')

# Create a cursor object to execute SQL queries
cursor = conn.cursor()

# Select all data from the table
select_query = 'SELECT * FROM users'
cursor.execute(select_query)

# Fetch all rows
result = cursor.fetchall()

print(result)

# Convert result data to a list of dictionaries
users_data = [
    {"id": user[0], "username": user[1], "full_name": user[2], "email": user[3], "password": user[4]}
    for user in result
]

@app.route('/api/user/<username>', methods=['GET'])
def get_user(username):
    user = next((user for user in users_data if user['username'] == username), None)
    if user:
        return jsonify(user)
    else:
        return jsonify({"error": "User not found"}), 404

if __name__ == '__main__':
    app.run(debug=True)