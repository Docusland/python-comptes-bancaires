@customer
Feature: add any customer

  Scenario: I try to create a customer with a invalid name
    Given I am an administrator
    When The name selected is void or already took
    Then The system raise an exception

  Scenario: I create a customer with a valid name
    Given I am an administrator
    When I select a valid name to create my organisation
    Then I return "the organisation was successfully created"