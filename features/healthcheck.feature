Feature: Healthcheck

    Scenario: Hit healthcheck
        When I make a get to "/healthcheck"
        Then there should be a message saying "ok"
         and the status code should be 200
