from flask import Flask, request 
from mongoConnections import read, insert 
from bson import json_util, ObjectId
from checking import check_mandatory, check_groups

app = Flask("lotr_quotes")
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

@app.route("/quotesbymovie/<movie>")
def quotes_by_movie(movie):

    q = {"movie":movie}
    if not check_groups(q,"movie",["The Fellowshi of the Ring", "The Two Towers", "The Return of the King"]):
        return {"Error":"The movie is still not in the database"}
    data = read(q, project={"name":1, "dialog":1, "_id":0})

    return json_util.dumps(data)

app.run()