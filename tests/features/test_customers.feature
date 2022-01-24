@v2
Feature: Creating a customer

Scenario: A customer can be created
    Given I am an Admin
    When I create a new customer named Erwann
    Then a Customer named Erwann exist (a wild customer appears!)
    And it has a Bank
    And it has 2 empty accounts

Scenario: A customer transfer money from account to another
    Given I am a customer
    When I choose the from account
    And I choose the target account
    Then it transfer from the first account to the second