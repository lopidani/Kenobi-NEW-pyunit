import os,sys

if os.getcwd() not in sys.path:
   sys.path.insert(0,os.getcwd())
from test_methods import methods
from time import sleep


test_name=__file__.rstrip('cd').split("/")[-1][:-3] if sys.platform=="darwin" else __file__.rstrip('cd').split("\\")[-1][:-3]   

browser='chrome desktop mac'
url="https://testing.perfectforms.com/"
if __name__=='__main__':
   OurTest= methods.Web(test_name)
   OurTest.goto_url(browser,url)
   OurTest.get_elem('name','password')
   OurTest.click_elem_selenium('name','password','element parola')
   OurTest.quit_browser()