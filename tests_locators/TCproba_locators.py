from tests_methods import project_settings
test_name = project_settings.running_test.name
MyTest = project_settings.ProjectSettings(test_name)
test_part = MyTest.test_parameters[0]
browser = project_settings.running_test.browser
url_player_desktop = 'https://testing.perfectforms.com:98'

def get_elements(browser):
    if 'desktop' in browser:
        user = 'daniell@perfectforms.com'
        passw = 'qqqqqq'
        Elog = [{'source': 'url', 'url': url_player_desktop},
         {'source': 'textctrl', 'source_name': 'Email', 'source_locator_type': 'name', 'source_locator_string': 'userName', 'source_tool': 'selenium', 
            'source_click': 1, 'source_clear': 1, 'source_change': 1, 'source_changed_value': user},
         {'source': 'textctrl', 'source_name': 'Password', 'source_locator_type': 'name', 'source_locator_string': 'password', 'source_tool': 'selenium', 
            'source_click': 1, 'source_clear': 1, 'source_change': 1, 'source_changed_value': passw},
         {'source': 'btn', 'source_name': 'Login', 'source_locator_type': 'id', 'source_locator_string': 'loginSubmit', 'source_tool': 'selenium', 
            'source_click': 1, 'source_check': 0, 'source_change': 0}]
        if test_part == 'full test' or test_part == 'part1':
            E = [
             Elog]
    return E
