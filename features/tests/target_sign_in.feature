# Created by noahsj at 10/28/2023
Feature: Test for targets sign in page
  Testing targets sign in page for lesson 3 hw

  Scenario: Verify that logged out users can access Sign-in page
    Given Open target main page
    When Click sign in
    And Under navigation menu, click sign in
    Then Sign in form opened