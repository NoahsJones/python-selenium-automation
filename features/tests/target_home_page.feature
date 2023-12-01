# Created by noahs at 11/6/2023
Feature: Home page of Target
  # Enter feature description here

  @smoke
  Scenario: Header has correct amount of UI elements
    Given Open target main page
    Then Verify header is present
    And Verify header has 5 links


  Scenario: User can see signin arrow
    Given Open target main page
    When Hover over signin
    Then Verify signin arrow shown
