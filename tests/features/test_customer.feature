@v2
Feature: Adding new custumer to a bank.

Background:
  Given an administrator
  And I own some accounts

Scenario: A new customer is create
  Given I want to create a customer
  When I create new customer named Customer
  Then a new Customer named Client exists

Scenario: An account is add to customer account list
  Given I want to open an account
  Then I add an account

Scenario: An account is remove account list
  Given I want to remove an account from customer's account list
  When I can remove an account to customer
  Then I remove an account

Scenario: Check if an account can be remove
  Given I remove an account from customer's account list
  When I check if an account is out of money
  Then an account could be remove
  If yes
  Then account can be remove
  If no
  Then account can't be remove