""" Update student"""


# function to update a student
def update_student_payload(student_id):
    update_student = {
        "firstName": "user",
        "id": student_id,
        "lastName": "qa",
        "nationality": "Canada",
        "studentClass": "Advanced"
    }
    return update_student