# Created by noahs at 11/12/2023
Feature: CLASS tests for product page
  repeat of class test

  Scenario: User can select colors
    Given Open target product A-88062531 page
    Then Verify user can click through colors


  Scenario: User can add a product to cart
    Given Open target main page
    When Search for nintendo switch controller
    And Click on Add to Cart button
    And Store product name
    And Open cart page
    Then Verify cart has 1 item(s)