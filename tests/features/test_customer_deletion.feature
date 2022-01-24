# Created by Nicolas Marette at 24/01/2022
@v2
Feature: Delete an existing customer
  Background:
    Given a customer named John Doe exists

  Scenario: A customer can be delete
    Given I am an administrator
    Then I delete a customer named John Doe
    And A customer named John Doe doesn't exists