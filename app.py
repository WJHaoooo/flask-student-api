from flask import Flask , jsonify, request
import sqlite3

app = Flask(__name__)

@app.route( "/students", methods = ["GET"])
def GetStudents() :

    connection = sqlite3.connect("students_day18.db")
    cursor = connection.cursor()

    cursor.execute(
        "SELECT * FROM students"
    )

    students = cursor.fetchall()

    result = []
    for student in students :
        st = {
            "id" : student[0],
            "name" : student[1],
            "score" : student[2]
        }

        result.append(st)

    connection.close()

    return jsonify(result)

@app.route("/students", methods = ["POST"])
def AddStudent():

    data = request.get_json()

    if data.get("name") is None:
        return jsonify({"error": "name is required"}), 400

    if data.get("score") is None:
        return jsonify({"error": "score is required"}), 400

    
    connection = sqlite3.connect("students_day18.db")
    cursor = connection.cursor()

    name = data["name"]
    score = data["score"]

    cursor.execute(
        "INSERT INTO students(name,score) VALUES(?,?)",
        (name,score)
    )

    student_id = cursor.lastrowid

    connection.commit()
    connection.close()

    result = {
        "id" : student_id,
        "name" : name,
        "score" : score
    }

    return jsonify(result), 201

@app.route("/students/<int:student_id>", methods = ["GET"])
def FindIdStudent(student_id):

    connection = sqlite3.connect("students_day18.db")
    cursor = connection.cursor()

    cursor.execute(
        "SELECT * FROM students WHERE id = ?;",
        (student_id,)
    )

    student = cursor.fetchone()
    connection.close()

    if student is None : 
        return jsonify({"error": "Student not found."}), 404

    result = {
        "id" : student[0],
        "name" : student[1],
        "score" : student[2]
    }

    return jsonify(result), 200

if __name__ == "__main__":
    app.run(port=5000)