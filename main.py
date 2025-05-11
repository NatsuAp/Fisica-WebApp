from components.mainPage import deployMainPage
from components.body import deployBody
import Utils.pageManager as pageManager

        
      
match pageManager.page:
    case "mainPage":
        deployMainPage()
    case "body":
        deployBody()
    
    



