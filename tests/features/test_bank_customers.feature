# Created by Nicolas Marette at 24/01/2022
@v2
Feature: Manage an customer bank

  Background:
    Given I am an administrator

  Scenario: A bank can found a customer by an uuid
    When I try to find a customer (John Doe) list with an uuid parameter
    Then I find John Doe

  Scenario: A bank can found a customer by a customer name
    When I try to find a customer (John Doe) list with a name parameter
    Then I find John Doe

  Scenario: A bank can added a customer
    When I add a new customer
    Then I can read the customer into the existing customers list

  Scenario: A bank can removed a customer
    When I removed an existing customer
    Then I can't read the deleting customer into the customers list