@customer
Feature: delete customer
  Scenario: I cannot delete a customer with an invalid name
    Given I am an administrator
    When I try to delete a void or an invalid name of customer
    Then the system raises an exception

  Scenario: i delete a customer with a correct name
    Given I am a administrator
    When I've found the name and i delete the customer
    Then I return the customer was deleted

