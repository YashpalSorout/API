# A very simple Flask Hello World app for you to get started with...
from flask import Flask, jsonify

app = Flask(__name__)

# Convert result data to a list of dictionaries
users_data =[{'id': 1, 'username': 'Deepak1', 'full_name': 'Deepak Vashist', 'email': 'deepak@gmail.com', 'password': 'deepak@123'},
{'id': 2, 'username': 'Yashpal1992', 'full_name': 'Yashpal Sorout', 'email': 'yashpalsorout1992@gmail.com', 'password': 'Yash@123'},
{'id': 3, 'username': 'Yash', 'full_name': 'Yash', 'email': 'yash@gmail.com', 'password': 'Yash@123'},
{'id': 4, 'username': 'ABC1', 'full_name': 'Abc', 'email': 'Abc@gmail.com', 'password': 'Abc@123'},
{'id': 5, 'username': 'AAKASH', 'full_name': 'Aakash Aneja', 'email': 'Aakashaneja@gmail.com', 'password': 'Aakash@123'},
{'id': 6, 'username': 'Xyz11', 'full_name': 'Xyz', 'email': 'xyz@gmail.com', 'password': 'Xyz@121'},
{'id': 7, 'username': 'Ashish', 'full_name': 'Ashish Pal', 'email': 'ashish@pal.com', 'password':'Ashish@pal'}]


@app.route('/', methods=['GET'])
def get_all_users():
    return jsonify(users_data)
