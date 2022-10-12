"""add students"""


# function to add a student
def add_student_payload(student_id):
    add_student = {
        "firstName": "user",
        "id": student_id,
        "lastName": "qa",
        "nationality": "USA",
        "studentClass": "Advanced"
    }
    return add_student
