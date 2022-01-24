@v2

Scenario: A bank can be created
  Given I am an Administrator
  When I create a Bank named BabyBank
  Then A Bank named BabyBank exist

Scenario: Bank already exist
  Given I am an Administrator
  When I check if Bank named BabyBank already exist
  Then A Bank named BabyBank exist

Scenario: An existing Bank can be editing
  Given I am an Administrator
  When I edit a Bank named BabyBank
  Then A Bank named BBank exist

Scenario: An existing Bank can be delete
  Given I am an Administrator
  When I delete a Bank named BBank
  Then A Bank named BBank is delete