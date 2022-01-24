Feature: Search customer bank

  Scenario: Find customer by savings account uuid
    Given I know the CE uuid of my customer
    When I search the customer by this uuid
    Then A customer is found

  Scenario: Find customer by current account uuid
    Given I know the CC uuid of my customer
    When I search the customer by this uuid
    Then A customer is found

  Scenario: Find customer by customer name
    Given I am an Admin
    When I search a customer by a name
    Then A customer is found

