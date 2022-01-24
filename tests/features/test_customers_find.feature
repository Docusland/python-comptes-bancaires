@v2
Feature: Search a customer

Background:
  Given I am a Customer named LeClient
    And I am a Customer of the bank LaBanque
    And I have an CurrentAccount
    And I have an SavingsAccount

Scenario: A bank can find a customer with his account uuid
  Given I am an Admin
  When I search for a customer with one of his account uuid
  Then I see information about this customer

Scenario: A bank can find a customer by name
    Given I am an Admin
    When I search for a customer with his name
    Then I see information about this customer