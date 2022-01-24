# Created by Nicolas Marette at 24/01/2022
@v2
Feature: Create a new bank

  Background:
    Given I am an administrator

  Scenario: A bank can be created
    When I create a new bank named Goodbank
    Then A bank named Goodbank exists
    And It has no customers
