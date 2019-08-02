# -*- coding: utf-8 -*-
import os,sys,importlib,opencv,requests,pyautogui
from time import sleep
from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
import project_settings
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.chrome.options import Options

# some initial datas      
platform=sys.platform
project_path=os.getcwd()
 
class Web(object):
      def __init__(self,test_name):
          self.test_name=test_name
          self.driver=None
          self.elem=None
     
      def set_webdriver_path(self,browser):              
          test_type=project_settings.running_test()
          if test_type=="LOCAL":
             if "desktop" in browser:
                if platform=="win32":
                   # names of webdrivers must be like below
                   if "chrome" in browser:webdr_name="\chromedriver2.43.exe"
                   elif "firefox" in browser:webdr_name="\geckodriver0.23.exe"  
                   elif "ie" in browser:webdr_name="\IEDriverServer64.exe" 
                   else:webdr_name=None
                elif platform=="darwin":
                     if "safari" in browser:webdr_name="/safaridriver"
                     elif "chrome" in browser:webdr_name="/chromedriver_75"
                     elif "firefox" in browser:webdr_name="/geckodriver_0.24"
                     else:webdr_name=None
                if webdr_name:
                   if platform=="win32":webdriver_path=self.define_working_folders(self.test_name)[1]+webdr_name   
                   elif platform=="darwin":
                      if "safari" in browser:webdriver_path="/usr/bin/safaridriver"
                      else:webdriver_path=self.define_working_folders(self.test_name)[1]+webdr_name      
                else:webdriver_path=None;raise AssertionError('For browser : '+browser+' we have no webdriver !')
                if webdriver_path:
                   return webdriver_path
   
      def get_driver(self,browser):
          webdriver_path=self.set_webdriver_path(browser)
          definition_error="""
 No correct deffinition of webdriver path ( chromedriver or geckodriver must be in webdriver path ) !
                         """ 
          if sys.platform=="win32":                 
             if "\chromedriver" in webdriver_path.lower() :br=webdriver.Chrome 
             elif "\geckodriver" in webdriver_path.lower() : br=webdriver.Firefox
             elif "\iedriverserver" in webdriver.path.lower(): br=webdriver.Ie 
             else : raise AssertionError(definition_error)      
          elif sys.platform=="darwin":
             if "/safaridriver" in webdriver_path.lower(): br=webdriver.Safari
             elif "/geckodriver" in webdriver_path.lower() : br=webdriver.Firefox 
             elif "/chromedriver" in webdriver_path.lower() : br=webdriver.Chrome                      
             else : raise AssertionError(definition_error)         
          # disable chrome is being controlled by automated software
          if "chromedriver" in webdriver_path.lower():
             ch_opt = Options()
             ch_opt.add_argument("--disable-infobars") 
             self.driver=br(executable_path=webdriver_path,chrome_options=ch_opt) 
          else:
             self.driver=br(executable_path=webdriver_path)
          if "desktop" in browser:      
             self.driver.maximize_window()   
          return self.driver 

      def define_working_folders(self,test_name):
          ProjectSetings=project_settings.ProjectSettings(test_name)
          tests_methods_path=project_path+ProjectSetings.project_folders[0]
          tests_webdrivers_path=project_path+ProjectSetings.project_folders[1]
          tests_screenshots_path=project_path+ProjectSetings.project_folders[2]
          test_screenshots_path=project_path+ProjectSetings.project_folders[3]
          tests_locators_path=project_path+ProjectSetings.project_folders[4]
          return tests_methods_path,tests_webdrivers_path,tests_screenshots_path,\
                 test_screenshots_path,tests_locators_path      

      def goto_url(self,browser,url):
          # here we set value for self.driver variable
          self.driver=self.get_driver(browser)    
          self.driver.get(url)               

      def get_elem(self,locator_type,locator_string): 
          try:
             if locator_type=='id':
                self.elem=WebDriverWait(self.driver,30).until(EC.visibility_of_element_located((By.ID,locator_string)))
             elif locator_type=='xpath':
                  self.elem=WebDriverWait(self.driver,30).until(EC.visibility_of_element_located((By.XPATH,locator_string)))
             elif locator_type=='name':
                   self.elem=WebDriverWait(self.driver,30).until(EC.visibility_of_element_located((By.NAME,locator_string)))
             elif locator_type=='css':
                   self.elem=WebDriverWait(self.driver,30).until(EC.visibility_of_element_located((By.CSS_SELECTOR,locator_string))) 
             else:print 'Locator type: '+locator_type.upper()+' for element: '+locator_string+'is incorrect !'\
                  ;self.driver.quit();sys.exit()
          # elem already sefined in __init__                        
          except:pass#self.elem=None 
          if self.elem:
             return self.elem
          else:print 'Can not locate element: '+locator_string+ ' with Selenium !';self.driver.quit();sys.exit()
      
      def click_elem_selenium(self,locator_type,locator_string,source_name):
          self.elem=self.get_elem(locator_type,locator_string)
          if self.elem :
             # click on drop-down on some browsers make drop-down empty , when click with execute_cript()
             # and freeze drop-down or spoil canvas when click without javascript
             # if running_test.browser in ("safari mac","chrome mac") and type == "drop-down":pass
             # firefox modify mouse arrow when focus
             # elif "firefox" not in running_test.browser:elem.send_keys(Keys.NULL)  
             sleep(1)
             try:
                 self.elem.click()
             except:
                    try:
                        self.driver.execute_script("arguments[0].click();",self.elem)                         
                    except:
                           try:
                               ActionChains(self.driver).move_to_element_with_offset(self.elem,0,0).click().perform()
                           except:err="Try other methods to click an element !";raise AssertionError(err)                       
             print 'Click: '+source_name  
        
      def quit_browser(self):
          sleep(1)
          self.driver.quit() 

      def get_running_module_name(self,test_name):
          if os.getcwd() not in sys.path:
             sys.path.insert(0,os.getcwd())
          module_name=self.import_module(test_name,None)
          return module_name 

      def import_module(self,package,module):
          module=importlib.import_module(package+'.'+module) if module is not None else importlib.import_module(package)
          return module 

      def test(self,test_name,driver,locator,browser):   
          # var1 
          # test_part pot sa-l iau din /tests_files/test_name.py     
          test_part=self.get_running_module_name(test_name).test_part
          #print 'X=',test_part
          # var 2
          # test_part pot sa-l iau din project_settings.py
          #test_part=project_settings.ProjectSettings(test_name).test_parameters[0]
          #print 'X=',test_part
          # elements = list of dictionaries 
          E=locator.get_elements(browser)
          for i in range(len(E)):
             for j in range(len(E[i])):
                  if "source" in E[i][j].keys():
                     if "source_locator_type" and "source_locator_string" in E[i][j].keys():
                        #elem=self.get_elem(driver,E[i][j]["source_locator_type"],E[i][j]["source_locator_string"])
                        elem=self.get_elem(E[i][j]["source_locator_type"],E[i][j]["source_locator_string"])
                        if E[i][j]["source_tool"]=="selenium":
                           try:
                              if E[i][j]["screenshot"]==1 :
                                 print 'Take screenshot of '+E[i][j]["source"]
                                 set_elem_screenshot(driver,test_name,elem,E[i][j]["source_img_name"])
                           except KeyError: pass
                           try:
                              if E[i][j]["source_click"]==1 :
                                 #-------------------------
                                 #print 'L=',driver.find_elements_by_xpath()
                                 #-------------------------
                                 self.click_elem_selenium(driver,elem,E[i][j]["source_name"])
                           except KeyError: pass
                           try:
                              if E[i][j]["source_clear"]==1 :
                                 if E[i][j]["source"] in ["textctrl","multi textctrl"]:
                                    elem.clear()
                                    print 'Clear : '+E[i][j]["source_name"]+" "+E[i][j]["source"]
                           except KeyError: pass
                           try:
                              if E[i][j]["source_change"]==1 :
                                 if E[i][j]["source"] in ["textctrl","multi textctrl"]:
                                    elem.send_keys(E[i][j]["source_changed_value"])
                                    print 'Change value for : '+E[i][j]["source_name"]+" "+E[i][j]["source"]
                                 elif E[i][j]["source"] == "textctrl":
                                    elem.send_keys(E[i][j]["source_changed_value"])
                                    print 'Change value for : '+E[i][j]["source_name"]+" "+E[i][j]["source"]
                                 elif E[i][j]["source"] in ["drop-down","list"]:
                                    #print 'L=',len(driver.window_handles)
                                    s= Select(elem)
                                    s.select_by_visible_text(E[i][j]["source_changed_value"])
                                    print 'Change value for : '+E[i][j]["source_name"]+" "+E[i][j]["source"]
                           except KeyError: pass
                           try:
                              if E[i][j]["source_check"]==1:
                                 ev=get_elem_value(driver,E[i][j]["source"],E[i][j]["source_value"],E[i][j]["source_locator_type"],E[i][j]["source_locator_string"]) 
                                 print "Check: "+ E[i][j]["source_name"]+" "+E[i][j]["source"]
                                 print 'ev0=',ev 
                                 try:
                                     print 'ev1=',len(ev)
                                 except :pass    
                                 if ev != E[i][j]["source_value"]:
                                    # quit_browser(driver)
                                    raise AssertionError("Alert ! "+E[i][j]["source_name"]+" "+E[i][j]["source"]+" changed it's default value!")                  
                           except KeyError: pass
                           try:
                              if E[i][j]["source_check_presence"]==1:
                                 if E[i][j]["source_presence"]==False and elem is None:
                                    print 'The main element : '+E[i][j]["source"]+ ' is not present on page !'
                           except KeyError:pass
                        if E[i][j]["source_tool"]=="opencv":
                           try:
                               if E[i][j]["source_click"]==1:
                                  reset_elem_coord(driver,elem,E[i][j]["source"])
                                  click_elem_by_offset(driver,elem,E[i][j]["coord"],E[i][j]["source_name"])
                           except KeyError: pass
                        elif E[i][j]["source_tool"]=="pyautogui":
                             try:
                                 if E[i][j]["source_screenshot"]==1 :
                                    set_elem_screenshot(driver,test_name,elem,E[i][j]["source_img_name"])
                             except KeyError: pass
                             try:
                                 if E[i][j]["source_click"]==1 :
                                    click_elem_pyautogui(test_name,E[i][j]["source_img_name"])
                                    print 'Mouse to: '+E[i][j]["source_name"]
                             except KeyError: pass
                             try:
                                 if E[i][j]["source_change"]==1 :
                                    clear_elem_pyautogui(elem)
                                    print 'Clear: '+E[i][j]["source_name"]
                                    set_elem_value_pyautogui(E[i][j]["source_changed_value"])
                                    print 'Change value for : '+E[i][j]["source_name"]+" "+E[i][j]["source"]
                             except KeyError:pass
                     else:
                          try:
                              # if source is 'new window' switch to new window
                              if E[i][j]["source"]=="previous window":
                                 driver.switch_to.window(driver.window_handles[0])
                          except KeyError: pass
                          try:
                              # if source is 'new window' switch to new window
                              if E[i][j]["source"]=="new window":
                                 driver.switch_to.window(driver.window_handles[1])
                          except KeyError: pass
                          try:
                              # if source is 'new window' switch to new window
                              if E[i][j]["source"]=="active window":
                                 driver.switch_to.window(driver.window_handles[-1])
                          except KeyError: pass
                          try:
                              if E[i][j]["source"]=="url":
                                 driver.get(E[i][j]["url"])
                                 if "desktop" in browser:
                                    if "chrome" in browser:
                                       driver.fullscreen_window()   
                                    else:driver.maximize_window() 
                          except KeyError: pass   
                          try:
                              if E[i][j]["source"]=="close page":
                                 driver.close()
                          except KeyError: pass         
                          try:
                              # if source is 'alert' chech text alert
                              if E[i][j]["source"]=="alert":
                                 try:
                                     from selenium.common.exceptions import TimeoutException
                                     WebDriverWait(driver,10).until(EC.alert_is_present(),\
                                     'Timed out waiting for PA creation '+' confirmation popup to appear.')
                                     alert = driver.switch_to.alert
                                     alert.accept()
                                     print("alert accepted")
                                 except TimeoutException:
                                        print("no alert")
                          except KeyError: pass
                          try:
                              # launch app from terminal
                              if E[i][j]["source"]=="terminal":
                                 from threading import Thread
                                 cmd="/Users/blackdesign/Desktop/cbt_tunnels-macos-x64 --username bcalin@perfectforms.com --authkey u9e112e2f5b4b0c6"
                                 t = Thread(target = lambda: os.system(cmd))
                                 t.start()
                          except KeyError: pass
                          try:
                              if E[i][j]["source"]=="wait":
                                 print 'Wait '+str(E[i][j]["seconds"])+' sec !'
                                 WebDriverWait(driver,E[i][j]["seconds"])
                                 sleep(E[i][j]["seconds"])
                          except KeyError: pass
                          try:
                              if E[i][j]["source"]=="write to file":
                                 f=open('/Users/blackdesign/Desktop/log2.txt','w')
                                 sys.stdout = f
                                 sys.stdout.close()
                          except KeyError: pass
                  # target we will use only on drop-down and how selenium
                  # drop-down sucks drop-down will be made by pyautogui
                  if "target" in E[i][j].keys():
                     if "target_locator_type" and "target_locator_string" in E[i][j].keys():
                        elem=get_elem(driver,E[i][j]["target_locator_type"],E[i][j]["target_locator_string"])
                        if E[i][j]["target_tool"]=="pyautogui":
                           try:
                               if E[i][j]["target_screenshot"]==1 :
                                  set_elem_screenshot(driver,test_name,elem,E[i][j]["target_img_name"])
                           except KeyError:pass
                           try:
                                 if E[i][j]["target_click"]==1 :
                                    #click_elem_pyautogui(E[i][j]["target_img_path"])
                                    click_elem_pyautogui(test_name,E[i][j]["target_img_name"])
                                    print 'Mouse to: '+E[i][j]["target_name"]
                           except KeyError: pass
                           try:
                                 if E[i][j]["target_change"]==1 :
                                    clear_elem_pyautogui(elem)
                                    print 'Clear: '+E[i][j]["target_name"]
                                    set_elem_value_pyautogui(E[i][j]["target_changed value"])
                                    print 'Change value for : '+E[i][j]["target_name"]+" "+E[i][j]["target"]
                           except KeyError: pass
                           try:
                                 if E[i][j]["drag-drop"]==1 :
                                    drag_on_target_pyautogui(test_name,E[i][j]["target_img_name"])
                                    print 'Drag : '+E[i][j]["source_name"]+' on '+E[i][j]["target_name"]
                           except KeyError:pass        


# def set_webdriver(test_name,browser):      
#     test_type=get_running_module_name(test_name).test_type
#     if test_type=="LOCAL":
#        if "desktop" in browser:
#           if platform=="win32":
#              if browser=="chrome desktop win":webdr_name="\chromedriver2.43.exe"
#              elif browser=="firefox desktop win":webdr_name="\geckodriver0.23.exe"   
#              elif browser=="ie desktop win":webdr_name="\IEDriverServer64.exe" 
#              else:webdr_name=None
#           elif platform=="darwin":
#                if browser.__contains__("safari desktop"):webdr_name="/safaridriver"
#                elif browser.__contains__("chrome desktop mac"):webdr_name="/chromedriver_75"
#                elif browser.__contains__("firefox desktop mac"):webdr_name="/geckodriver_0.24"
#                else:webdr_name=None
#           if webdr_name:
#              if platform=="win32":webdriver_path=define_working_folders(test_name)[1]+webdr_name   
#              elif platform=="darwin":
#                 if browser.__contains__("safari desktop"):webdriver_path="/usr/bin/safaridriver"
#                 else:webdriver_path=define_working_folders(test_name)[1]+webdr_name      
#           else:webdriver_path=None;raise AssertionError('For browser : '+browser+' we have no webdriver !')
#           if webdriver_path:
#              return webdriver_path 
#        else: raise AssertionError('Test : '+test_name+' on ,'+browser.upper()+' not yet on LOCAL !')             
#     if test_type=="CBT":
#        from CBT import CBTLogin
#        caps={}
#        caps=CBTLogin(browser).cbt_variables()
#        caps['name']=get_running_module_name(test_name).test_name   
#        if "desktop" in browser:
#           if browser=="chrome desktop win":
#              caps['browserName']='Chrome';caps['version']='60x64';caps['platform']='Windows 10';caps['screenResolution'] = '1680x1050' 
#           elif browser=="chrome desktop mac":
#                caps['browserName']='Chrome';caps['version']='67x64';caps['platform']='Mac OSX 10.13';caps['screenResolution'] = '1400x900'      
#           elif browser=="firefox desktop win":
#                caps['browserName']='Firefox';caps['version']='60x64';caps['platform']='Windows 10';caps['screenResolution'] = '1680x1050' 
#           elif browser=="firefox desktop mac":
#                caps['browserName']='Firefox';caps['version']='60';caps['platform']='Mac OSX 10.13';caps['screenResolution'] = '1400x900'
#           elif browser=="ie desktop win":
#                caps['browserName']='Internet Explorer';caps['version']='11x32';caps['platform']='Windows 10';caps['screenResolution'] = '1680x1050' 
#           elif browser=="edge desktop win":
#                caps['browserName']='MicrosoftEdge';caps['version'] = '17';caps['platform']='Windows 10';caps['screenResolution'] = '1680x1050'
#           elif browser=="safari desktop mac":
#                caps['browserName']='Safari';caps['screenResolution'] = '1400x900';caps['platform'] = 'Mac OSX 10.14';caps['version'] = '12'
#                # edit C:\Python27\Lib\site-packages\selenium\webdriver\common\action_chains.py (and save) and
#                # add  at "class ActionChains(object)" on "def __init__(self, driver)" method at the end next 2 lines:
#                # if self._driver.name in ('Safari','Safari Technology Preview'):
#                #    self.w3c_actions.key_action.pause=lambda *args,**kwargs:None 
#           else:caps=None;raise AssertionError('For this browser we have no CAPS !')
#           if caps:
#              return caps    
#        if "phone" in browser:
#           if browser=="chrome phone android 7":
#              caps['browserName']='Chrome';caps['deviceName']='Galaxy S7';caps['platformVersion']='7.0';caps['platformName'] = 'Android';caps['deviceOrientation'] = 'portrait' 
#           elif browser=="chrome phone android 8":
#              caps['browserName']='Chrome';caps['deviceName']='Galaxy S8';caps['platformVersion']='8.0';caps['platformName'] = 'Android';caps['deviceOrientation'] = 'portrait'  
#           elif browser=="chrome phone android 9":
#                caps['browserName']='Chrome';caps['deviceName']='Pixel 3';caps['platformVersion']='9.0';caps['platformName'] = 'Android';caps['deviceOrientation'] = 'portrait'         
#           elif browser=="safari phone ios 12":
#                caps['browserName']='Safari';caps['deviceName']='iPhone XR Simulator';caps['platformVersion']='12.0';caps['platformName'] = 'iOS';caps['deviceOrientation'] = 'portrait'   
#           elif browser=="safari phone ios 11":
#                caps['browserName']='Safari';caps['deviceName']='iPhone 8 Simulator';caps['platformVersion']='11.0';caps['platformName'] = 'iOS';caps['deviceOrientation'] = 'portrait'  
#           elif browser=="safari phone ios 10":
#                caps['browserName']='Safari';caps['deviceName']='iPhone 7 Simulator';caps['platformVersion']='10.2';caps['platformName'] = 'iOS';caps['deviceOrientation'] = 'portrait'                 
#           else:caps=None;raise AssertionError('For this browser we have no CAPS !')         
#           if caps:
#              return caps   
#        if "tablet" in browser:
#           if browser=="chrome tablet android":
#              caps['browserName']='Chrome';caps['deviceName']='Nexus 9';caps['platformVersion']='6.0';caps['platformName'] = 'Android';caps['deviceOrientation'] = 'portrait' 
#           elif browser=="safari tablet ios":
#              caps['browserName']='Safari';caps['deviceName']='iPad 6th Generation Simulator';caps['platformVersion']='12.0';caps['platformName'] = 'iOS';caps['deviceOrientation'] = 'landscape'    
#           else:caps=None;raise AssertionError('For this browser we have no CAPS !')         
#           if caps:
#              return caps            
        
# # ca sa putem da click pe radio btn published (sa fie dezactivat)
# # tb ca dropdown Draft sa nu fie gol si dropdown Published sa nu fie gol
# # click published radio btn and select minim published version
# def click_prbtn_sel_min_pvs(driver,(rb1_xpath,rb1_name),(rb2_xpath,rb2_name),dd1_xpath,dd2_xpath):
#     print 'Check if we can press published radio btn !'
#     find_by_xpath_and_click_object(driver,rb1_xpath,rb1_name)
#     select1 = Select(driver.find_element_by_xpath(dd1_xpath))
#     find_by_xpath_and_click_object(driver,rb2_xpath,rb2_name)
#     select2 = Select(driver.find_element_by_xpath(dd2_xpath))
#     if len(select1.options) != 0 and len(select2.options) != 0 :
#        rb=WebDriverWait(driver,3).until(EC.element_to_be_clickable((By.XPATH,rb2_xpath)))
#        find_by_xpath_and_click_object(driver,rb2_xpath,rb2_name)
#        print 'Select drop-down min value !'
#        select2.select_by_value(str(min([float(x.text) for x in select2.options])))
#        result='pass'
#     else: result="fail";raise AssertionError("To click on published btn we must have a draft version and form must be published !")

# def click_suite_elements(driver,D):
#     for i in D.keys():
#         for j in D[i].keys():
#             click_object(driver,D[i][j],j,None)
                      

# def find_by_xpath_and_click_object(driver,obj_xpath,object_name):
#     sleep(2)
#     try:  
#         driver.find_element_by_xpath(obj_xpath).click()
#     except:err="Locator '%s'   N O T   R I G H T  for : '%s' or elem. not present !" %(obj_xpath,object_name);raise AssertionError(err)       

# def reset_canvas_coord(driver,cv_name,cv_xpath):
#     sleep(2)       
#     elem=WebDriverWait(driver,10).until(EC.visibility_of_element_located((By.XPATH,cv_xpath)))      
#     #ActionChains(driver).move_to_element_with_offset(elem,0,0).context_click().perform()
#     ActionChains(driver).move_to_element_with_offset(elem,0,0).click().perform()
#     print 'Reset : '+cv_name+' coordinates !'

# def reset_elem_coord(driver,elem,source):
#     #sleep(2)       
#     #elem=WebDriverWait(driver,10).until(EC.visibility_of_element_located((By.XPATH,cv_xpath)))      
#     #ActionChains(driver).move_to_element_with_offset(elem,0,0).context_click().perform()
#     ActionChains(driver).move_to_element_with_offset(elem,0,0).click().perform()
#     print 'Reset : '+source+' coordinates !'    

# def click_elem_by_offset(driver,elem,(elem_coord),source_name):
#     sleep(1)
#     #canvas=driver.find_element_by_xpath(cv_xpath)     
#     ActionChains(driver).move_to_element_with_offset(elem,elem_coord[0],elem_coord[1]).click().perform()  
#     #ActionChains(driver).move_to_element_with_offset(canvas,obj_coord[0],obj_coord[1]).context_click().perform() 
#     print "Click : "+source_name+" after it's coordinates !"  

# def create_screenshots_dir(path):
#     try:
#         if not os.path.exists(path):
#            os.mkdir(path)
#     except OSError as e:os.remove(path);raise AssertionError(str(e))   

     
# def close_test(error_type):
#     if error_type=="bug":
#        raise AssertionError('THIS IS A BUG ! I will close test !')    
#     elif error_type=="concept error":
#          raise AssertionError('THIS IS A CONCEPT ERROR ! I will close test !')       

# def get_elem_value(driver,source,source_value,locator_type,locator_string):
#     elem=get_elem(driver,locator_type,locator_string)            
#     if source in ["check box","radio btn"]: 
#        ev=elem.is_selected() 
#     if source.__contains__("textctrl"): 
#        ev=elem.get_attribute('value')
#     if source == "drop-down":
#        # selection 
#        s= Select(elem)
#        # var1
#        #for opt in s.options:
#        #    if opt.is_selected():
#        #       cs= s.first_selected_option
#        #       ev=cs.text 
#        #    else:ev=""  
#        #------------------
#        # current selection
#        # var2
#        try:
#            cs= s.first_selected_option
#            ev=cs.text 
#        except NoSuchElementException:
#               ev=""      
#     if source in ["grid cell","text"]:
#        ev=elem.text    
#        #ev=driver.find_element_by_xpath(elem_xpath).get_attribute('innerHTML')
#     # SetField,SimpleBranch
#     if source == "list":
#        s= Select(elem)
#        if source_value in [option.text for option in s.options]:
#           ev=source_value
#           s.select_by_visible_text(source_value)
#        else:ev=None      
#     return ev 

# # update stages/(behaviors) and paths coordinates with coord. founded by open cv
# def update_coord(BS,P,Lbs_coord,Lph_coord):
#     # for behaviors/stages
#     if None not in [BS,Lbs_coord]:   
#        for i in range(len(BS)):
#           BS[i][0]["coord"]=Lbs_coord[i]
#     # for paths
#     if None not in [P,Lph_coord]:   
#        for j in range(len(P)):
#           P[j][0]["coord"]=Lph_coord[j]
                
# # get elements (paths and behaviors/stages) coordinates
# # on locators file we have a list with ordonated elements (after y axis): OEy_locators to click on
# # and on opencv file we have a list with ordonated coordinates (after y axix): OEy_opencv
# # define paths coordinates and behaviors/stages coordinates
# Lph_coord=[]
# Lbs_coord=[]
# def get_elem_coord(OEy_locators,Lph_coord,Lbs_coord,OEy_opencv):
#     for i in range(len(OEy_locators)):
#         try:
#             if OEy_locators[i]=="path":
#                Lph_coord.append(OEy_opencv[i])
#             else:Lbs_coord.append(OEy_opencv[i])
#         except IndexError:
#                           pass  

# def set_click_by_browser(test_name,browser):
#     if browser.__contains__("win"):
#        # sa-l fut in gura de click ca a fost 2 , acum e 1
#        #if "chrome" in browser:clk=2
#        if "chrome" in browser:clk=1   
#        elif "firefox" or "ie" or "edge" in browser:clk=1
#     elif browser.__contains__("mac"):clk=1              
#     return clk 
     
# # save canvas screenshot
# def save_to_png(driver,canvas,path_to):
#     if running_test()=='LOCAL': 
#        try:   
#            driver.get_screenshot_as_file(path_to) 
#            w=canvas.location['x']+canvas.size['width']
#            h=canvas.location['y']+canvas.size['height']
#            img=Image.open(path_to)
#            img=img.crop((int(canvas.location['x']),int(canvas.location['y']),int(w),int(h)))
#            img.save(path_to)
#        except Exception as EC:os.remove(path_to);print "Can't take screenshot ! "+str(EC)        
#     else:raise AssertionError("SCREENSHOT IS TAKEN ONLY IN LOCAL TEST !")

# # set element screenshot
# def set_elem_screenshot(driver,test_name,elem,elem_img_name): 
#     if running_test()=='LOCAL':
#           elem_img_path=define_working_folders(test_name)[3]+elem_img_name
#        #if not os.path.exists(elem_img_path):
#           try: 
#               driver.get_screenshot_as_file(elem_img_path) 
#               x=elem.location['x']
#               y=elem.location['y']
#               w=elem.location['x']+elem.size['width']
#               h=elem.location['y']+elem.size['height']
#               img=Image.open(elem_img_path)
#               if running_test.browser.__contains__("chrome"):
#                  img=img.crop((x,y,w,h))
#               if running_test.browser.__contains__("firefox"):
#                  img=img.crop((x-5,y-5,w+5,h+5))
#               if running_test.browser.__contains__("safari"):
#                  img=img.crop((x,y,w,h))   
#               img.save(elem_img_path)
#           except Exception as EC:os.remove(elem_img_path);print "Can't take screenshot ! "+str(EC)      
#     #else:raise AssertionError("SCREENSHOT IS TAKEN ONLY IN LOCAL TEST !")                        

# # if we want a value for a element but elem is 
# # not reachable by keyboard we will take value
# # by elem.get_attribute("innerHTML")
# def get_value_from_innerHTML(txt):
#     # beggining index from 'value=' string
#     beg=txt.index('value=')
#     # full text without 'value=' string
#     t=txt[beg+len('value='):]
#     # list with " indexes
#     I=[]
#     count=0
#     for i in range(len(txt[beg+len('value='):])):
#         if txt[beg+len('value='):][i]=='"':
#            count+=1 
#            # take only first 2 indexes of "
#            if count <=2:
#               I.append(i)        
#     s=t[I[0]+1:I[1]] 
#     #print len(s.split(' '))
#     return s

# def quit_browser(driver):
#     sleep(2)
#     driver.quit()            

# # when elem is not reachable by keyboard we will 
# # take elem screenshot and find elem with pyautogui
# def click_elem_not_keyboard_reachable(driver,elem,elem_img_path):
#     set_elem_screenshot(driver,elem,elem_img_path)
#     sleep(2)
#     # center coordinates of elem on page 
#     Celem=pyautogui.locateCenterOnScreen(elem_img_path)
#     pyautogui.moveTo(Celem.x,Celem.y,0.25)
#     sleep(2)
#     # find txt in elem (in textctrl)
#     txt=elem.get_attribute("innerHTML")
#     for item in get_value_from_innerHTML(txt):
#         # sleep 1/3 from a second
#         sleep(.3)
#         pyautogui.keyDown('backspace')
#     sleep(2) 

# def click_elem_pyautogui(test_name,elem_img_name):
#     elem_img_path=define_working_folders(test_name)[3]+elem_img_name 
#     sleep(2)
#     if "btn.png" not in elem_img_path:
#        coord=pyautogui.locateCenterOnScreen(elem_img_path,grayscale=True,confidence=0.9)
#     else:coord=pyautogui.locateCenterOnScreen(elem_img_path,grayscale=True,confidence=0.6)
#     sleep(2)
#     pyautogui.click(coord.x,coord.y,clicks=1,interval=0.4,button='left')
#     sleep(2)           

# def clear_elem_pyautogui(elem):
#     txt=elem.get_attribute("innerHTML")
#     # some kind of focus
#     pyautogui.press(presses=1, keys='del')      
#     for item in get_value_from_innerHTML(txt):
#         # sleep 1/3 from a second
#         sleep(.3)
#         pyautogui.keyDown('backspace')
#     sleep(2)

# def set_elem_value_pyautogui(value):
#     sleep(2)
#     pyautogui.typewrite(value)
#     sleep(2)

# def drag_on_target_pyautogui(test_name,target_img_name): 
#     target_img_path=define_working_folders(test_name)[3]+target_img_name  
#     sleep(2)
#     target_coord=pyautogui.locateCenterOnScreen(target_img_path,grayscale=True,confidence=0.7)#0.9 0.7 on button
#     sleep(2)
#     pyautogui.dragTo(target_coord.x,target_coord.y,0.4, button='left')#0.25
#     sleep(2)
                                      
# def set_screenshots_test_folder(test_name):
#     screenshots_folder_name=define_working_folders(test_name)[2]
#     test_screenshots_folder_name=define_working_folders(test_name)[3]
#     create_screenshots_dir(screenshots_folder_name)
#     create_screenshots_dir(test_screenshots_folder_name)

# # if a canvas has elements inside we can find elements
# #  coordinates from image screenshot with opencv
# def get_elem_coord_from_img_with_opencv(test_name,source_img_name):
#     source_img_path=define_working_folders(test_name)[3]+source_img_name  
#     # dictionary with element key and center coordinates value
#     Ecc=opencv.find_elements(source_img_path)
#     return Ecc