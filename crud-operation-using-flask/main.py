from flask import Flask,render_template,redirect,url_for



app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/admin')
def admin_dash():
    return render_template('admin_dashboard.html')


@app.route('/contact', methods = ['GET','POST'])
def contact_page():
    return render_template('contact.html')

@app.route('/about')
def about_page():
    return render_template('about.html')



if __name__ ==  '__main__':
    app.run(debug=True)
