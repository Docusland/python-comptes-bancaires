@v2
Feature: Creating a bank.

Scenario: A Bank can be created.
    Given I am an Admin
    When I create a new bank named Westpac
    Then a Bank named Westpac exists
    And it has 0 Customers