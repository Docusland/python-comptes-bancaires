@v2
Feature: Create a bank

Background:
  Given I own a bank named SuperBank
  And I own a customer named Client

Scenario: Create a new bank
  Given I am an Administrator
  When I create a new bank named SuperBank
  Then a Bank named SuperBank exists
  And It has no customers

Scenario: See the customer list of the bank
  Given I am an Administrator
  When I display the customer list of the bank
  Then a list of customer is displayed

Scenario: Want to transfer money from account to another account uuid
  Given I am a Customer named Client
  When I send money to other account with uuid account number
  Then source account decrease money and other account earn

Scenario: Search customer by uuid
  Given I am an administrator
  When I search customer in customer list of Superbank Bank
  And I compare the uuid of the customer with the customer uuid list
  Then I should find a customer
  If yes
  Then a customer is find
  Else
  Then there is no customer with this uuid

Scenario: Search customer by name
  Given I am an administrator
  When I search customer in customer list of Superbank Bank
  And I compare the name of the customer with the customer name list
  Then I should find a customer
  If yes
  Then a customer is find
  Else
  Then there is no customer with this uuid