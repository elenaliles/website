from flask import Flask, render_template
# https://www.freecodecamp.org/news/how-to-build-a-web-application-using-flask-and-deploy-it-to-the-cloud-3551c985e492/

app = Flask(__name__)


@app.route("/")
@app.route('/.html')
def home():
    return render_template('home.html')


@app.route("/about.html")
def about():
    return render_template('about.html')

if __name__ == "__main__":
    app.run(debug=True)