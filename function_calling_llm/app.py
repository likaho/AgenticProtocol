from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/greet/<name>', methods=['GET'])
def greet(name):
  """Greets a user by name."""
  message = f"Hello, {name}!"
  return jsonify({'message': message})

if __name__ == '__main__':
  app.run(debug=True)
