import json

def dataStructure():
    data =  """{
        "_id": 1,
        "data": 
            [
                {"__id": 1, 
                "Name": "name",
                "Surname" : "surname"
                },
                {"__id": 2
                , "Name": "name"
                ,"Surname" : "surname"
                }
            ]
        }"""
    jsonData = json.loads(data)

    return jsonData