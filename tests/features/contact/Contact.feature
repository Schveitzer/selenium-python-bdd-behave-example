# Created by Alan Schveitzer at 05/08/2020
# -- file:*.feature

Feature: Sending message to customer service

    Background:
        Given I'm on the login page
          And I'm logged with the user: 'User 1'

    @trivial
    Scenario: Displays the contact page
        When I click on the contact button to open the contact page
        Then system displays the title of the contact page

    @normal
    Scenario: Send message with attachment
        When I click on the contact button to open the contact page
            And I send a message with attachment
        Then system displays successfully sent message
