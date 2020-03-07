Feature: Echo Server

    Scenario: Make an echo request
        Given the message "hello world"
        When I make a post to "/echo/send-message"
        Then there should be a message saying "hello world"
         and the status code should be 200
    
    Scenario: Send a get instead of post
        When I make a get to "/echo/send-message"
        Then the status code should be 405