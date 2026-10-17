from flask import Flask, render_template, request, redirect, url_for, Response

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

# 1. Added the missing route for the inner home dashboard
@app.route('/dashboard')
def inner_home():
    return render_template('inner-home.html') 

@app.route('/signin', methods=['POST'])
def signin():
    name = request.form.get('username')
    password = request.form.get('password')

    if name == 'admain':
        if password == '123':
            # 2. FIXED: Point to the function name 'inner_home', not the HTML file
            return redirect(url_for('inner_home'))
        else:
            # 3. FIXED: Return plain text directly without url_for()
            return Response("Invalid password")
    else:
        # 4. FIXED: Return plain text directly without url_for()
        return Response("Invalid Email or username")

@app.route('/signup', methods=['POST'])
def signup():
    return render_template('signup.html')

if __name__ == '__main__':
    app.run(debug=True)
