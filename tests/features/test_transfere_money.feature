# Created by mon78 at 24/01/2022
Feature: a client can transfere here money

  Scenario:
    Given trouverunautrenomdeclientoriginal exist
    And 5€ was less than lasommequejaisurmoncompte
    When I thransfer 5€ to trouverunautrenomdeclientoriginal
    Then J'ai 5€ less on my account
    And trouverunautrenomdeclientoriginal have 5€ more on this account
