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
        
        print(dictionary)
        
    return render_template("rate_page.html")
    
app.run(debug=True)
