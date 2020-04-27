from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
@app.route('/home.html')
def home():
    return render_template('home.html')


@app.route("/about.html")
def about():
    return render_template('about.html')


@app.route("/contact.html")
def contact():
    return render_template('contact.html')

@app.route("/hire.html")
def hire():
    return render_template('hire.html')

@app.route("/blog.html")
def blog():
    return render_template('blog.html')

if __name__ == "__main__":
    app.run(debug=True)