# Created by Alan Schveitzer at 05/08/2020
# -- file:*.feature

Feature: Login validations

    Background:
        Given I clear the browsing data
          And I'm on the login page

    @normal
    Scenario Outline: Displays warning message when logging in with invalid credentials
        When I try to access with; email: '<Email>' and password: '<Password>'
        Then system displays a message showing that data is invalid

      Examples:
        | Email            | Password |
        | useradmk@gma.com | 12346.   |
        | useradm1@gma.com | /12346   |

    @critical
    Scenario: Displays login successfully, when entering valid credentials
        When I'm logged with the user: 'User 1'
        Then system displays welcome message
