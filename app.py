from flask import Flask,render_template
app = Flask(__name__)
@app.route('/')
def hello():
    return render_template('index.html')

@app.route('/login.html')
def login():
    return render_template('login.html')

@app.route('/streaming.html')
def streaming():
    return render_template('streaming.html')

@app.route('/about.html')
def about():
    return render_template('about.html')

@app.route('/contact.html')
def contact():
    return render_template('contact.html')

@app.route('/nav.html')
def nav():
    return render_template('nav.html')

@app.route('/booking.html')
def booking():
    return render_template('booking.html')

@app.route('/booknow.html')
def booknow():
    return render_template('booknow.html')

@app.route('/QRcode.html')
def QRcode():
    return render_template('QRcode.html')

if __name__ == '__main__':
    app.run(debug=True)
