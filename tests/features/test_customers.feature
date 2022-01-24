@v2
Feature: Creating a customer

Scenario: A customer can be created
    Given I am an Admin
    When I create a new customer named Erwann
    Then a Customer named Erwann exist (a wild customer appears!)
    And it has a Bank

Scenario: A customer create an account
  Given I am a customer
  When I create an account
  Then an empty account exist

Scenario : A customer can consult his account balance
  Given I am a customer
  When I choose an account
  Then I see my account balance

Scenario: A customer transfer money from account to another
    Given I am a customer
    When I choose the from account
    And I choose the target account with uuid
    Then it transfer from the first account to the second

Scenario: A customer remove an existing account
  Given I am a customer
  And I remove an existing account
  When this account have no money
  Then it remove this account

