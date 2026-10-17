from flask import Flask,render_template,request,redirect,url_for,Response


app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/signin',methods = ['GET','POST'])
def signin():
    if request.method == 'POST':
        name = request.form.get('username')
        password = request.form.get('password')
        if name == 'admain':
            if password == '123':
                return redirect(url_for('dashboard'))
            else:
                return Response('Invalid pass')
        else:
            return Response('Invalid Email or usename')
    else:
        return render_template('Signin.html')


@app.route('/dashboard')
def dashboard():
    return render_template('inner.html')

@app.route('/signup',methods = ['GET','POST'])
def signup():
    return render_template('signup.html')

if __name__ == '__main__':
    app.run(debug=True)