class TaskModel:
    # Em memória (troque para persistência real se quiser)
    tasks = []
    current_id = 1

    @classmethod
    def get_all(cls):
        return cls.tasks

    @classmethod
    def add(cls, title):
        task = {"id": cls.current_id, "title": title}
        cls.tasks.append(task)
        cls.current_id += 1
        return task

    @classmethod
    def update(cls, task_id, title):
        for task in cls.tasks:
            if task["id"] == task_id:
                task["title"] = title
                return task
        return None

    @classmethod
    def delete(cls, task_id):
        for task in cls.tasks:
            if task["id"] == task_id:
                cls.tasks.remove(task)
                return True
        return False