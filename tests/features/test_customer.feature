@v2
Feature: Creating new Customer

  Scenario: A customer can be created
    Given Customer is newly created
    When I create a new Customer name Brice
    Then a Customer named Brice exists

  Scenario: A customer can have a Current Account
    Given A customer can have a current account
    When The customer have a bank
    Then The customer have a current account with 0

  Scenario: A customer can have a Saving Account
    Given A customer can have a saving account
    When The customer have a bank
    Then The customer have a saving account with 0

  Scenario: A customer can transfer money with his two account
    Given A customer transfer money
    When The customer have a current and saving account
    Then The customer transfer 10€ from his current account to his saving account

  Scenario: A customer can transfer money to another people
    Given A customer tranfer money
    When The customer have a bank
    And The customer have the uuid of the account to transfer
    Then The customer transfer 10€ to the uuid account