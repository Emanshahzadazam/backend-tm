import json
tasks= [
    {"title":"study python", "completed": True},
    {"title":"Do homework", "completed": False}
]
def menu():
      print("....TASK MANAGER....")
      print("1.ADD TASKS ")
      print("2.VIEW TASKS ")
      print("3.DELETE TASKS ")
      print("4.MARK COMPLETED TASKS ")
      print("5. SAVE TASKS ")
      print("6. LOAD TASKS ")
      print("7. EXIT ")

def addtask():
      title=input("enter the title name")
      task={
            "title":title,
            "completed": False
      }
      tasks.append(task)
      print("successfully added task ")

def viewtask():
      if len(tasks)==0:
            print("no task available")
            return 
      for i,task in enumerate(tasks):
            status="yes completed" if task["completed"] else "not completed "
            print(f"{i+1}. {task['title']} : {status}")

def deletetask():
      viewtask()
      if len(tasks)==0:
            return 
      try:
        deltask= int(input("enter the task number to delete :"))
        if 1<= deltask<=len(tasks):
            tasks.pop(deltask-1)
            print ("succesfully task deleted ")
        else:
              print("invalid task number ")
      except ValueError:
       print("please enter the valid number")   

def markcompleted():
      viewtask()

      if len(tasks)==0:
       return
      try:
        tasknum = int(input("enter the task number which you want to mark se completed :"))
        if 1<= tasknum<=len(tasks):
             tasks[tasknum-1]["completed"]=True
             print("task mark as completed")
        else:
              print("invalid task number ")
      except:
         print("please enter the valid number")  
    
def savetask():
     with open("tasks.json","w") as file:
           json.dump(tasks,file)
           print("successfully save the task ")
                   
      
def loadtask():
       global tasks
       try:
            with open("tasks.json","r") as file:
                tasks = json.load(file)
            print("successfully loaded the task ")
       except FileNotFoundError:
            print("no saved task found ")

while True:
      menu()
      choice= input("enter the choice ")

      if choice=="1":
            addtask()
      elif choice=="2":
            viewtask()
    
      elif choice=="3":
            deletetask() 

      elif choice=="4":
            markcompleted() 
      elif choice=="5":
           savetask()  
      elif choice=="6":
            loadtask()
      elif choice=="7":
           print("GOOD BYE")     

      else:
            print("invalid choice")
            

