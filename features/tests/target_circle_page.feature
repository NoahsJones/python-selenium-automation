# Created by noahs at 11/5/2023
Feature: Target Circle
  # Enter feature description here

  Scenario: Verify that target circle has all benefit boxes
    Given Open target main page
    When Click on target circle
    Then Verify 5 benefit boxes display
