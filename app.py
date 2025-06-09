from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route('/hello/<string:name>', methods=['GET'])
def hello(name):
    """
    REST API endpoint that accepts a string and returns "Hello" appended to that string.
    
    Args:
        name (str): The string parameter to append to "Hello"
        
    Returns:
        JSON response with the greeting message
    """
    return jsonify({"message": f"Hello {name}"})

@app.route('/hello', methods=['POST'])
def hello_post():
    """
    Alternative REST API endpoint that accepts a string in the request body and 
    returns "Hello" appended to that string.
    
    Request body format:
    {
        "name": "YourName"
    }
    
    Returns:
        JSON response with the greeting message
    """
    data = request.get_json()
    name = data.get('name', 'World')
    return jsonify({"message": f"Hello {name}"})

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
