Feature: Use the website to change how search results are displayed
    So that I can select my yellow t shirts
    As an Australian customer
    I want to be able to save it for later

    Scenario: Save a yellow shirt for later
        Given I want to order a shirt
        Then I search for yellow t shirts in the Australian store
        When I choose a yellow t shirt
        Then I save it for later