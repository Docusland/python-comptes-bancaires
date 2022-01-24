@cc
Feature: Adding and removing money from a Compte Courant.
 @skip
Scenario: Valid CC keeps money I inject
    Given CC is newly created
    When I add 10€
    Then CC holds 10€
 @skip
Scenario: Simply removing cash
    Given I have an existing CC with 10€
    When I withdraw 10€
    Then CC holds 0€
 @skip
Scenario: Generate agios with overdraft authorization
    Given CC is newly created
    And I have an overdraft authorization with a 10% agios
    When I withdraw 10€
    Then CC holds -11€

 @skip
Scenario: Skip agios with overdraft authorization
    Given CC is newly created
    And I have an overdraft authorization with a 10% agios
    When I add 100€
    And I withdraw 10€
    Then CC holds 90€

 @skip
 Scenario: Next feature : It is possible to close an account.
    Given CC is newly created
    And I add 100€
    When I want to close my account
    Then the bank refunds me of 100€