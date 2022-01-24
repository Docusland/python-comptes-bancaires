@customer
Feature: Adding new custumer to a bank.

Scenario: A new customer is adding in bank
  Given I am a customer looking for a bank
  When I create new customer named Customer
  Then a new Customer named Customer exists
  And the bank has one customer