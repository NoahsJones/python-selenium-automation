# Created by noahsj at 10/31/2023
Feature: Add to Cart on Amazon
  This feature allows users to add items to their cart for later purchase.

  Scenario: Verify amazon products can be added to cart
    Given open amazon main page
    When amazon search product
    And amazon select the product
    And amazon add product to cart
    And amazon navigate to cart
    Then amazon verify product is in cart