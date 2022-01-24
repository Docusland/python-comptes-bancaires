@v2
Feature: check if customer exist.

Scenario: Valid customer exist
    Given Customer is newly created
    When I name a customer named 'Toto'
    Then Customer names is 'Toto'