# Created by Nicolas Marette at 24/01/2022
@v2
Feature: Transfer money to an account to an other

  Background:
    Given An account with an certain uuid

  Scenario: A bank can transferred moneys
    When I try to transfer money
    Then The new account received the money
