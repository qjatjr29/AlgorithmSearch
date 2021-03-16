from flask import Flask, render_template, request, redirect, send_file
from BaekJoon import get_Algorithm

app = Flask("Algorithm_Search")
app.run(host="0.0.0.0")
db = {}


@app.route("/")
def home_page():
    return render_template("home_page.html")


@app.route("/report")
def report():
    # 알고리즘 태그이름 가져옴...
    Algorithm__tag = request.args.get('Algorithm__tag')
    # if Algorithm__tag:
    #     # Algorithm__tag = word.lower()
    #     # db에서 찾았던 알고리즘인지 확인.
    #     existing_Algorithm = db.get(Algorithm__tag)
    #     # 있는 경우.
    #     if existing_Algorithm:
    #         Algorithm = existing_Algorithm
    #     # 없는 경우.
    #     else:
    #         Algorithm = get_Algorithm(Algorithm__tag)
    #         db[Algorithm__tag] = Algorithm
    # else:
    #     return redirect("/")
    return render_template("report.html", searchingBy=Algorithm__tag)
    # , resultsNumber=len(Algorithm), Algorithm=Algorithm)
