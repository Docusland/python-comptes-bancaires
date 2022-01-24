@pv2
Feature: Add an account

Scenario: A user can have an account
    Given I am a customer of the bank
    When I ask to the bank to create an account
    Then The customer have a new account