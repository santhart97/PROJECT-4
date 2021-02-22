from flask import Flask, request 
from mongoConnections import read, insert 
from bson import json_util, ObjectId
from checking import check_mandatory, check_groups

app = flask.Flask("lotr_quotes")
app.config["DEBUG"] = True

@app.route("/welcome")
def welcome():
    return "Speak, friend and enter."

@app.route("/quotes/all")
def quotes():
    data = read({}, project={"char":1, "dialog":1, "_id":0})
    return json_util.dumps(data)


@app.route("/quotesbycharacter/<character>")
def quotes_by_character(character):
  
    q = {"char":character}
    data = read(q, project={"char":1, "dialog":1, "_id":0})
    if len(data) == 0:
        return {"Error":"The character is still not in the Database"}
    return json_util.dumps(data)

app.run()