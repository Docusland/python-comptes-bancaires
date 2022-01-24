@customer
Feature: search customer
  Scenario: I search a customer with a valid name
    When The name selected is exist in the list of customer
    Then I return the information about this customer

  Scenario: I search a customer with an invalid name
    When The name selected is void or already took
    Then The system raise an exception

