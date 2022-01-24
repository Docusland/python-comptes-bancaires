# Created by Nicolas Marette at 24/01/2022
@v2
Feature: Create a new Customer

  Background:
    Given Into the bank
    And I am an administrator

  Scenario: A customer can be created
    When I create a new customer named John Doe
    Then A customer named John Doe exists
