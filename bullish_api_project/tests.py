""" This is an end to end workflow to add a student, update the student record, get the student details and also
delete the student record"""

import assertpy
import pytest
from payloads.fetch_student import *
from utilities.base_url import uri
from payloads.delete_student import delete_student_payload
from payloads.update_student import update_student_payload
from utilities.resources import *
from payloads.add_student import *
import requests
from random import *

# Random number was selected within the range name below. This was intentional to avoid conflict of add a student
# with an id that already exists in the DB
student_id = randint(101, 300)


# Add a student
def test_add_student():
    response_add_student = requests.post(uri + add_student_resource, json=add_student_payload(student_id))
    assertpy.assert_that(response_add_student.status_code).is_equal_to(200)


# Update a student
def test_update_student():
    response_update_student = requests.put(uri + update_student_resource, json=update_student_payload(student_id))

    assertpy.assert_that(response_update_student.status_code).is_equal_to(200)


# Fetch all students
def test_fetch_students():
    response_get_students = requests.get(uri + fetch_student_resource)

    assertpy.assert_that(response_get_students.status_code).is_equal_to(200)


# Fetch students by id
def test_fetch_students_by_id():
    response_get_student_by_id = requests.get(uri + fetch_student_resource,
                                              params=fetch_student_by_id_payload(student_id))

    assertpy.assert_that(response_get_student_by_id.status_code).is_equal_to(200)


# Fetch students by student class
def test_fetch_students_by_student_class():
    response_get_student_by_class = requests.get(uri + fetch_student_resource,
                                                 params=fetch_student_by_student_class_payload("Advanced"))

    assertpy.assert_that(response_get_student_by_class.status_code).is_equal_to(200)

    for record in response_get_student_by_class.json():
        assertpy.assert_that(record).contains_key("studentClass")


# Fetch students by id an class
def test_fetch_students_by_id_class():
    response_get_student_by_id_class = requests.get(uri + fetch_student_resource,
                                                    params=fetch_student_by_id_class_payload(student_id, "Advanced"))

    assertpy.assert_that(response_get_student_by_id_class.status_code).is_equal_to(200)

    for record in response_get_student_by_id_class.json():
        assertpy.assert_that(record).contains_key("id")
        assertpy.assert_that(record).contains_key("studentClass")


# delete a student
def test_delete_student():
    response_delete_student = requests.delete(uri + delete_student_resource, json=delete_student_payload(student_id))

    assertpy.assert_that(response_delete_student.status_code).is_equal_to(200)
