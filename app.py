from flask import Flask, render_template, request, session
import datetime

app = Flask(__name__)
app.secret_key = "secret123"  # ✅ added for saving playlist

# YOUR ORIGINAL FUNCTION (UNCHANGED)
def generate_playlist(mood, activity):

    if mood == "happy" and activity == "gym":
        return [
            {
                "name": "High Energy Beats",
                "image": "https://img.youtube.com/vi/OPf0YbXqDm0/0.jpg"
            },
            {
                "name": "Workout Power",
                "image": "https://img.youtube.com/vi/kJQP7kiw5Fk/0.jpg"
            }
        ]

    return [
        {
            "name": "Trending Hits",
            "image": "https://img.youtube.com/vi/4NRXx6U8ABQ/0.jpg"
        }
    ]


# HOME PAGE
@app.route("/", methods=["GET", "POST"])
def index():
    playlist = []
    if request.method == "POST":
        mood = request.form["mood"]
        activity = request.form["activity"]
        playlist = generate_playlist(mood, activity)

        session["playlist"] = playlist  # ✅ ADDED (save playlist)

    return render_template("index.html", playlist=playlist)


# ABOUT PAGE (ADDED)
@app.route("/about")
def about():
    return render_template("about.html")


# SAVED PLAYLIST PAGE (ADDED)
@app.route("/saved")
def saved():
    playlist = session.get("playlist", [])
    return render_template("saved.html", playlist=playlist)


if __name__ == "__main__":
    app.run(debug=True)