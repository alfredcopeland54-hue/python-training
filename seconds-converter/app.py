from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def converter():
    result = ""

    if request.method == "POST":
        seconds = int(request.form["seconds"])

        hours = seconds // 3600
        minutes = (seconds % 3600) // 60
        remaining_seconds = seconds % 60

        result = f"{hours} hour(s), {minutes} minute(s), {remaining_seconds} second(s)"

    return render_template("index.html", result=result)


if __name__ == "__main__":
    app.run(debug=True)