Feature: Add a account to a customer
Background:
    Given I am a customer named "Toto"

Scenario: Add account to a customer
    Given I have an account
    When I add an account in the account's list
    Then This account is in the account's list