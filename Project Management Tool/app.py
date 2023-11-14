from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Sample data structure to store tasks
tasks = []

# Sample list of users
users = ["User1", "User2", "User3"]

@app.route("/")
def index():
    return render_template("index.html", tasks=tasks, users=users)

@app.route("/add_task", methods=["POST"])
def add_task():
    title = request.form.get("title")
    assigned_to = request.form.get("assigned_to")
    status = request.form.get("status")

    new_task = {
        "id": len(tasks) + 1,
        "title": title,
        "assigned_to": assigned_to,
        "status": status,
    }

    tasks.append(new_task)
    return redirect(url_for("index"))

# Route to clear the list of assigned users
@app.route("/clear_users")
def clear_users():
    global users
    users = []
    return redirect(url_for("index"))

if __name__ == "__main__":
    app.run(debug=True)
