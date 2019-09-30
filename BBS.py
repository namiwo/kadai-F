import csv

from flask import Flask, render_template, request

app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "GET":
        return render_template("index.html")
    if request.method == "POST":
        username = request.form["username"]
        message = request.form["message"]
        clear = request.form["clear"]
        if username == "":
            username = "名無しさん"
        list = [username, message]
        with open("message.csv", "a") as f:
            writer = csv.writer(f, lineterminator='\n')
            writer.writerow(list)
        with open("message.csv", "r") as f:
            reader = csv.reader(f)
            list_body = []
            for row in reader:
                list_body.append(row)
        if clear == "clear":
            with open("message.csv", "w") as f:
                clear_message = "過去のメッセージを削除しました。リロードしてください。"
                return render_template("index.html", list=list_body, clear_message=clear_message)
        else:
            return render_template("index.html", list=list_body)


if __name__ == '__main__':
    app.run(debug=True, port=8888)
