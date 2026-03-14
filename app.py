import shutil
from components.mainPage import deployMainPage
import Utils.pageManager as pageManager
from components.homepage import deployHomePage
import streamlit as st
from components.Experimentos.mru import deployMRU
from components.ErrorPage import deployWarningPage
from components.login import deployLoginPage   
from components.endPage import deployEndPage

if "page" not in st.session_state:
    st.session_state.page = "login"
#pageManager.page= "mru"


   
print(pageManager.st.session_state.page)
match pageManager.st.session_state.page:
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
        

    
       
    
    



