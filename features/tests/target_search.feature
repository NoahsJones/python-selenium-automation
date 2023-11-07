# Created by noahsj at 10/28/2023
Feature: Search tests
  Finding a product on targets website for lesson 3 hw

  Scenario: Verify user can search for coffee.
    Given Open target main page
    When Search for coffee
    Then Verify search worked for coffee
    And Verify coffee in search result url


  Scenario: User can search for tea
    Given Open target main page
    When Search for tea
    Then Verify search worked for tea
    And Verify tea in search result url


  Scenario: User can search for Christmas Decorations
    Given Open target main page
    When Search for Christmas Decorations
    Then Verify search worked for Christmas Decorations
    And Verify Christmas+Decorations in search result url


  Scenario Outline: Verify products can be searched.
    Given Open target main page
    When target search for <product>
    Then target verify <product_result> is found
    And Verify <product_url> in search result url
    Examples:
    |product              |product_result       |product_url          |
    |coffee               |Coffee               |coffee               |
    |fruit                |Fruit                |fruit                |
    |shovel               |Shovel               |shovel               |
    |mug                  |mug                  |mug                  |
    |Christmas Decorations|Christmas Decorations|Christmas+Decorations|