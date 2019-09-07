 
import sys
from tests_methods import project_settings
test_name = project_settings.running_test.name
MyTest = project_settings.ProjectSettings(test_name)
test_part = MyTest.test_parameters[0]
browser = project_settings.running_test.browser

# LOCATORS
frame="//iframe[@id='MjIzMDY=']"
# coord1 (86,291)
call_funct_btn="PF_24"
#call_funct_btn="//iframe//input[@id='PF_24']"
call_funct_txt="//input[@id='PF_23']"
call_mess_btn="PF_25"
nr_2_txt_btn1="PF_37"
nr_2_txt_btn2="PF_39"
nr_2_txt1="PF_36"
nr_2_txt2="PF_40"
eq_btn1="PF_30"
txt1="PF_28"
eq_btn2="PF_58"
txt2="PF_56"
eq_btn3="PF_34"
txt3="PF_33"
eq_btn4="PF_59"
txt4="PF_57"
eq_btn5="PF_49"
txt5="PF_48"
eq_btn6="PF_66"
txt6="PF_64"
prod_btn_tb="PF_80"
res_tb1="//input[@id='1-PF_76']"
res_tb2="//input[@id='1-PF_79']"
url_player="https://testing.perfectforms.com/qa_tests/CallJavaScript.html"
#-----------------------------------
# SCREENSHOTS NAMES
if sys.platform=="win32":canvas_img="\\javascript_frame.png"
elif sys.platform=="darwin":canvas_img="/javascript_frame.png"
#-----------------------------------
      
def get_elements(browser):
    if "desktop" or "phone" or "tablet" in browser: 
       E1=[
       {"source":"url","url":url_player}, 
       {"source":"canvas","source_name":'frame',"source_locator_type":"xpath","source_locator_string":frame,\
        "source_tool":"selenium","source_click":0,"source_check":0,"source_change":0,"source_screenshot":1,\
        "source_scroll":0,"source_img_name":canvas_img},
       {"source":"canvas","source_name":"elem80","source_locator_type":"xpath","source_locator_string":frame,\
        "source_coord":(),"source_click":1,"source_tool":"opencv","source_img_name":canvas_img},
       {"source":"wait","seconds":3},    
          ] 
       E2=[ 
         
       {"source":"btn","source_name":"Call Function","source_locator_type":"xpath","source_locator_string":call_funct_btn,\
       "source_tool":"selenium","source_click":1,"source_check":0},
       {"source":"btn","source_name":'Nr 2 txt btn1',"source_locator_type":"id","source_locator_string":nr_2_txt_btn1,\
        "source_tool":"selenium","source_click":1}, 
       {"source":"btn","source_name":'Nr 2 txt btn2',"source_locator_type":"id","source_locator_string":nr_2_txt_btn2,\
        "source_tool":"selenium","source_click":1},
       {"source":"btn","source_name":'Equal1',"source_locator_type":"id","source_locator_string":eq_btn1,\
        "source_tool":"selenium","source_click":1},
       {"source":"btn","source_name":'Equal2',"source_locator_type":"id","source_locator_string":eq_btn2,\
        "source_tool":"selenium","source_click":1},
       {"source":"btn","source_name":'Equal3',"source_locator_type":"id","source_locator_string":eq_btn3,\
        "source_tool":"selenium","source_click":1}, 
       {"source":"btn","source_name":'Equal4',"source_locator_type":"id","source_locator_string":eq_btn4,\
        "source_tool":"selenium","source_click":1}, 
       {"source":"btn","source_name":'Equal5',"source_locator_type":"id","source_locator_string":eq_btn5,\
        "source_tool":"selenium","source_click":1},
       {"source":"btn","source_name":'Equal6',"source_locator_type":"id","source_locator_string":eq_btn6,\
        "source_tool":"selenium","source_click":1},   
       {"source":"wait","seconds":1},
          ] 
       E3=[  
       {"source":"textctrl","source_name":"Call funct txt","source_locator_type":"name","source_locator_string":call_funct_txt,\
        "source_tool":"selenium","source_click":1,"source_check":1,"source_value":"Hello world!"},
       {"source":"textctrl","source_name":"Nr 2 txt1","source_locator_type":"name","source_locator_string":nr_2_txt1,\
        "source_tool":"selenium","source_click":1,"source_check":1,"source_value":"four hundred forty seven point eight nine "},
       {"source":"textctrl","source_name":"Nr 2 txt2","source_locator_type":"name","source_locator_string":nr_2_txt2,\
        "source_tool":"selenium","source_click":1,"source_check":1,"source_value":"four hundred fifty six point three "}, 
       {"source":"textctrl","source_name":"Txt1","source_locator_type":"name","source_locator_string":txt1,\
        "source_tool":"selenium","source_click":1,"source_check":1,"source_value":"15.00"}, 
       {"source":"textctrl","source_name":"Txt2","source_locator_type":"name","source_locator_string":txt2,\
        "source_tool":"selenium","source_click":1,"source_check":1,"source_value":"15"},
       {"source":"textctrl","source_name":"Txt3","source_locator_type":"name","source_locator_string":txt3,\
        "source_tool":"selenium","source_click":1,"source_check":1,"source_value":"20"}, 
       {"source":"textctrl","source_name":"Txt4","source_locator_type":"name","source_locator_string":txt4,\
        "source_tool":"selenium","source_click":1,"source_check":1,"source_value":"1"},
       {"source":"textctrl","source_name":"Txt5","source_locator_type":"name","source_locator_string":txt5,\
        "source_tool":"selenium","source_click":1,"source_check":1,"source_value":"15"},
       {"source":"textctrl","source_name":"Txt6","source_locator_type":"name","source_locator_string":txt6,\
        "source_tool":"selenium","source_click":1,"source_check":1,"source_value":"15"}, 
       {"source":"textctrl","source_name":"Result tb1","source_locator_type":"xpath","source_locator_string":res_tb1,\
        "source_tool":"selenium","source_click":1,"source_check":1,"source_value":"-9"},              
       {"source":"textctrl","source_name":"Result tb2","source_locator_type":"xpath","source_locator_string":res_tb2,\
        "source_tool":"selenium","source_click":1,"source_check":1,"source_value":"25.00"},                                                                                                                                                                               
           ]
       if test_part=="full test" or test_part=="part1":    
          E=[E1]
          #E=[E1,E2,E3]     
    return E       