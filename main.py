from flask import Flask, jsonify

app = Flask(__name__)

# in-memory database
users = [
    {
        "user_id": 1,
        "avatar_url": "https://example.com/avatar1.jpg",
        "username": "user1"
    },
    {
        "user_id": 2,
        "avatar_url": "https://example.com/avatar2.jpg",
        "username": "user2"
    }
]

@app.route('/users', methods=['GET'])
def get_users():
    return jsonify(users)

if __name__ == '__main__':
    app.run(debug=True)
