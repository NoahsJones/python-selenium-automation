# Created by noahs at 11/5/2023
Feature: Target Circle
  # Enter feature description here

  Scenario: Verify that target circle has all benefit boxes
    Given Open target main page
    When Click on target circle
    Then Verify 5 benefit boxes display


  Scenario: User can click through circle tabs
    Given Open target circle page
    Then Verify clicking through Circle tab works


  Scenario: User is able to navigate to Google Play Target page
    Given Open target circle page
    And Store original window
    When Click Google Play button
    And Switch to new window
    Then Verify Google Play Target page opened
    And Close current page
    And Return to original window