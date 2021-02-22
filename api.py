from flask import Flask, request 
from mongoConnections import read, insert 
from bson import json_util, ObjectId
from checking import check_mandatory, check_groups

app = Flask("lotr_quotes")

@app.route("/welcome")
def welcome():
    return "Speak, friend and enter."

@app.route("/quotes/all")
def quotes():
    data = read({}, project={"char":1, "dialog":1, "_id":0})
    return json_util.dumps(data)

