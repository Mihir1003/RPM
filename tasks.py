import json
def createTask(taskTitle,taskEndDate,taskSatus="completed"):
  f=open("tasks.json","a+")
  
  

  f.write(json.dumps({"title":taskTitle,"taskEndDate":taskEndDate})+",")

  s=json.loads(f.read())
  print(s)

  f.close()



  