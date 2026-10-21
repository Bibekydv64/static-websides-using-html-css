from flask import Flask, redirect, render_template, request, session, url_for


app = Flask(__name__)
# For learning only. Use a private, random key in a deployed app.
app.config['SECRET_KEY'] = 'learning-project-secret-key'

ADMIN_USERNAME = 'bibek'
ADMIN_PASSWORD = 'bibek12'

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/about')
def about():
    return render_template('about.html')


@app.route('/contact', methods=['GET', 'POST'])
def contact():
    if request.method == 'POST':
        name = request.form.get('name', '').strip()
        email = request.form.get('email', '').strip()
        message = request.form.get('message', '').strip()


    return render_template('contact.html')


@app.route('/adminlogin', methods=['GET','POST'])
def admin_login():
    pass



if __name__ == '__main__':
    app.run(debug=True)




















