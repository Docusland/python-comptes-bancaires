@v2
  Feature: Creating a customer

    Scenario: A Customer can be created
      Given I am an Employee of the Bank named BabyBank
      When I create a customer named CustomerA
      Then A customer named CustomerA exist

    Scenario: Customer already exist
      Given I am an Employee of the Bank named BabyBank
      When I check if Customer named Customer01 exist
      Then Customer named Customer01 exist

    Scenario: An existing Customer can be edited
      Given I am an Employee of the Bank named BabyBank
      When I edit a customer named CustomerA
      And change his name by CustomerAA
      Then A customer named CustomerA is replace by CustomerAA

    Scenario: A existing Customer can be delete
      Given I am an Employee of the Bank named BabyBank
      When I delete a customer named CustomerAA
      Then A customer named CustomerAA is delete