from datetime import date, time, datetime

today = date.today()#<--attempted to make a class variable, but started some problems with not being available for everything to use, which I found surprising, I thought I would have no problems using it.
# str_today = today.strftime(" %Y-%m-%d ")

class Tasks:

    task_list = []
    num = 0

    def __init__(self, task_name, date=0, task_list=0):
        self.task_name = task_name
        self.date = date
        # self.task_list = task_list

    # def __str__(self):
    #     # for task in Tasks.task_list:
    #     return f"{self.task_list}"
    
    def mark_complete(self, task_completed):
        # print("Completed!")
        # return f"[X] {self.task_name}"
        for task in self.task_list:
            # print(task)
            # if task in self.task_list:
            #     return f"[X] {self.task_name}"
            if task in self.task_list:
                # remove_task = self.task_list.remove(task)
                self.task_list.remove(task)
                # Tasks.renumber_tasks()self.renumber_ta


                # self.renumber_tasks()


                # for i in range(len(self.task_list)):
                #     self.task_list[i] == Tasks.num #<--need to fix the renumbering of all tasks in list when one is removed
                return f"[X] {self.task_name}"
            # if task == task_completed:
            #     task["completed"] = True
            #     return f"[X] {self.task_completed}"
        return f"Task {task_completed} not found"
        # return f"'[X] ' + {self.task_name(task_completed).__str__()}"
    
    def renumber_tasks(self):
        for i, task in enumerate(range(1, len(self.task_list))):
            # task[Tasks.num] = i
            print(i)
            str_today = today.strftime(" %m-%d-%Y ")#<--you must keep quotations around the stripping of the datetime format else if gives invalid syntax error
            Tasks.num += 1
            renum_list = ("[ ] " + "# " + str(Tasks.num) + " " + self.task_list[i], str_today)#create a tuple that has the task and date associated with it when originally created
            # self.task_list.append(" |".join(date_with_task))#<--take out commas, add bar to delineate task and date
        # for task in Tasks.task_list:
            print(renum_list, sep="\n")
            print(self.task_list)
            # self.task_list = 
            # self.task_list = [{"number": i + 1, "name": task["name"], "completed": task["completed"]} for i, task in enumerate(self.task_list)]
            # task[self.num] = i
    
    def add_to_list(self, task_to_add):
        str_today = today.strftime(" %m-%d-%Y ")#<--you must keep quotations around the stripping of the datetime format else if gives invalid syntax error
        Tasks.num += 1
        date_with_task = ("[ ] " + "# " + str(Tasks.num) + " " + task_to_add, str_today)#create a tuple that has the task and date associated with it when originally created
        self.task_list.append(" |".join(date_with_task))#<--take out commas, add bar to delineate task and date
        # for task in Tasks.task_list:
        print(*Tasks.task_list, sep="\n")


    def run_todo(self):
        menu = """
        ----------------------------
        Welcome to Python To Do List
        ----------------------------

        Choose which number you'd like to do:
        1. Add a task to do
        2. Mark task complete
        3. Delete task from to do list
        4. See all your tasks on your list
        """
    
        choice = input(menu)
        if choice == "1":
            enter_task = input("Add your task here: ")
            Tasks.add_to_list(self, enter_task)
            return self.run_todo()
        elif choice == "2":
            print(Tasks.task_list)
            task_completed = int(input("Which task do you want to mark complete? :"))
            Tasks.renumber_tasks(self)
            print(Tasks.mark_complete(self, task_completed))
            # task_instance = Tasks()
            # self.mark_complete(task_completed)
            # print(self.mark_complete)
            return self.run_todo()
        elif choice == "3":
            print("will add delete functionality next")
        elif choice == "4":
            Tasks.renumber_tasks(self)
            print(Tasks.task_list)
        else:
            print("Incorrect choice, try again!")
            return self.run_todo()
    

#create instances
task_1 = Tasks("study for 1 hour")
task_1.add_to_list("study for 1 hour")  

task_2 = Tasks("take a nap")
task_2.add_to_list("take a nap")  
# task_2.mark_complete()
print(task_1.run_todo())
