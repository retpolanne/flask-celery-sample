Feature: Send Mail with Message

    Scenario: Make a send mail request
        Given the message "hello world"
          and the email address "foobar@helloworld.io"
         When I make a post to "/echo/send-mail"
         Then the status code should be 201
          and the task "send_mail" should be scheduled
    
    Scenario: Send a get instead of post
         When I make a get to "/echo/send-mail"
         Then the status code should be 405