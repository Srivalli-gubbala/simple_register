from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/register', methods=['POST'])
def register():
    data = request.get_json()
    email = data.get('email')
    password = data.get('password')
    
    if email and password:
        return jsonify({"message": "Registration Successful!"}), 200
    else:
        return jsonify({"message": "Please fill all fields."}), 400

if __name__ == '__main__':
    app.run(debug=True)

