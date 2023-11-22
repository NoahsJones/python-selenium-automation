# Created by noahsj at 10/28/2023
Feature: Test for targets sign in page
  Testing targets sign in page for lesson 3 hw

  Scenario: Verify that logged out users can access Sign-in page
    Given Open target main page
    When Click sign in
    And Under navigation menu, click sign in
    Then Sign in form opened


  Scenario: Verify a user can successfully sign in
    Given Open target main page
    When Click sign in
    And Under navigation menu, click sign in
    And Input user credentials email: leverichm@stamberg.nl password: ********
    Then Verify user is logged in



  Scenario: User can open and close Terms and Conditions from sign in page
    #Given target Open sign in page ..... this was not working so I had to lengthen my test preconditions. However, it works the same
    Given Open target main page
    When Click sign in
    And Under navigation menu, click sign in
    And Store original windows
    When Click on Target terms and conditions link
    And Switch to the newly opened window
    Then Verify Terms and Conditions page is opened
    And User can close new window and switch back to original



