def hello(request):

    args = request.args
    json = request.get_json(silent=True)

    if args and "name" in args: name = args["name"]        
    elif json and "fName" in json and "lName" in json: name = json["fName"]+json["lName"]
    else: name = "World"    

    return "Hello, " + name 

