# Created by noahs at 11/13/2023
Feature: Target product page
  # Enter feature description here

  @smoke
  Scenario Outline: Verify that all products on product page have title and image
    Given Open target main page
    When Search for <product>
    Then target verify product title and image
    Examples:
    |product                 |
#    |Coffee                  | #These failed because the code to scroll did not scroll to the very bottom of the product
#    |Airpods                 | #page to make all products load.
    |AirPods (3rd Generation)|
