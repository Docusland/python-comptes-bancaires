@v2

Feature: Finding a customer

Background:
  Given I am a Customer named Theo JOUAN
  And I am a Customer of the TestBank
  And I own a SavingAccount
  And I own a CurrentAccount

Scenario: A bank can find a customer by customer name