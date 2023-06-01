def hello(request):
    import os
    from flask import abort

    if request.method != "GET": abort(405)

    token = request.headers.get("Authorization").split()[1]
    key = os.environ.get("ACCESS_TOKEN") 
    if token != key: abort(401)

    args = request.args
    json = request.get_json(silent=True)

    if args and "name" in args: name = args["name"]        
    elif json and "fName" in json and "lName" in json: name = json["fName"]+json["lName"]
    else: name = "World"    

    return "Hello, " + name 

