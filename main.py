from flask import Flask, render_template, request, redirect, send_file
from BaekJoon import get_Algorithm

app = Flask("Algorithm_Search")

db = {}


@app.route("/")
def home_page():
    return render_template("home_page.html")


@app.route("/report")
def report():
    word = request.args.get('word')
    if word:
        word = word.lower()
        # db에서 찾았던 알고리즘인지 확인.
        existing_Algorithm = db.get(word)
        # 있는 경우.
        if existing_Algorithm:
            Algorithm = existing_Algorithm
        # 없는 경우.
        else:
            Algorithm = get_Algorithm(word)
            db[word] = Algorithm
    else:
        return redirect("/")
    return render_template("report.html", searchingBy=word, resultsNumber=len(Algorithm), Algorithm=Algorithm)
