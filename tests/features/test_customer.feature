@v2
Feature Create a Customer

    Scenario: A Customer can be created
    Given I created Customer named Theo JOUAN
    When Customer can create current account and saving account
    And Costumer can transfer money between an other account and customer


    Scenario: A Customer can consult his account balance
    Given Customer create an account
    When Customer can see his balance account

    Scenario:


    Scenario: A customer can closed his account