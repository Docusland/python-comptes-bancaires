@V2
Feature: Create a bank

Background:
  Given Im an employee from the bank named toto
  Then it has no customer

Scenario: Add a new customer to bank named toto
  Given I want to add a new customer named Bob
  Then there is now one customer named Bob
