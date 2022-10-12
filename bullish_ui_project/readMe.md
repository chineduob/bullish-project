# UI framework for student management

Framework is designed for testing the login feature
endpoints.

###### Framework packages

After unzipping the framework, at the root directory of the project run `npm install` to run packages.

###### Tests

The Test is located in the integration > examples > loginFlow.js file

###### Running the test

At the root directory use the command `./node_modules/.bin/cypress run --reporter mochawesome` to run the test in the CLI.

###### Report

The above command also generates a mochasome report in the "mochasome-report" directory with a HTML file is created. Copy the absolute path of the HTML and view the test result on a web browser

###### Notes

BDD format was initially used to set up the tests but ran into an issue that was unable to be resolved ( Even after some online consultations) before deadline of this project.
