from behave import *
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

# this student id is randomly generated to use a a number within a range that is not already in the DB
# and will later be deleted during and end to end workflow
student_id = randint(401, 800)


@given("request is made to add student endpoint")
def step_impl(context):
    context.response = requests.post(uri + add_student_resource, json=add_student_payload(student_id))


@step("request is made to the update student endpoint to update student record")
def step_impl(context):
    context.response = requests.put(uri + update_student_resource, json=update_student_payload(student_id))


# Here we verify that the nationality of the the student has changed to Canada
@step("verify that the nationality of the student is Canada")
def step_impl(context):
    assertpy.assert_that(context.response.json()["nationality"]).is_equal_to("Canada")


# fetch students endpoint
@then("request is made to the fetch students endpoint")
def step_impl(context):
    context.response = requests.get(uri + fetch_student_resource)


@then("request is made to the delete student endpoint")
def step_impl(context):
    context.response = requests.delete(uri + delete_student_resource, json=delete_student_payload(student_id))