@bank
Feature: create bank

  Scenario: I try to create a bank with an empty name
    Given I am an administrator
    Then I cannot create a bank with an empty name

  Scenario: I try to create a bank with a invalid name
    Given I am an administrator
     When a bank named Giangrande exists
    Then I cannot create a bank with the name Giangrande

  Scenario: I create a bank with a valid name
    Given I am an administrator
    When I select a valid name to create my organisation
    Then I return "the organisation was successfully created"

  Scenario: I search a bank with a valid name
    When The name selected is exist in the list of bank
    Then I return the information about this bank

  Scenario: I search a bank with an invalid name
    When The name selected is void or already took
    Then The system raise an exception

