Feature: Send Email with Message

    Scenario: Make a send email request
        Given the message "hello world"
          and the email address "foobar@helloworld.io"
         When I make a post to "/echo/send-email"
         Then the status code should be 201
    
    Scenario: Send a get instead of post
         When I make a get to "/echo/send-email"
         Then the status code should be 405