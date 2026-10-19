Feature: User Authentication
  As a registered system user
  I want to log into the application with my credentials
  So that I can securely access my dashboard

  Scenario: Successful login with valid credentials
    Given the user is on the login page
    When the user enters valid credentials and clicks the login button
    Then the user should be successfully redirected to the dashboard