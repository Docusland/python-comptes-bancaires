@v2
  Feature: Creating a bank

    Scenario: A bank can be created
      Given I am an Administrator
      When I create a new bank name Banque
      Then a Bank named Banque exists
      And it has no customers

    Scenario: A bank can have one customer
      Given I am an employees in Banque bank
      When I add a new customer name Brice
      Then The bank have one customer

    Scenario: A bank can have 2 customers
      Given I am an employees in Banque bank
      When I add a new customer name Brice
      And I add a new customer name Roger
      Then The bank have two customers

    Scenario: A bank can remove one customer
      Given I am an employees in Banque bank
      When I add a new customer name Brice
      And The customer have 0 on his accounts
      Then The bank have one customer remove
