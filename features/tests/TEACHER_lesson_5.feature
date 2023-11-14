Feature: Tests for product page

  Scenario: TEACHER User can select colors
    Given TEACHER Open target product A-88062531 page
    Then TEACHER Verify user can click through colors



  Scenario: TEACHER User can add a product to cart
    Given Open target main page
    When Search for AirPods (3rd Generation)
    And TEACHER Click on Add to Cart button
    And TEACHER Store product name
    And TEACHER Open cart page
    Then TEACHER Verify cart has 1 item(s)
    And TEACHER Verify cart has correct product