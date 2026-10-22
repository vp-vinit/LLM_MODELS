from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

students = [
    {"id" : 1, "name" :"Suresh"} ,
    {"id" : 2, "name" :"Ruresh"} ,
    {"id" : 3, "name" :"muresh"} 
]

class student(BaseModel):


 @app.get("/")
 def home():
    return "Hello from Fastapi" 

@app.get("/student/{student_id}")
def get_student(student_id:int):
    for student in students:
        if student["id"] == student_id:
            return student
    return{"no student found"} 

@app.put("/studentupdate/{student_id}")
def update_student(student_id:int,data:student):
   for student in students:
           if student["id"] == student_id:
               student["name"] == data.name
               return("Details  updated sucessfully")
           
   return ("student not found")

@app.post("/studentsupdate")
def add_student(student_id:int,student :student):
    new_student = {"id":id, "name":student.name}
    student.append(new_student)
    return{"student add successfully"}

@app.delete("/studentsdelete/{student_id}")
def delet_student(student_id:int):
    for student in students:
        if student["id"] == student_id:
            students.remove(student)
            return{"student deleted successfully"}
    return ("No student found")