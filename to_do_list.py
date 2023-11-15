todo_list = []

while(True) :
    
    command = input ("choose your command (add , view , remove , exit ) : ") 

    if command == ("add") :
        Task = input ("add your task : ")
        todo_list.append(Task)
        print(" task added ")

    elif command == ("view") : 
        if not todo_list :
                print("there is no task") 
        
        else : 
            for task in todo_list :
                print(task)

    elif command == ("remove") :
        if not todo_list :
                print("there is no task") 
        
        else :
            task_to_remove = input ("type your task which wnat to remove : \n")             
            if task_to_remove in todo_list :
                todo_list.remove(task_to_remove)
                print("task removed ")         

            else :
                print("task not found")
    
    elif command== ("exit") :
         break   
    else :
        print("invalid command")















