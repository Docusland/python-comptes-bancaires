# Created by Nicolas Marette at 24/01/2022
@v2
Feature: Manage a customer account

  Background:
    Given Into the bank
    And A customer named John Doe

  Scenario: A customer add an account
    When A customer create an account
    Then The account has no money

  Scenario: Verify that an account can be removed
    When Verify an account balance
    Then An account has nothing

  Scenario: A customer remove an account
    When A customer delete his account
    Then The account doesn't exists