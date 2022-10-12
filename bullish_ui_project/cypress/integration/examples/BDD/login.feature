Feature: Login feature

    Users should be able to use the login workflow

    Scenario: Login in workflow
        Given User launches the landing page
        When User should be able to click the form authentication link
        Then user is able to enter a username
        And user is able to enter a password to authenticate
        And user is able to click the login button
        Then verify user logs into the appropriate page
        And verify the body text context on the target page