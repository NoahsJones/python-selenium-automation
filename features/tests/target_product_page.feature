# Created by noahs at 11/13/2023
Feature: Target product page
  # Enter feature description here

  Scenario Outline: Verify that all products on product page have title and image
    Given Open target main page
    When Search for <product>
    Then target verify product title and image
    Examples:
    |product                 |
#    |Coffee                  |
#    |Airpods                 |
    |AirPods (3rd Generation)|
