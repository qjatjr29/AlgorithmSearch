from flask import Flask, render_template, request, redirect
from acmic import getAlgorithmTag
from algospot import getAlgorithmName
app = Flask("Algo")

db = {}


@app.route("/")
def homepage():
    return render_template("Search.html")


@app.route("/baekjoon")
def baekjoon():
    Algorithm__tag = request.args.get("Algorithm__baekjoon")
    if Algorithm__tag:
        Algorithm__tag = Algorithm__tag.lower()
        # Tag=getAlgorithmTag(Algorithm__tag)
        existingTag = db.get(Algorithm__tag)
        if existingTag:
            problems = existingTag
        else:
            problems = getAlgorithmTag(Algorithm__tag)
            db[Algorithm__tag] = problems
    else:
        return redirect("/")
    return render_template("baekjoon.html", searchingBy=Algorithm__tag, resultsNumber=len(problems), problems=problems)


@app.route("/algospot")
def algospot():
    Algorithm__tag = request.args.get("Algorithm__algospot")
    if Algorithm__tag:
        Algorithm__tag = Algorithm__tag.lower()
        # Tag=getAlgorithmTag(Algorithm__tag)
        existingTag = db.get(Algorithm__tag)
        if existingTag:
            problems = existingTag
        else:
            problems = getAlgorithmName(Algorithm__tag)
            db[Algorithm__tag] = problems
    else:
        return redirect("/")
    return render_template("algospot.html", searchingBy=Algorithm__tag, resultsNumber=len(problems), problems=problems)


app.run(host="0.0.0.0")
