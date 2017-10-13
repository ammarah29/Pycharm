Feature: Use the website to find shirts
        So that I can order a shirt
        As a customer
        I want to be able to find t shirts

    Scenario: Search for t shirts
        Given I want to order a shirt
        When I search for purple t shirts
        Then I should see some purple t shirts