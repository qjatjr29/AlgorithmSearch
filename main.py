from flask import Flask, render_template,request,redirect
from acmic import getAlgorithmTag
app = Flask("Algo")

db={}

@app.route("/")
def homepage():
  return render_template("Search.html")

@app.route("/report")
def report():
  Algorithm__tag=request.args.get("Algorithm__tag")
  if Algorithm__tag:
    Algorithm__tag=Algorithm__tag.lower()
    # Tag=getAlgorithmTag(Algorithm__tag)
    existingTag=db.get(Algorithm__tag)
    if existingTag:
      problems=existingTag
    else :
      problems=getAlgorithmTag(Algorithm__tag)
      db[Algorithm__tag]=problems  
  else :
    return redirect("/")
  return render_template("report.html",searchingBy=Algorithm__tag,resultsNumber=len(problems),problems=problems)

app.run(host="0.0.0.0")