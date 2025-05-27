import shutil
from components.mainPage import deployMainPage
import Utils.pageManager as pageManager
from components.homepage import deployHomePage
import streamlit as st
from components.Experimentos.mru import deployMRU
from components.ErrorPage import deployWarningPage
from components.login import deployLoginPage   
from components.endPage import deployEndPage


#pageManager.page= "mru"

shutil.rmtree("temp_images")
print(pageManager.page)
match pageManager.page:
    case "mainpage":
        deployMainPage()
    case "homepage":
        deployHomePage()
    case "error":
        deployWarningPage()
    case "mru":
        deployMRU()
    case "login":
        deployLoginPage()
    case "end":
        deployEndPage()
        

    
       
    
    



