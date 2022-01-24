@v2
Feature: Creating a bank

Scenario: A bank can be created
    Given I am an Admin
    When I create a new bank named LaBanque
    Then a Bank named LaBanque exist
    And it has no customers

Scenario: A bank can have customers
  Given I am an Admin
  When I create a new customer named LeClient
  Then a Customer named LeClient exist
  And it has no account

Scenario: A bank can have several customers
    Given I am an Admin
    When I create a new customer named LeClient
    And I create another new customer named LeBron
    Then 2 customers is created

  Scenario: A bank delete a customer
    Given I am an Admin
    When I delete an existing customer
    Then this customer is deleted