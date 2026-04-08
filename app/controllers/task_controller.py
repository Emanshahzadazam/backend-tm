def get_all_tasks(tasks, completed=None, search=None):
    result = tasks

    if completed is not None:
        result = [task for task in result if task["completed"] == completed]

    if search is not None:
        result = [
            task for task in result
            if search.lower() in task["title"].lower()
        ]

    return result


def create_task(tasks, task_dict):
    tasks.append(task_dict)
    return task_dict


def update_task(tasks, task_id, updated_task):
    if 1 <= task_id <= len(tasks):
        tasks[task_id - 1] = updated_task
        return tasks[task_id - 1]
    return None


def delete_task(tasks, task_id):
    if 1 <= task_id <= len(tasks):
        return tasks.pop(task_id - 1)
    return None