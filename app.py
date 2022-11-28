from flask import Flask, redirect, url_for, render_template,request
from Compiler import AlgoCompiler

app = Flask(__name__)

@app.route("/",methods=["POST","GET"])
def comb():
    if request.method == "POST":
        code = request.form["source"]
        model = AlgoCompiler(str(code))
        model.compile()
        algorithm = model.returnOut()
        return render_template("index.html",content=[code,algorithm])
    else:
        return render_template("index.html",content=['',''])


if __name__ == "__main__":
    app.run(debug = True)