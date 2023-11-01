# Created by noahsj at 10/30/2023
Feature: Add to Cart
  This feature allows users to add items to their cart for later purchase.

  Scenario: Verify sprouts products can be added to cart
    Given open sprouts main page
    When sprouts search product
    And sprouts select the product
    And sprouts add product to cart
    And sprouts navigate to cart
    Then sprouts verify product is in cart
