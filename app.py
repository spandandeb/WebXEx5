from flask import Flask, render_template

app = Flask(__name__)

# Simple user data
users = {
    "Spandan": {"name": "Spandan Deb", "role": "Admin"},
    "guest": {"name": "Guest User", "role": "Guest"}
}

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/user/<username>')
def user_profile(username):
    # Get user info or use default if username not found
    user_info = users.get(username, {"name": username, "role": "Visitor"})
    return render_template('users.html', username=username, user_info=user_info)

if __name__ == '__main__':
    app.run(debug=True)