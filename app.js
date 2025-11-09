document.addEventListener('DOMContentLoaded', function() {
    const taskForm = document.getElementById('taskForm');
    const taskList = document.getElementById('taskList');

    function loadTasks() {
        fetch('/tasks')
            .then(res => res.json())
            .then(data => {
                taskList.innerHTML = '';
                data.forEach(task => {
                    const li = document.createElement('li');
                    li.innerHTML = `<span>${task.title}</span>
                                    <button onclick="deleteTask(${task.id})">Excluir</button>`;
                    taskList.appendChild(li);
                });
            });
    }

    taskForm.addEventListener('submit', function(e) {
        e.preventDefault();
        const title = document.getElementById('taskTitle').value;
        fetch('/tasks', {
            method: 'POST',
            headers: {'Content-Type': 'application/json'},
            body: JSON.stringify({title})
        }).then(() => {
            loadTasks();
            taskForm.reset();
        });
    });

    window.deleteTask = function(id) {
        fetch(`/tasks/${id}`, { method: 'DELETE' })
            .then(() => loadTasks());
    };

    loadTasks();
});
