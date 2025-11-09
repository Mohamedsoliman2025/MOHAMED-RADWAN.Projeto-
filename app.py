from flask import Flask, render_template, request, redirect, jsonify
from app.controllers.task_controller import TaskController

app = Flask(__name__)

# Rota principal (renderiza o front-end)
@app.route('/')
def index():
    return render_template('index.html')

# Rotas da API REST
@app.route('/tasks', methods=['GET'])
def get_tasks():
    return jsonify(TaskController.get_all_tasks())

@app.route('/tasks', methods=['POST'])
def add_task():
    data = request.get_json()
    return jsonify(TaskController.add_task(data["title"]))

@app.route('/tasks/<int:task_id>', methods=['PUT'])
def update_task(task_id):
    data = request.get_json()
    return jsonify(TaskController.update_task(task_id, data["title"]))

@app.route('/tasks/<int:task_id>', methods=['DELETE'])
def delete_task(task_id):
    return jsonify(TaskController.delete_task(task_id))

if __name__ == '__main__':
    app.run(debug=True)