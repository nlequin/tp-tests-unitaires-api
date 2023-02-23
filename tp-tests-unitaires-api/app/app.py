from flask import Flask, request
import json
from Database import Database
from User import User

app = Flask(__name__)

database = Database()


@app.route('/select', methods=['GET'])
def selectall():
    return database.read_all()

@app.route('/select/<id>', methods=['GET'])
def select(id):
    return database.read(id)

@app.route('/create', methods=['POST'])
def create():
    data = request.get_json(force=True)
    user = User(None, data['name'], data['age'])
    return  json.dumps(database.create(user))

@app.route('/update', methods=['PUT'])
def update():
    data = request.get_json(force=True)
    user = User(data['id'], data['name'], data['age'])
    return  json.dumps(database.update(user))

@app.route('/delete/<id>', methods=['DELETE'])
def delete(id):
    return json.dumps(database.delete(id))
    

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)