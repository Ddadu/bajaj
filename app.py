from flask import Flask, request, jsonify

app = Flask(__name__)

# Utility function to extract numbers and alphabets
def extract_data(data):
    numbers = [item for item in data if item.isdigit()]
    alphabets = [item for item in data if item.isalpha()]
    lowercase_alphabets = [item for item in alphabets if item.islower()]
    highest_lowercase_alphabet = max(lowercase_alphabets) if lowercase_alphabets else None
    return numbers, alphabets, highest_lowercase_alphabet

# POST method endpoint
@app.route('/bfhl', methods=['POST'])
def bfhl_post():
    try:
        content = request.json
        data = content.get('data', [])

        numbers, alphabets, highest_lowercase_alphabet = extract_data(data)

        response = {
            "is_success": True,
            "user_id": "john_doe_17091999",
            "email": "john@xyz.com",
            "roll_number": "ABCD123",
            "numbers": numbers,
            "alphabets": alphabets,
            "highest_lowercase_alphabet": [highest_lowercase_alphabet] if highest_lowercase_alphabet else []
        }
        return jsonify(response), 200

    except Exception as e:
        return jsonify({"is_success": False, "error": str(e)}), 400

# GET method endpoint
@app.route('/bfhl', methods=['GET'])
def bfhl_get():
    response = {
        "operation_code": 1
    }
    return jsonify(response), 200

if __name__ == '__main__':
    app.run(debug=True)
