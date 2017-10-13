Feature: Use the website to change how search results are displayed
    So that I can select my yellow t shirts
    As an Australian customer
    I want to be able to add a yellow shirt to my basket

    Scenario: Add a yellow shirt to my basket
        Given I want to order a shirt
        Then I search for yellow t shirts in the Australian store
        When I choose a yellow t shirt
        Then I add it to my basket