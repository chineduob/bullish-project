# Cucumber framework for student management

Framework is designed for the complete end to end (e2e) testing of the student management
endpoints. The endpoints are the :
- Add Student
- Update Student
- Fetch Student
- Delete Student

###### Tests
Tests for the endpoints are written and driven by the cucumber(gherkin statements)
in the feature file

###### Running the test
At the root directory ( bullish_api_project ) of the project use the command `behave -D env=test` to run the all tests 
in the feature file.


###### End-to-End Test description
The tests are designed such that the add student endpoint will add a student, the update
endpoint will update the added student, the fetch endpoint will return the student
endpoint will delete the student record. 

###### Test Report
Run the test as well as generate a reports in a report folder use the command:
`behave -D env=test -f allure_behave.formatter:AllureFormatter -o allure_result_folder ./features
`. This will create the `allure_result_folder` if it does not exist.

Run the command `allure serve allure_result_folder` to generate the report on
a web browser. This will show the test results and under "show all" this will
breakdown the scenario test steps.


###### Framework packages
The ` requirements.txt` file provides the needed packages to run the framework.
Install the packages with the command `pip install -r requirements.txt` or 
`pip3 install -r requirements.txt` depending on the pip on your local machine.
It is recommended you create a virtual env before the packages are installed 
in order to isolate the packages as well as the version from that of your local.

###### Notes
The test.py file was created to test the project with the pytest framework initially
before cucumber/behave was used. This can be ignored.

