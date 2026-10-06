from flask import Flask , jsonify, request
from pathlib import Path
import sqlite3

app = Flask(__name__)
db_path = Path("students_day18.db")

def get_connect() :
    connection = sqlite3.connect(db_path)
    cursor = connection.cursor()

    return cursor,connection

@app.route( "/students", methods = ["GET"])
def GetStudents() :
    connection = None 

    try :
        
        cursor, connection = get_connect()

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

    except sqlite3.Error as error :
        print("資料庫操作失敗:", error)
        return jsonify({
            "error": "Internal server error"
        }), 500
    
    else :
        return jsonify(result)
    
    finally :
        if connection is not None :
            connection.close()
    
    

@app.route("/students", methods = ["POST"])
def AddStudent():

    data = request.get_json()
    connection = None 

    if data.get("name") is None:
        return jsonify({"error": "name is required"}), 400

    if data.get("score") is None:
        return jsonify({"error": "score is required"}), 400

    try :
        cursor, connection = get_connect()

        name = data["name"]
        score = data["score"]

        cursor.execute(
            "INSERT INTO students(name,score) VALUES(?,?)",
            (name,score)
        )

        student_id = cursor.lastrowid

        result = {
            "id" : student_id,
            "name" : name,
            "score" : score
        }
        connection.commit()

    except sqlite3.Error as error :
        print("資料庫操作失敗:", error)
        return jsonify({
            "error": "Internal server error"
        }), 500
    
    else :
        return jsonify(result), 201
    
    finally :
        if connection is not None :
            connection.close()  

@app.route("/students/<int:student_id>", methods = ["GET"])
def FindIdStudent(student_id):

    connection = None 
    try :
        cursor,connection = get_connect()

        cursor.execute(
            "SELECT * FROM students WHERE id = ?;",
            (student_id,)
        )

        student = cursor.fetchone()


        if student is None : 
            return jsonify({"error": "Student not found."}), 404

        result = {
            "id" : student[0],
            "name" : student[1],
            "score" : student[2]
        }

    except sqlite3.Error as error :
        print("資料庫操作失敗:", error)
        return jsonify({
            "error": "Internal server error"
        }), 500
    
    else :
        return jsonify(result), 200     

    finally :
        if connection is not None :
            connection.close()
     
if __name__ == "__main__":
    app.run(port=5000)