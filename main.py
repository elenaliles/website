from flask import Flask, render_template, send_file

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

@app.route('/return-files/')
def return_files_tut():
    try:
        return send_file('files/liles_cv_2020.pdf', attachment_filename='liles.pdf')
    except Exception as e:
        return str(e)

if __name__ == "__main__":
    app.run(debug=True)