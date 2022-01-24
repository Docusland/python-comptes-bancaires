@bank
Feature: Create a bank

Scenario: Create a new bank
  Given I open a new bank
  When I create a new bank named SuperBank
  Then a Bank named SuperBank exists
  And It has no customers