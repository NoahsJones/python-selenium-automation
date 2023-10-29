# Created by noahsj at 10/28/2023
Feature: Search tests
  Finding a product on targets website for lesson 3 hw

  Scenario: Verify user can search for a product.
    Given Open target main page
    When Search for product
    Then Verify search worked
    And Verify search result url
