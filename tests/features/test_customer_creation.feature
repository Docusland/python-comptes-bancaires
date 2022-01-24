@v2
# Created by Arthur Ruby at 24/01/2022

Feature: Customer creation

  Background:
    Given I have an existing Bank named Westpac

  Scenario: A single Customer can be added to the Bank.
    Given I am an Admin at Westpac bank
    When I add a new Customer named Jean-Michel
    Then a new Customer named Jean-Michel exists
    And the Bank has 1 Customer

  Scenario: Multiple Customers can be added to the Bank.
    Given I am an Admin at Westpac bank
    When I add a new Customer named Jean-Michel
    And I add another new Customer named Gisèle-Michèle
    Then the bank has 2 Customers