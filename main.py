from components.mainPage import deployMainPage
import Utils.pageManager as pageManager
from components.homepage import deployHomePage
        
print(pageManager.page)
match pageManager.page:
    case "mainPage":
        deployMainPage()
    case "homepage":
        deployHomePage()

    
       
    
    



