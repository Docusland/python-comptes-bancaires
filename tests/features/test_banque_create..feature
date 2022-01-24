# Created by mon78 at 24/01/2022
Feature: Creating a bank

  Scenario: A bank can be created
    Given I am an Administrator
    And A customer named inserericiunnomdebankoriginal does'nt exist
    When I create a bank named inserericiunnomdebankoriginal
    Then I bank name inserericiunnomdebankoriginal was created
    And inserericiunnondebankoriginal have 0 customer