@v2
Feature: Add a customer, check customer_bank, customer has Compte, CompteCourant and CompteEpargne.

  Scenario: Add a Customer
    Given Customer is newly created
    When I add TOTO
    Then Customer has been created with name=TOTO

  Scenario: Customer has CurrentAccount
    Given Create an CurrentAccount for a new Customer
    When I add 10€
    Then CurrentAccount holds 10€

  Scenario: Customer has SavingsAccount
    Given Create an SavingsAccount for a new Customer
    When I add 10€
    Then SavingsAccount holds 10€

    #TODO
  Scenario: Check if Customer has bank
    Given i add a new bank to a Customer
    Then A Customer has a bank.name

