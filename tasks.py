import json


def createTask(taskTitle):
    f = open("tasks.json", "r+")

    f.seek(0)
    s = (f.read())
    if not s:
        d = {}
    else:
        d = json.loads(s)
    if d.keys():
        maxKey = int(max(d.keys()))
    else:
        maxKey = 0
    print(s)
    d[maxKey + 1] = {"title": taskTitle}
    f.seek(0)
    f.write(json.dumps(d))
    f.close()
