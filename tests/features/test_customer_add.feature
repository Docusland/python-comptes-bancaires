Feature: Add a bank customer

  Scenario: Creating new customer
    Given I am an Admin
    When I create a new bank customer named Roger
    Then A new customer "Roger" is Created
    And The bank has a customer

  Scenario: Creating several customers
    Given I am an Admin
    When I create a customer named Jean
    And I create a customer named Paul
    Then The bank has 2 customers