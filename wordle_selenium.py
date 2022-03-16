from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys
import time, pyautogui, random, pydirectinput

namess = ['Hen','Queasy','Malibuca','Kami','Rezon','Vadeal','Anas','ThomasHD','TaySon','Raizen','Chapix','Pinq','Merstach','JannisZ','DKS','Vortex','Stormyrite','Kiryache','BadSniper','Decyptos','Xsweeze','Merijn','Teeq','Chico','TChypSs','Setty','Venο','PabloWingu','Joefn','Toose','Mappi','phyenix','Andilex','Clement','TruleX','lushaFN','Artskill','MrSavage','Floki','Juu','default','Рutrick','Raifla','FuryLegendary','Skram','iRezUmi','Refsgaard','Gabix','Noahreyli','Hookka','Benjyfishy','Belusi','pkr','Swifty','Zroqz','aqua','Swag','Hijoe','klown','Link','Grolzz','Stompy','Nakoo','Trippernn','Kinzell','DaaN','zAndy','Nebs','Zeston','Alexcod','Dyox','Vicotryona','Wafflar','RELLVIS','Shmeky','Endretta','Flickzy','Kylie','Kikoo','YikesJxn','Bubak','Kefyy','Hellfire','Wox','Karmy','Huty','Flodax','NeFrizi','Milad','MoSh','OvLDER','Karma','Mlody','Fastroki','Neylu','cheatiin','Swillium','LeTsHe','Crusti','Kayn','Snayzy','shizogod','FlowiS','Flikk','IDrop','nayte','Matsoe','Jureky','Umplify','Slender','Safik','wakie','Voidd','Michael','Crow','AstroSMZ','EsTyftn','verox','airknn','Hycris','Xsterioz','ETq','Hottie','zeykoo','Joseeh','Packo','Adn','Nikof','Shaykoz','Grayinjo','shadowfn','Blacky','Saevid','Siberiajkee','Keziix','elokratz','Night','Slovay','Mawakha','Skite','Krizzii','RedRush','Commandment','Mero','Deyy','Cented','Khanada','Degen','Jahq','Acorn','Slackes','Stretch','Ajerss','Edgey','skqttles','nosh','Tragix','MackWood','Bucke','Bugha','Avery','Chukky','nut','Jamper','Saf','illest','Rise','Reverse','Threats','Clix','Justice','Kreo','Dusky','Dukez','Whofishy','Eomzo','PeterBot','Teyo','Voil','Speguu','Cazz','DeRoller','Charlie','Snake','Rocaine','Tahi','PaMstou','Aspect','paper','Dom','Nani','Userz','Ceice','Chimp','Tkay','Zlem','Sprite','Dubs','Squish','narwhal','Fatch','Xccept','Okis','Fryst','Kwah','casqer','clarityG','Plege','Scoped','Osp','RogueShark','TabzG','Bully','Joji','wCarey','Cold','Nittle','Megga','blakeps','Knight','Tabnae','Visxals','Durant','Kn1pher','Neeqo','Nexy','smqcked','Crumble','Bizzle','Gabe','Doniee','Avivv','Magnolia','Muz','Goku','PXMP','Pxlarized','Susscript','Marzz','Eclipsae','Crunchy','Smite']
path = "./chromedriver.exe"

driver = webdriver.Chrome(path)
driver.set_window_position(-1000, 0)


def maincycle():
    driver.set_window_position(-1000, 0)
    driver.get("https://mywordle.strivemath.com/")
    time.sleep(1)

    pyautogui.typewrite(random.choice(namess))
    pydirectinput.press('enter')

    select = Select(driver.find_element_by_id('cars'))
    select.select_by_value('any')

    link = driver.find_element_by_partial_link_text('https://mywordle.strivemath.com')
    link.click()
    driver.set_window_position(0, 0)

maincycle()

count = 0

while True:
    time.sleep(3)
    try:
        continuebutton = driver.find_element_by_xpath('//button[text()="Make Your Own Wordle"]')
        maincycle()
    except:
        count = count + 1
        print(f"not it - {count}")