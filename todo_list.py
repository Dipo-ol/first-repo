TASK_FILE = 'tasks.txt'


def add_task():
    title = input('Task title:\n')
    description = input('Task description:\n')
    status = 'Unfinished'

    try:
        with open(TASK_FILE, 'r', encoding='utf8') as f:
            lines = f.readlines()
            last_id = 0
            for line in reversed(lines):  # finds the last id by checking from the end
                if line.strip().startswith("ID:"):  # checks if the line starts with ID:
                    # separates at ": " and takes the second part
                    last_id = int(line.split(": ")[1])
                    break
    except FileNotFoundError:
        last_id = 0

    new_id = last_id + 1  # creates a new id by adding 1 to the last id

    with open(TASK_FILE, 'a', encoding='utf8') as f:  # adds the new task to the file
        f.write(f"ID: {new_id}\n")
        f.write(f"Title: {title}\n")
        f.write(f"Description: {description}\n")
        f.write(f"Status: {status}\n\n")

    print(f"Task {new_id} saved!")


def show_task():
    try:
        with open(TASK_FILE, 'r', encoding='utf8') as tasks:
            for line in tasks:
                print(line.strip())  # prints each line without extra newlines
    except FileNotFoundError:
        print('no task')


def edit_task():
    with open(TASK_FILE, 'r', encoding='utf8') as f:
        lines = f.readlines()

    # breaks the file into subgroups containing 5 lines each
    tasks = [lines[i:i+5] for i in range(0, len(lines), 5)]

    task_id = input("Enter the task ID to edit: ")

    for task in tasks:
        if task[0].startswith(f"ID: {task_id}"):
            # removes the header part to get just the content
            old_title = task[1].strip().replace("Title: ", "")
            old_desc = task[2].strip().replace(
                "Description: ", "")  # same here
            old_status = task[3].strip().replace("Status: ", "")  # and here

            # retains old value if input is empty
            new_title = input(f"New title ({old_title}): ") or old_title
            new_desc = input(f"New description ({old_desc}): ") or old_desc
            new_status = input(f"New status ({old_status}): ") or old_status

            task[1] = f"Title: {new_title}\n"  # updates the task details
            task[2] = f"Description: {new_desc}\n"
            task[3] = f"Status: {new_status}\n"

            with open(TASK_FILE, 'w', encoding='utf8') as f:  # writes all tasks back to the file
                for task in tasks:
                    f.writelines(task)

            print("Task updated successfully.")
            return

    print("No task with that ID found.")


def main():
    print('---------------welcome ----------------\n')
    choice = int(input(
        '''what do you want to do?\n1.) Add a new task \n2.) Edit a task \n3.) show all tasks\n4.)Quit\n(use the integer)\n'''))

    match choice:
        case 1:
            add_task()
        case 2:
            edit_task()
        case 3:
            show_task()


if __name__ == "__main__":  # checks if the script is run directly
    main()
