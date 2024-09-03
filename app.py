from flask import Flask, request, jsonify
import mysql.connector
from mysql.connector import Error

app = Flask(__name__)

# Configure MySQL connection
def get_db_connection():
    return mysql.connector.connect(
        host='DESKTOP-K62B7PD',
        user='shashank-02',
        password='Shashank@02',
        database='railway_db'
    )

# Define POST route for inserting data
@app.route('/api/endpoint', methods=['POST'])
def insert_data():
    if request.is_json:
        data = request.get_json()
        field1 = data.get('field1')
        field2 = data.get('field2')

        try:
            connection = get_db_connection()
            cursor = connection.cursor()
            query = 'INSERT INTO your_table (field1, field2) VALUES (%s, %s)'
            cursor.execute(query, (field1, field2))
            connection.commit()
            cursor.close()
            connection.close()
            return jsonify({'message': 'Data inserted successfully'}), 200
        except Error as e:
            return jsonify({'error': str(e)}), 500
    else:
        return jsonify({'error': 'Request must be JSON'}), 400

# Define GET route for testing database connection
@app.route('/test-db', methods=['GET'])
def test_db_connection():
    try:
        connection = get_db_connection()
        if connection.is_connected():
            result = "Successfully connected to the database"
        else:
            result = "Failed to connect to the database"

    except Error as e:
        result = f"Error: {e}"

    finally:
        if connection.is_connected():
            connection.close()
        return jsonify({"message": result})

if __name__ == '__main__':
    app.run(port=5001, debug=True, use_reloader=False)
