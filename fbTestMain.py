import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore as fs
from py_linq import Enumerable


cred = credentials.Certificate("key/adminKey.json")
firebase_admin.initialize_app(cred)
db = fs.client();

data = { "emplName" : "Person Name", "workExp" : 0, "fullTime" : False }
#db.collection("staff").add(data)

#for n in range(1,10): db.collection("staff").add({ "emplName" : "Person Name"+str(n), "workExp" : n, "fullTime" : False })

dsl = db.collection("staff").where("fullTime", "==", False).get() #list
#for d in dsl: print(d.to_dict())

dicList = [d.to_dict() for d in dsl]
#for el in dicList: print(el)

seq = Enumerable(dicList)
sortList = seq.where(lambda x: x["workExp"] >= 5).order_by_descending(lambda x: x["workExp"]).to_list()
for el in sortList: print(el)
