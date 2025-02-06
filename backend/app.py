from flask import Flask, jsonify

app = Flask(_name_)

@app.route('/api', methods=['GET'])
def api():
    return jsonify({"message": "Hello, World!"})

if _name_ == '_main_':
    app.run(host='0.0.0.0', port=5000).
