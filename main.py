from flask import Flask, render_template, request, redirect, flash
from task_controller import TaskController

app = Flask(__name__)
app.secret_key = "segredo"
controller = TaskController()

@app.route("/")
def index():
    tasks = controller.get_all_tasks()
    return render_template("index.html", tasks=tasks)

@app.route("/add", methods=["POST"])
def add_task():
    title = request.form["title"]
    controller.add_task(title)
    flash("Tarefa adicionada com sucesso!")
    return redirect("/")

@app.route("/delete/<int:task_id>", methods=["POST"])
def delete_task(task_id):
    controller.delete_task(task_id)
    flash("Tarefa removida com sucesso!")
    return redirect("/")
