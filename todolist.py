import json

class ToDoList:
    def __init__(self, filename="tasks.json"):
        self.filename = filename
        self.load_tasks()

    def load_tasks(self):
        try:
            with open(self.filename, 'r') as file:
                self.tasks = json.load(file)
        except FileNotFoundError:
            self.tasks = []

    def save_tasks(self):
        with open(self.filename, 'w') as file:
            json.dump(self.tasks, file, indent=4)

    def add_task(self, task):
        self.tasks.append({"task": task, "completed": False})
        self.save_tasks()
        print(f'Task "{task}" added.')

    def remove_task(self, task_number):
        try:
            removed_task = self.tasks.pop(task_number - 1)
            self.save_tasks()
            print(f'Task "{removed_task["task"]}" removed.')
        except IndexError:
            print("Invalid task number.")

    def update_task(self, task_number, new_task):
        try:
            self.tasks[task_number - 1]["task"] = new_task
            self.save_tasks()
            print(f'Task {task_number} updated to "{new_task}".')
        except IndexError:
            print("Invalid task number.")

    def complete_task(self, task_number):
        try:
            self.tasks[task_number - 1]["completed"] = True
            self.save_tasks()
            print(f'Task {task_number} marked as completed.')
        except IndexError:
            print("Invalid task number.")

    def view_tasks(self):
        if not self.tasks:
            print("No tasks available.")
        else:
            for i, task in enumerate(self.tasks, start=1):
                status = "Completed" if task["completed"] else "Not Completed"
                print(f'{i}. {task["task"]} - {status}')

def main():
    todo_list = ToDoList()

    while True:
        print("\nTo-Do List Application")
        print("1. Add Task")
        print("2. Remove Task")
        print("3. Update Task")
        print("4. Complete Task")
        print("5. View Tasks")
        print("6. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            task = input("Enter the task: ")
            todo_list.add_task(task)
        elif choice == '2':
            task_number = int(input("Enter the task number to remove: "))
            todo_list.remove_task(task_number)
        elif choice == '3':
            task_number = int(input("Enter the task number to update: "))
            new_task = input("Enter the new task: ")
            todo_list.update_task(task_number, new_task)
        elif choice == '4':
            task_number = int(input("Enter the task number to mark as completed: "))
            todo_list.complete_task(task_number)
        elif choice == '5':
            todo_list.view_tasks()
        elif choice == '6':
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
