@bank
Feature: remove bank

    Scenario: I cannot delete a bank with an invalid name
    Given I am an administrator
    When I try to delete the Giangrande Family bank
    Then the system raises an exception

  Scenario: i delete a bank with a correct name
    Given I am a administrator
    When I've found the name and i delete the bank
    Then I return the bank was deleted
