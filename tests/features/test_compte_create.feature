# Created by mon78 at 24/01/2022
Feature: Creating a customer

  Scenario: A customer can be created
    Given I am an employed of the bank named inserericiunnomdebankoriginal
    And A customer named inserericiunnomoriginal does'nt exist
    When I create a customer named inserericiunnomoriginal for inserericiunnomdebankoriginal
    Then A customer named inserericiunnomoriginal was create for
    And inserericiunnomoriginal have 1 more customer
