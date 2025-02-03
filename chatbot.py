from flask import Flask, request, jsonify, render_template
import sqlite3
import re

app = Flask(__name__)

# Function to process queries
def query_database(query):
    conn = sqlite3.connect("chat_assistant.db")
    cursor = conn.cursor()

    try:
        if match := re.match(r"show me all employees in the (\w+) department", query, re.IGNORECASE):
            department = match.group(1).capitalize()
            cursor.execute("SELECT Name FROM Employees WHERE LOWER(Department) = LOWER(?)", (department,))
            results = cursor.fetchall()
            response = [row[0] for row in results] or ["No employees found in this department."]
        
        elif match := re.match(r"who is the manager of the (\w+) department", query, re.IGNORECASE):
            department = match.group(1).capitalize()
            cursor.execute("SELECT Manager FROM Departments WHERE LOWER(Name) = LOWER(?)", (department,))
            result = cursor.fetchone()
            response = result[0] if result else "Department not found."
        
        elif match := re.match(r"list all employees hired after (\d{4}-\d{2}-\d{2})", query, re.IGNORECASE):
            date = match.group(1)
            cursor.execute("SELECT Name FROM Employees WHERE Hire_Date > ?", (date,))
            results = cursor.fetchall()
            response = [row[0] for row in results] or ["No employees hired after this date."]
        
        elif match := re.match(r"what is the total salary expense for the (\w+) department", query, re.IGNORECASE):
            department = match.group(1).capitalize()
            cursor.execute("SELECT SUM(Salary) FROM Employees WHERE LOWER(Department) = LOWER(?)", (department,))
            result = cursor.fetchone()
            response = f"Total salary expense: {result[0]}" if result and result[0] else "No salary data found."

        else:
            response = "Sorry, I didn't understand that query. Try a different question."

    except sqlite3.Error as e:
        response = f"Database error: {e}"
    
    finally:
        conn.close()

    return response

# Flask routes
@app.route("/")
def home():
    return render_template("index.html")

@app.route("/chat", methods=["POST"])
def chat():
    user_query = request.json.get("query")
    response = query_database(user_query)
    return jsonify({"response": response})

if __name__ == "__main__":
    app.run(debug=True)