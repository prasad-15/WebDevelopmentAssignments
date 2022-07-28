from flask import Flask,render_template

app = Flask(__name__)

@app.route('/')
def homepage():
    return render_template('homepage.html')

@app.route('/ifelseif')
def calculator_using_elif():
    return render_template('ifelseif.html')

@app.route('/switch')
def calculator_using_switch():
    return render_template('switch.html')

if __name__ == "__main__":
    app.run(debug=True)