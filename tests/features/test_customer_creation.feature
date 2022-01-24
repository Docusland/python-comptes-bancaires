@v2
Feature: check if bank exist and if there are clients in.

Scenario: Valid bank exist
    Given Bank is newly created
    When I name a bank 'Crédit Mutuel'
    Then Bank names 'Crédit Mutuel'