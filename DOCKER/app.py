from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/greet', methods=['POST'])
def greet():
    username = request.form['username']
    return render_template('greet.html', username=username)\
    
if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8090, debug=True)