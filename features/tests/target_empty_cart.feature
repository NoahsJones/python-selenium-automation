# Created by noahsj at 10/28/2023
Feature: Test for targets empty cart
  testing targets empty cart feature for lesson 3 hw

  Scenario: Verify that cart displays it is empty
    Given Open target main page
    When Click on Cart icon
    Then Message displays 'Cart is empty'


