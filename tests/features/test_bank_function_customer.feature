
Feature: Add a client in a bank
Background:
    Given I am a bank named "Crédit Mutuel"

Scenario: Add client in bank
    Given I am a customer named "Toto"
    When I add this customer in the customer's list
    Then "Toto" is in the customer's list

Scenario: Remove client in bank
    Given I am a customer named "Toto"
    When I remove this customer in the customer's list
    Then "Toto" is out the customer's list

