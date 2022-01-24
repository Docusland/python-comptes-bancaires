Feature: Deletion a customer bank

  Scenario: Deletion a customer bank by name
    Given A customer bank already exist
    When I delete a customer bank
    Then A customer bank is deleted


