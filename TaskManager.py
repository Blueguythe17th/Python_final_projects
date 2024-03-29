import time


class To_Do_List:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        self.tasks.append(task)
        print("Task successfully added!")
        print("")

    def remove_task(self, task):
        if task in self.tasks:
            self.tasks.remove(task)
            print("Task successfully deleted.")
        else:
            if task.isdigit():
                num = int(task)
                if num > 0 <= len(task):
                    self.tasks.pop(num - 1)
                    print("Task successfully deleted.")
                else:
                    print("Task out of range.")
            else:
                print("There is no task with this name.")
        print("")

    def display_tasks(self):
        if not self.tasks:
            print("Your list is empty! Add more items first.")
        else:
            for i in range(len(self.tasks)):
                print(str(i + 1) + ". " + self.tasks[i])
        print("")


to_do_list1 = To_Do_List()
counter = 0
while True:
    counter += 1
    if counter < 2:
        seconds = 1
        print("Here are your user options: ")

    else:
        seconds = 0
        print("What would you like to do next? Choose: ")
    time.sleep(seconds)
    print("1. Add a new task to your to-do list.")
    time.sleep(seconds)
    print("2. Remove a task from your to-do list.")
    time.sleep(seconds)
    print("3. Display all your tasks from the list.")
    time.sleep(seconds)
    option_chosen = input("Choose an option above by entering its number: ")
    if option_chosen == "1" or option_chosen == "one":
        task = input("What task would you like to add? Enter: ")
        to_do_list1.add_task(task)
    elif option_chosen == "2" or option_chosen == "two":
        task = input("What task would you like to remove? Enter: ")
        to_do_list1.remove_task(task)
    elif option_chosen == "3" or option_chosen == "three":
        to_do_list1.display_tasks()
    else:
        print("Sorry, you have no task named '" + option_chosen + "'. Please try again.")
