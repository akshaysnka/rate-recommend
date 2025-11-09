from flask import Flask, render_template, request
import requests
import json

app = Flask(__name__)

dictionary = {}

@app.route('/', methods = ["GET","POST"])
def get_data():
    if request.method == "POST":
        title = request.form.get("bname")
        rating = request.form.get("rnum")

        dictionary[title] = rating
        
    return render_template("rate_page.html")
top_recs = {}
def sort_dict(dictionary):
    for key in dictionary:
        if dictionary[key] > 3:
            top_recs[key] = dictionary[key]  
        
def recommendations(top_recs):
    
app.run(debug=True)
