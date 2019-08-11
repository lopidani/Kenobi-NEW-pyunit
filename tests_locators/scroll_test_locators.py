import sys
from tests_methods import project_settings
test_name = project_settings.running_test.name
MyTest = project_settings.ProjectSettings(test_name)
test_part = MyTest.test_parameters[0]
browser = project_settings.running_test.browser

#------------------------------------------
# LOCATORS AND TEST STEPS

# LOGIN PERFECTFORMS DATAS
url_player_desktop = 'https://testing.perfectforms.com'
user ='userd@pf.com'
passw ='qqqqqq'
greet_win_xpath="//a[contains(.,'Exit')]"
hlp_win_xpath="(//button[contains(.,'Close')])[2]"
edit_form_xpath="/html[1]/body[1]/div[1]/aside[1]/div[3]/div[1]/div[1]/div[1]"
private_xpath="//i[@class='pf pf-carot-left']"
scroll_test_xpath="//a[@title='Scroll test']"
published_btn_xpath="//input[@value='published']"
published_vrs_drop_xpath="//select[@id='publishedVersion']"
draft_btn_xpath="//input[contains(@value,'draft')]"
draft_vrs_drop_xpath="//select[contains(@id,'draftVersion')]" 
design_btn_xpath="/html[1]/body[1]/div[1]/section[1]/div[2]/div[4]/div[1]/button[1]"
cls_hlp_win_xpath="(//button[@class='greeting-button close-help-center'])[1]"
txtctrl_xpath="//div[@id='PFXX6564441752806096896']"
txtctrl_is_click_xpath="//a[@role='button'][contains(.,'Text Input is clicked')]"
canvas_xpath="//canvas[@id='aPageSel']"
              
# DASHBORD LOCATORS
file_xpath="/html[1]/body[1]/div[1]/div[1]/header[1]/div[1]/div[3]/ul[1]/li[1]/a[1]"
save_as_new_version_xpath="/html[1]/body[1]/div[1]/div[1]/header[1]/div[1]/div[3]/ul[1]/li[1]/ul[1]/li[2]/a[1]"
# era
close_form_xpath="/html[1]/body[1]/div[1]/div[1]/header[1]/div[1]/div[3]/ul[1]/li[1]/ul[1]/li[6]/a[1]"
#close_form_xpath="//a[text()='Close']"
publish_btn_xpath="/html[1]/body[1]/div[1]/section[1]/div[2]/div[4]/div[1]/button[2]"
ok_publish_xpath="//button[@type='button'][contains(.,'Yes')]"
sign_out_xpath="//span[contains(.,'Sign Out')]"
close_no_save_btn_xpath="//button[contains(.,'No')]"

grid_cell_txtinput1_xpath="//td[@role='gridcell'][contains(.,'Text Input 1')]"
#grid_cell_txtinput1_xpath="//td[text()='Text Input 1']"
#grid_cell_txtinput1_xpath="//td[text()='Text Input 1']" if running_test.browser=="safari" else "//td[@role='gridcell'][contains(.,'Text Input 1')]"
grid_cell_txtinput3_xpath="//td[@role='gridcell'][contains(.,'Text Input 3')]"
del_icon_xpath="(//i[@class='fa pf-delete icon-gradient'])[2]"
add_icon_xpath="(//i[contains(@class,'fa pf-add')])[2]"
#-----------------------------------------
# Select Object window
# era
trgle_xpath="//a[@href='#'][contains(.,'Page 1')]"
#trgle_xpath="//span[@class='field-list-toggle glyphicon glyphicon-triangle-right']"
# era
txt_txtinput3_xpath="//a[@href='#'][contains(.,'Text Input 3')]"
#txt_txtinput3_xpath="//a[@data-selected-item='PFXX6488416045739540480']"
# era
ok_btn_xpath="//button[@type='button'][contains(.,'OK')]"
#ok_btn_xpath="//button[text()='OK']"
# era
cancel_btn_xpath="//button[@type='button'][contains(.,'Cancel')]"
#cancel_btn_xpath="//button[text()='Cancel']"
#-----------------------------------
radio1_xpath="(//input[@name='defaultMessage'])[1]"
radio2_xpath="(//input[@name='defaultMessage'])[2]"
txtctrl_message_xpath="//textarea[contains(@id,'message')]"
radio3_xpath="//input[contains(@name,'stopExecution')]"
summary_btn_xpath="//a[contains(text(),'Summary')]"
auto_sum_check_xpath="//input[@id='autosummary']"
auto_sum_textctrl_xpath="//textarea[@id='summary']"
#-----------------------------------
# SCREENSHOTS NAMES
if sys.platform=="win32":canvas_img="\\scroll_test_canvas.png"
elif sys.platform=="darwin":canvas_img="/scroll_test_canvas.png"
#-----------------------------------
# EVERY STAGE (PART OF TEST TO INTERACT WITH ELEMENTS) IS A LIST OF DICTIONARY
# to click: "click":1, to check: "check":1, to change: "change":1 , to clear: "clear":1
# to take screenshot: "screenshot":1, to drag a source elem and drop to a target elem: "drag-drop":1


def get_elements(browser):
    if 'desktop' in browser:
       Elog=[
       {'source': 'url', 'url': url_player_desktop},     
       # username field
       {"source":"textctrl","source_name":"Email","source_locator_type":"name","source_locator_string":'userName',\
       "source_tool":"selenium","source_click":1,"source_clear":1,"source_change":1,"source_changed_value":user},
       # password field
       {"source":"textctrl","source_name":"Password","source_locator_type":"name","source_locator_string":'password',\
       "source_tool":"selenium","source_click":1,"source_clear":1,"source_change":1,"source_changed_value":passw},
       # login btn
       {"source":"btn","source_name":"Login","source_locator_type":"id","source_locator_string":'loginSubmit',\
       "source_tool":"selenium","source_click":1,"source_check":0,"source_change":0}, 
           ]
       
        # click btn greeting window
       Egreet=[
       {"source":"btn","source_name":'Greeting Window Exit',"source_locator_type":"xpath","source_locator_string":greet_win_xpath,\
       "source_tool":"selenium","source_click":1,"source_check":0,"source_change":0}
              ]
       # close btn help window
       Ehlp=[
       {"source":"btn","source_name":"Close","source_locator_type":"xpath","source_locator_string":cls_hlp_win_xpath,\
       "source_tool":"selenium","source_click":1,"source_check":0,"source_change":0}
            ]
       # choose form    
       Ech_form=[
       {"source":"btn","source_name":"Edit Forms","source_locator_type":"xpath","source_locator_string":edit_form_xpath,\
        "source_tool":"selenium","source_click":1,"source_check":0,"source_change":0},
       {"source":"btn","source_name":"Private","source_locator_type":"xpath","source_locator_string":private_xpath,\
        "source_tool":"selenium","source_click":1,"source_check":0,"source_change":0},
       {"source":"btn","source_name":"Scroll test","source_locator_type":"xpath","source_locator_string":scroll_test_xpath,\
        "source_tool":"selenium","source_click":1,"source_check":0,"source_change":0}, 
                ]
       # take first published version
       Efst_publ=[
       {"source":"radio btn","source_name":"Published","source_locator_type":"xpath","source_locator_string":published_btn_xpath,\
       "source_tool":"selenium","source_click":1,"source_check":0,"source_change":0}, 
       {"source":"drop-down","source_name":"Published drop-down","source_locator_type":"id","source_locator_string":"publishedVersion", 
       "source_tool":"selenium","source_click":1,"source_check":0,"source_change":1,"source_changed_value":'1.0'}, 
                 ]
       # enter in canvas
       Ecnv_entr=[ 
       {"source":"btn","source_name":"Design","source_locator_type":"xpath","source_locator_string":design_btn_xpath,\
       "source_tool":"selenium","source_click":1,"source_check":0,"source_change":0},    
       {"source":"btn","source_name":'Help Center Window close ,again',"source_locator_type":"xpath","source_locator_string":cls_hlp_win_xpath,\
       "source_tool":"selenium","source_click":1,"source_check":0,"source_change":0},
       {"source":"textctrl","source_name":"Text Input","source_locator_type":"xpath","source_locator_string":txtctrl_xpath,\
       "source_tool":"selenium","source_click":1,"source_clear":0,"source_change":0}, 
       {"source":"text","source_name":"Text input is clicked","source_locator_type":"xpath","source_locator_string":txtctrl_is_click_xpath,\
       "source_tool":"selenium","source_click":1,"source_clear":0,"source_change":0},            
                 ] 
       # work with canvas - take canvas screenshot and find elements in canvas with opencv adter coordinates 
       Ecnv_img=[
       {"source":"canvas","source_name":'Scroll test canvas',"source_locator_type":"xpath","source_locator_string":canvas_xpath,\
        "source_tool":"selenium","source_click":0,"source_check":0,"source_change":0,"source_screenshot":1,"source_img_name":canvas_img},
       {"source":"canvas","source_name":'scroll canvas',"source_locator_type":"xpath","source_locator_string":canvas_xpath,\
        "source_tool":"selenium","source_scroll":1},
       {"source":"wait","seconds":3},  
                
                ] 
       
       # Elements are on canvas so source to click on is canvas with it's locators   
       # first elem finded with coord , elem1 is given when we run opencv.py with canvas screenshot path
       # so in elem definition we must include canvas screenshot path witch is given by canvas img (screenshot) name
       
       Ecnv_elem1=[
       {"source":"canvas","source_name":"elem1","source_locator_type":"xpath","source_locator_string":canvas_xpath,\
       "source_coord":(),"source_click":1,"source_tool":"opencv","source_img_name":canvas_img},
       {"source":"grid cell","source_name":"Mandatory grid cell","source_value":"Text Input 1","source_locator_type":"xpath",\
       "source_locator_string":grid_cell_txtinput1_xpath,"source_tool":"selenium","source_click":1,"source_check":1},
       {"source":"radio btn","source_name":"Show Default Message","source_value":True,"source_locator_type":"xpath",\
       "source_locator_string":radio1_xpath,"source_click":0,"source_check":1,"source_tool":"selenium"},
       {"source":"radio btn","source_name":"Stop Execution","source_value":True,"source_locator_type":"xpath",\
       "source_locator_string":radio3_xpath,"source_click":0,"source_check":1,"source_tool":"selenium"},
       {"source":"btn","source_name":"Summary","source_locator_type":"xpath","source_locator_string":summary_btn_xpath,\
       "source_click":1,"source_check":0,"source_tool":"selenium"},
       {"source":"radio btn","source_":"Auto-summary","source_value":True,"source_locator_type":"xpath",\
       "source_locator_string":auto_sum_check_xpath,"source_click":0,"source_check":1,"source_tool":"selenium"},
       {"source":"multi textctrl","source_name":"Auto-summary text","source_value":"","source_locator_type":"xpath",\
       "source_locator_string":auto_sum_textctrl_xpath,"source_click":1,"source_check":1,"source_tool":"selenium"}
                 ]  
       Ecnv_elem2=[
       {"source":"canvas","source_name":"elem2","source_locator_type":"xpath","source_locator_string":canvas_xpath,\
       "source_coord":(),"source_click":1,"source_tool":"opencv","source_img_name":canvas_img},
                 ]        
       
       
       # At full test or part1 test we take first published version
       if test_part=="full test" or test_part=="part1":
          E=[Elog,Egreet,Ehlp,Ech_form,Efst_publ,Ecnv_entr,Ecnv_img]#,Ecnv_elem1,Ecnv_elem2]
    return E   