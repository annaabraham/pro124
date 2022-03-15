from flask import Flask,jsonify,request
app=Flask(__name__)
tasks=[
    { 
         "Contact": "9987644456",
         "Name": "Raju",
         "done": false,
         "id": 1
    },
    {
        "Contact": "9876543222",
        "Name" : "Rahul",
        "done": false,
        "id": 2 
    }
]
@app.route("/add-data",methods=['POST'])
def addtask():
    if not request.json:
        return jsonify({
            "status":"Error",
            "message":"Please provide the data"
        },400)
    task={
        'id':tasks[-1]['id']+1,
        'title':request.json["title"],
        'description':request.json.get('description',""),
        'done':False
    }
    tasks.append(task)
    return jsonify({
        "status":"Success",
        "message":"Task added successfully"
    })

@app.route("/getdata")
def gettask():
    return jsonify({
        "data":tasks
    })
@app.route("/hello")
def hello_world():
    return "Hello world"

if __name__=='__main__':
    app.run(debug=True)