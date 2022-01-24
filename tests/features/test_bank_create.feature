# Created by Linh Chi at 24/01/2022
@v2
Feature: Creating a bank

  Scenario: A bank can be created
    Given I am an Administrator
    When I create a new bank named TurfuBank
    Then a bank named TurfuBank exists
      And it has no customers

  Scenario: A bank has no name
    Given I am an Administrator
    When I create a new bank with no name
    Then a bank is not created