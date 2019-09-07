# -*- coding: utf-8 -*-
import os,sys,unittest,requests,sys
if os.getcwd() not in sys.path:
   sys.path.insert(0,os.getcwd())
from tests_methods import methods,project_settings,opencv
from selenium import webdriver
from time import sleep
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

browsers=project_settings.browsers
test_name=__file__.rstrip('cd').split("/")[-1][:-3] if sys.platform=="darwin" else __file__.rstrip('cd').split("\\")[-1][:-3]   
MyTest=project_settings.ProjectSettings(test_name)
project_settings.running_test.name=test_name
test_type=project_settings.running_test()
test_part=MyTest.test_parameters[0]
locator_folder=MyTest.project_folders[4][1:]
locator_name=MyTest.test_parameters[1]

class TESTMETA(type):
      def __new__(mcs, name, bases, dict):
          def test_generator(browser):
              def test(self):
                  # instantiate Web class from methods.py module
                  self.Web=methods.Web(test_name)
                  self.item = self.Web.set_webdriver_path(browser)
                  if self.item:
                     if test_type == 'LOCAL':
                        self.driver=self.Web.get_driver(browser)
                     if test_type == 'CBT':
                        from CBT import CBTLogin
                        self.api_session = requests.Session()
                        self.api_session.auth = (CBTLogin(browser).username, CBTLogin(browser).authkey)
                        self.driver = webdriver.Remote(desired_capabilities=self.item,command_executor='http://%s:%s@hub.crossbrowsertesting.com:80/wd/hub' % (CBTLogin(browser).username, CBTLogin(browser).authkey))
                     project_settings.running_test.browser = browser
                     self.locator= self.Web.import_module(locator_folder,locator_name)
                     try:
                         print 'This is : '+test_name+' , '+test_type+' , '+test_part+' , '+browser.upper()
                     except TypeError:
                            raise AssertionError('Test name incorrect ! ==> project_settings.py')
                     try:
                         self.Web.test(test_name,self.driver,self.locator,browser)
                         if test_type == 'CBT':
                            print 'Taking snapshot'
                            self.snapshot_hash = self.api_session.post('https://crossbrowsertesting.com/api/v3/selenium/' + self.driver.session_id + '/snapshots').json()['hash']
                         self.test_result = 'pass'
                     except AssertionError as e:
                            if test_type == 'LOCAL':
                               print 'Error : ' + str(e)
                            if test_type == 'CBT':
                               self.snapshot_hash = self.api_session.post('https://crossbrowsertesting.com/api/v3/selenium/' + self.driver.session_id + '/snapshots').json()['hash']
                               self.api_session.put('https://crossbrowsertesting.com/api/v3/selenium/' + self.driver.session_id + '/snapshots/' + self.snapshot_hash,
                               data={'description': 'AssertionError: ' + str(e)})    
                            self.test_result = 'fail'
                            raise
              return test

          for browser in browsers:
              my_test = "test_%s"%browser.replace(" ","_")
              dict[my_test] = test_generator(browser)
          return type.__new__(mcs,name,bases,dict)      

class TEST(unittest.TestCase):
      __metaclass__ = TESTMETA
       
      def setUp(self):
          self.test_result = None
          self.driver = None

      def tearDown(self):
          if self.test_result is not None:
             if test_type == 'LOCAL':
                print 'score: ', self.test_result
                if project_settings.running_test.browser in ("safari desktop mac","firefox desktop mac","edge desktop win","ie desktop win"):    
                   print 'Quit browser !'
                   for proc in psutil.process_iter(): 
                       if project_settings.running_test.browser.split(" ")[0] in proc.name():  
                          proc.kill()
                          break
                else:
                     if self.driver:
                        print "Quit driver !"
                        self.driver.quit()          
             if test_type == 'CBT':
                print 'Done with session %s'% self.driver.session_id
                self.api_session.put('https://crossbrowsertesting.com/api/v3/selenium/'+self.driver.session_id,
                data={'action': 'set_score', 'score': self.test_result})
                self.api_session.delete('https://crossbrowsertesting.com/api/v3/selenium/'+self.driver.session_id)

if __name__ == '__main__':
   unittest.main()        
