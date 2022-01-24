# Created by Linh Chi at 24/01/2022
@v2
Feature: Creating a current account

  Scenario: An account can be created
    Given I am an Administrator
      And a customer named Jean-Michel exists
    When I create a current account to customer Jean-Michel
    Then a current account is created
      And a customer named Jean-Michel has current account
