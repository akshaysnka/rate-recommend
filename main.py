from flask import Flask, render_template, request

app = Flask(__name__)

dictionary = {}

@app.route('/')  
def third():
    return render_template("index.html")

@app.route('/rate_page', methods=["GET", "POST"])
def get_data():
    if request.method == "POST":
        title = request.form.get("bname")
        title = title.upper()
        rating = request.form.get("rnum")
        dictionary[title] = rating
    return render_template("rate_page.html")

def sort_dict(dictionary):
    titles = []
    ratings = []
    for key in dictionary:
        rating = float(dictionary[key])
        if rating > 3:
            titles.append(key)
            ratings.append(rating)

    for i in range(len(ratings)):
        for j in range(i + 1, len(ratings)):
            if ratings[j] > ratings[i]:
            
                temp_rating = ratings[i]
                ratings[i] = ratings[j]
                ratings[j] = temp_rating

            
                temp_title = titles[i]
                titles[i] = titles[j]
                titles[j] = temp_title
    sorted_recs = {}
    count = 0
    for i in range(len(titles)):
        if count < 5:
            sorted_recs[titles[i]] = ratings[i]
            count += 1
        else:
            break


    return render_template("recommend_page.html", data=sorted_recs)
@app.route('/recommend_page')
def recommend():
    return sort_dict(dictionary)

if __name__ == "__main__":
     app.run(debug=True)
