@cc
Feature: Adding and removing money from a Compte Epargne.

Scenario: Valid CE keeps money I inject
    Given CE is newly created
    When I add 10€
    Then CE holds 10€

Scenario: Simply removing cash
    Given I have an existing CE with 10€
    When I withdraw 10€
    Then CE holds 0€

Scenario: Apply interest to account
    Given this account Exist
    And this account was created at the same date and month
    When this interest was apply on this acconut
    Then apply inetrest

 @skip
 Scenario: Next feature : It is possible to close an account.
    Given CE is newly created
    And I add 100€
    When I want to close my account
    Then the bank refunds me of 100€