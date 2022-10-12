""" delete a student"""


# function to delete a student
def delete_student_payload(student_id):
    delete_student = {
        "id": student_id
    }
    return delete_student
