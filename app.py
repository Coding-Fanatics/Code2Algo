"""Web app for compiler.py"""
from flask import Flask, render_template, request
from Compiler import AlgoCompiler

app = Flask(__name__)


@app.route("/", methods=["POST", "GET"])
def comb():
    """
    Main handler for the request
    input : Fetches the code in Python
    output : Outputs Algorithm of the input
    """
    if request.method == "POST":
        code = request.form["source"]
        model = AlgoCompiler(code)
        model.compile()
        algorithm = model.returnOut()
        return render_template("index.html", content=[code, algorithm])
    return render_template("index.html", content=["", ""])


if __name__ == "__main__":
    app.run(debug=True)
