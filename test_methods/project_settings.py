import sys
test_part=test_name=locator_name=None
platform=sys.platform

def project_folders(test_name):
    if platform=="win32":python_modules_name="\\test_methods";screenshots_folder_name="\\test_screenshots";\
       webdrivers_folder_name="\\test_webdrivers\\win";test_screenshots_folder_name=screenshots_folder_name+"\\"+test_name
    elif platform=="darwin":python_modules_name="/test_modules";screenshots_folder_name="/test_screenshots";\
       webdrivers_folder_name="/test_webdrivers/mac";test_screenshots_folder_name=screenshots_folder_name+"/"+test_name  
    return python_modules_name,webdrivers_folder_name,screenshots_folder_name,test_screenshots_folder_name       

def tests_parameters(test_name):
    global test_part,locator_name
    if test_name=="TC_proba":test_part="full test";locator_name="TCproba_locators"
                                   
    return test_part,locator_name

def running_test():
    name=""
    browser=""
    test_type="LOCAL"
    #test_type="CBT"
    return test_type
