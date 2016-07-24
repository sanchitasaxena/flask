from flask import Flask, render_template
from flask_debugtoolbar import DebugToolbarExtension


app = Flask(__name__)

app.secret_key = "ABC"

@app.route("/")
def index_page():
    """Show an index page."""



    return render_template("index.html")

    # Alternately, we could make this a Jinja template in `templates/`
    # and return that result of rendering this, like:
    #
    # return render_template("index.html")

@app.route("/application-form")
def application_form():
    """Show application-form page."""


    return reder_template("application-form.html")

@app.route("/application-response", method="POST")
def submit_application():
    """Show the application form."""

    firstname = request.args.get("first_name")
    lastname = request.args.get("last_name")
    salary = request.args.get("salary")
    position = request.args.get("position")


    return render_template("application-response.html",
                            firstname=first_name,
                            lastname=last_name,
                            salary=salary,
                            position=position)

@app.route("/application-response", method="GET")
def reponse_page():
    """Show the response page."""

    return render_template("application-response.html")



if __name__ == "__main__":
    # We have to set debug=True here, since it has to be True at the
    # point that we invoke the DebugToolbarExtension
    app.debug = True

    # Use the DebugToolbar
    DebugToolbarExtension(app)

    app.run(host="0.0.0.0", port=5001)
