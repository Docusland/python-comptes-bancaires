Feature: New bank


  Scenario: Creating new bank
    Given I am an Admin
    When I create a new bank named SquirrelBank
    Then A bank named SquirrelBank exists
    And It has 0 Customer






