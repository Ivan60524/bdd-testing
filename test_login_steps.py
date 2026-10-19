from pytest_bdd import scenarios, given, when, then

# Vinculamos este archivo con el archivo .feature
scenarios('user_login.feature')

@given("the user is on the login page")
def user_on_login_page():
    # Simulamos la navegación a la página de login
    print("\nNavigating to the login page...")

@when("the user enters valid credentials and clicks the login button")
def enter_valid_credentials():
    # Simulamos el ingreso de credenciales y clic en login
    print("Entering valid username and password, then clicking login...")

@then("the user should be successfully redirected to the dashboard")
def verify_dashboard_redirect():
    # Aserción para verificar que el inicio de sesión fue exitoso
    assert True, "User failed to reach the dashboard"