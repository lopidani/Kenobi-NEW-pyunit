import sys
platform=sys.platform

browsers=["chrome desktop mac","safari desktop mac","firefox desktop mac","chrome desktop win","firefox desktop win","ie desktop win","edge desktop win",
"chrome phone android 7","chrome phone android 8","chrome phone android 9","safari phone ios 12",
"safari phone ios 11","safari phone ios 10","safari tablet ios","chrome tablet android"]

class ProjectSettings(object):
      def __init__(self,test_name):
          self.test_name=test_name 
    
      @property
      def project_folders(self):
          if platform=="win32":self.tests_methods="\\tests_methods";self.tests_screenshots="\\tests_screenshots";\
             self.tests_webdrivers="\\tests_webdrivers\\win";self.test_screenshots=self.tests_screenshots+"\\"+self.test_name;\
             self.tests_locators="\\tests_locators"  
          elif platform=="darwin":self.tests_methods="/tests_methods";self.tests_screenshots="/tests_screenshots";\
               self.tests_webdrivers="/tests_webdrivers/mac";self.test_screenshots=self.tests_screenshots+"/"+self.test_name;\
               self.tests_locators="/tests_locators"  
          return self.tests_methods,self.tests_webdrivers,self.tests_screenshots,\
                 self.test_screenshots,self.tests_locators       

      @property
      def test_parameters(self):
          if self.test_name=="TC_proba":self.test_part="full test";self.test_locator="TCproba_locators"
          if self.test_name=="TC_Beh_Integration_Form_CMandatory":self.test_part="full test";self.test_locator="bh_cmandatory_locators" 
          if self.test_name=="TC_scroll_test":self.test_part="full test";self.test_locator="scroll_test_locators"           
          if self.test_name=="TC_Call_JavaScript_player":self.test_part="full test";self.test_locator="TCCallJavaScript_locators"               
          return self.test_part,self.test_locator

def running_test():
    name=""
    browser=""
    test_type="LOCAL"
    #self.test_type="CBT"
    return test_type
