@pv2

Feature: Create a bank

Scenario: A bank can be created
    Given Bank is newly created
    When I want to create a Bank
    Then The bank is created

Feature: Remove a bank

Scenario: A bank can be removed
    Given Bank is removed
    When I want to remove a bank
    Then The bank is removed

