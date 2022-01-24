@v2
Feature Creating a bank

Scenario: A bank can be created
    Given I create a new bank named TestBank
    Then a bank named TestBank exists
    And has many customers

