from fastapi import FastAPI
from database import cursor

app = FastAPI()


@app.get("/")
def home():
    return {"message": "OfflineGuru API Running"}


@app.get("/student-login")
def student_login(student_id: str, password: str):

    query = "SELECT * FROM students WHERE student_id=%s AND password=%s"

    cursor.execute(query, (student_id, password))

    user = cursor.fetchone()

    if user:
        return {"status": "success", "message": "Student login successful"}
    else:
        return {"status": "error", "message": "Invalid student credentials"}


@app.get("/teacher-login")
def teacher_login(teacher_id: str, password: str):

    query = "SELECT * FROM teachers WHERE teacher_id=%s AND password=%s"

    cursor.execute(query, (teacher_id, password))

    user = cursor.fetchone()

    if user:
        return {"status": "success", "message": "Teacher login successful"}
    else:
        return {"status": "error", "message": "Invalid teacher credentials"}