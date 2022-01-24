@v2
Feature: Create a bank

Scenario: Create a new bank
  Given I am an Administrator
  When I create a new bank named SuperBank
  Then a Bank named SuperBank exists
  And It has no customers

Scenario: See the customer list of the bank
  Given I am an Administrator
  When I display the customer list of the bank
  Then a list of customer is displayed
