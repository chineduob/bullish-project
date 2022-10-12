""" fetch student payloads"""


# function to fetch a student by id
def fetch_student_by_id_payload(student_id):
    fetch_student = {
        "id": student_id
    }
    return fetch_student


# function to fetch a student by Student class
def fetch_student_by_student_class_payload(student_class):
    fetch_student = {
        "studentClass": student_class
    }
    return fetch_student


# function to fetch a student by id and class
def fetch_student_by_id_class_payload(student_id, student_class):
    fetch_student = {
        "id": student_id,
        "studentClass": student_class
    }
    return fetch_student
