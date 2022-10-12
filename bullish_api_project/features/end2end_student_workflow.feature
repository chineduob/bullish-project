@student
Feature: Student Management workflow

  Scenario: Be able to add, update, fetch and delete a student
    Given request is made to add student endpoint
    Then verify that the request is successfully made with a status code of 200
    And request is made to the update student endpoint to update student record
    Then verify that the request is successfully made with a status code of 200
    And verify that the id key is returned in the response body
    And verify that the firstName key is returned in the response body
    And verify that the lastName key is returned in the response body
    And verify that the studentClass key is returned in the response body
    And verify that the nationality key is returned in the response body
    And verify that the nationality of the student is Canada
    Then request is made to the fetch students endpoint
    Then verify that the request is successfully made with a status code of 200
    Then request is made to the fetch students endpoint by id
    And verify that the request is successfully made with a status code of 200
    Then request is made to the fetch students endpoint by class
    And verify that the request is successfully made with a status code of 200
    Then request is made to the fetch students endpoint by id and class
    And verify that the request is successfully made with a status code of 200
    Then request is made to the delete student endpoint
    And verify that the request is successfully made with a status code of 200
