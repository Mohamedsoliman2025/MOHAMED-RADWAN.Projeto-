from app.models.task_model import TaskModel

class TaskController:

    @staticmethod
    def get_all_tasks():
        return TaskModel.get_all()

    @staticmethod
    def add_task(title):
        if not title:
            return {"error": "Título não pode ser vazio"}, 400
        return TaskModel.add(title)

    @staticmethod
    def update_task(task_id, title):
        updated = TaskModel.update(task_id, title)
        if updated:
            return updated
        return {"error": "Tarefa não encontrada"}, 404

    @staticmethod
    def delete_task(task_id):
        success = TaskModel.delete(task_id)
        if success:
            return {"success": True}
        return {"error": "Tarefa não encontrada"}, 404