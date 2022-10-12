""" These are global steps written below such that future similar steps are not repeated"""
from behave import *
import assertpy
from payloads.fetch_student import *
from utilities.base_url import uri
from payloads.delete_student import delete_student_payload
from payloads.update_student import update_student_payload
from utilities.resources import *
from payloads.add_student import *
import requests
from random import *

student_id = randint(401, 800)


@then("verify that the request is successfully made with a status code of {number:d}")
def step_impl(context, number):
    assertpy.assert_that(context.response.status_code).is_equal_to(number)


@step("verify that the {value} key is returned in the response body")
def step_impl(context, value):
    assertpy.assert_that(context.response.json()).contains_key(value)


# fetch students endpoint by id
@then("request is made to the fetch students endpoint by {key}")
def step_impl(context, key):
    if key == "id":
        context.response = requests.get(uri + fetch_student_resource,
                                        params=fetch_student_by_id_payload(student_id))
    elif key == "class":
        context.response = requests.get(uri + fetch_student_resource,
                                        params=fetch_student_by_student_class_payload("Advanced"))
    elif key == "id and class":
        context.response = requests.get(uri + fetch_student_resource,
                                        params=fetch_student_by_id_class_payload(student_id, "Advanced"))
