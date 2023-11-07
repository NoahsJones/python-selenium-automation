# Created by noahs at 11/5/2023
Feature: Target Help page
  # Enter feature description here

  Scenario: Verify UI elements appear on Help page
    #Given Open target main page
    #When target navigate to Help page
    Given Open target help page
    Then target verify 14 UI elements exist