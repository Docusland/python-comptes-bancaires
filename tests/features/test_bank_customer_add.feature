@v2
Feature: Add a client in a bank
Background:
    Given I am a bank named "Crédit Mutuel"

Scenario: A customer can be add to the bank
    Given I am a bank named "Crédit Mutuel"
    Then I can add a customer to this bank

