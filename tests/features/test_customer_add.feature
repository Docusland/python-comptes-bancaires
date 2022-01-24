@v2
Feature: Adding new custumer to a bank.

Background:
  Given I own a bank named Superbank
  And I own some accounts

Scenario: A new customer is create
  Given I am an Administrator
  When I create new customer named Customer
  Then a new Customer named Client exists

Scenario: A customer is add in SuperBank bank
  Given I am an Administrator
  Then I add my custumer to SuperBank bank

Scenario: A customer is remove from SuperBank bank
  Given I am an administrator
  When I can remove a customer from SuperBank bank
  Then I remove a customer from SuperBank bank

Scenario: Check if an account can be remove
  Given I am an administrator
  When I check if an account is out of money
  Then an account could be remove
  If yes
  Then account can be remove
  If no
  Then account can't be remove