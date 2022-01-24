# Created by Linh Chi at 24/01/2022
@v2
Feature: Accessing a bank

  Scenario: A bank can be accessed
    Given I am an Administrator
    When I access a bank data
    Then I get data from bank

    Scenario: A bank cannot be accessed
      Given I am not Administrator
      Then I don't get data from bank
