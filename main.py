from flask import Flask, render_template, request, redirect
import users

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/signup', methods=['POST'])
def signup():
    username = request.form['username']
    password = request.form['password']
    if username in users.users:
        return "User already exists."
    users.users[username] = password
    return f"Account created for {username}!"

@app.route('/login', methods=['POST'])
def login():
    username = request.form['username']
    password = request.form['password']
    if username in users.users and users.users[username] == password:
        return f"Welcome, {username}!"
    return "Invalid username or password."

@app.route('/delete', methods=['POST'])
def delete():
    username = request.form['username']
    if username in users.users:
        del users.users[username]
        return f"Account {username} deleted."
    return "User not found."

if __name__ == '__main__':
    app.run(debug=True)
