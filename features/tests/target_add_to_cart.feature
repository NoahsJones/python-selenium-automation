# Created by noahs at 11/5/2023
Feature: Add a Product to Cart
  A product can be searched, found, and added to a users cart successfully.

  Scenario: Verify a product can be added to cart
    Given Open target main page
    When target search for coffee
    And target add coffee to cart
    Then target verify Coffee in cart