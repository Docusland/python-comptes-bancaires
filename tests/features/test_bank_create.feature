@v2
Feature: add a Bank, add a customer to Bank

Scenario: Bank exists
    Given New Bank created
    When I add new Bank called CMB
    Then Bank called CMB has been created.

Scenario: Bank recently created has no costumers
    Given New CMB Bank created
    When I check Customers in CMB Bank
    Then CMB Bank has 0 customers