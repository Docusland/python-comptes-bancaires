# Created by Nicolas Marette at 24/01/2022
@v2
Feature: Delete an existing bank

  Background:
    Given a bank named Goodbank exists
    And I am an administrator

  Scenario: A bank can be delete
    When I delete a bank named Goodbank
    Then A bank named Goodbank doesn't exists