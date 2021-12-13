# Create by Raul Pulido at 12/11/2021
Feature: Register new user

    Scenario: New user Register
        Given I am going to Fortune Teller website
        When I click on Register Menu option
        Then A registration form display 
        Then I type the information and register a new user
       