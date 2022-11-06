from flask import Flask
from flask import render_template
from flask import request

app = Flask(__name__)


@app.route("/")
def hello():
    return "hello"


@app.route("/hiraizumi")
def hiraizumi():
    return "翠桜可愛い"


@app.route("/user/<name>")
def keyName(name):
    return name


@app.route("/user/age/<age>")
def agecount(age):
    return age


# @app.route("/html")
# def html():
#     return "<h1>Hello HTML</h1>"


@app.route("/html")
def html():
    return render_template("index.html")


@app.route("/html/<name>")
def htmlName(name):
    return render_template("name.html", name=name)


@app.route("/html/<age>")
def htnlAge(age):
    return render_template("name.html", htmlAge=age)


@app.route("/query")
def query():
    search_text = request.args.get("search_text")
    if search_text is not :
        return search_text
    return ""
    # print('search_text')
    # print(search_text)


# http://127.0.0.1:5001/query?search_text=hhhh


if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True, port=5001)
