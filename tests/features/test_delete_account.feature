# Created by mon78 at 24/01/2022
Feature: Delete an account

  Scenario: An account can be deleted
    Given I am an employed of the bank named inserericiunnomdebankoriginal
    And A customer named inserericiunnomoriginal exist
    And A customer named inserericiunnomoriginal don't have more money than 0€
    When I Delete a customer named inserericiunnomoriginal for the bank named inserericiunnomdebankoriginal
    Then A customer named inserericiunnomoriginal was deleted for inserericiunnomdebankoriginal
    And inserericiunnomdebankoriginal have 1 less customer
    And inserericiunmonoriginal doesn't exist anymore
