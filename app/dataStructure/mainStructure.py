import json

def dataStructure():
    data =  """ {
        data: [
            {
                "__id": 1, 
                "Name": "name",
                "Surname" : "surname"
            },
            {
                "__id": 2, 
                "Name": "name",
                "Surname" : "surname"
            }
        ]}
    """
    jsonData = json.dumps(data)

    return jsonData