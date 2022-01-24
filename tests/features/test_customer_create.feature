# Created by Linh Chi at 24/01/2022
@v2
Feature: Creating a customer

#  feature finding a customer
#  Background:
#    Given  I am a Customer named xxx
#    And I am a customer of the bank xxx
#    And I own a SavingsAccount
#    And I own a CurrentAccount

  Scenario: A customer can be created
    Given a bank named TurfuBank exists
      And I am an Administrator
    When I create a customer named Jean-Michel
      And I add them to TurfuBank
    Then a customer named Jean-Michel exists
      And the bank named TurfuBank has customer named Jean-Michel amongst its customers
      And they have bank TurfuBank
      And they have no accounts

  Scenario: A customer has no name
    Given a bank named TurfuBank exists
      And I am an Administrator
    When I create a customer with no name
    Then a customer is not created

  Scenario: The bank does not exist
    Given a bank named TurfuBank does not exist
      And I am an Administrator
    When I create a customer named Jean-Michel
