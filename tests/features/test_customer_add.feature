@v2
Feature: Adding new custumer to a bank.

Scenario: A new customer is create
  Given I am an Administrator
  When I create new customer named Customer
  Then a new Customer named Customer exists

Scenario: A customer is add in bank
  Given I am an Administrator
  Then I add my custumer to a bank