import re, requests, os, sys
from time import time as timer	
from multiprocessing.dummy import Pool
from colorama import Fore								
from colorama import Style
####### Colors	 ######	
fr  =   Fore.RED											
fc  =   Fore.CYAN											
fw  =   Fore.WHITE											
fg  =   Fore.GREEN											
sd  =   Style.DIM											
sn  =   Style.NORMAL										
sb  =   Style.BRIGHT
										
#######################

def banners():
    try:
        os.mkdir('CMS')
    except:
        pass
        
    banner = """{}

                   ...          
                 ;::::;           ::
               ;::::; :;        :::::: 
              ;::::;  :;   CMS Scanner
             ;:::::'   :;     By RaiC0d3r
            ;:::::;     ;.
           ,:::::'       ;           OOO\
           ::::::;       ;          OOOOO\{}
           ;:::::;       ;         OOOOOOOO
          ,;::::::;     ;'         / OOOOOOO
        ;:::::::::`. ,,,;.        /  / DOOOOOO
      .';:::::::::::::::::;,     /  /     DOOOO
     ,::::::;::::::;;;;::::;,   /  /        DOOO
    ;`::::::`'::::::;;;::::: ,#/  /          DOOO
    :`:::::::`;::::::;;::: ;::#  /            DOOO  {}
    ::`:::::::`;:::::::: ;::::# /              DOO
    `:`:::::::`;:::::: ;::::::#/               DOO
     :::`:::::::`;; ;:::::::::##                OO
     ::::`:::::::`;::::::::;:::#                OO
     `:::::`::::::::::::;'`:;::#                O
      `:::::`::::::::;' /  / `:#
       ::::::`:::::;'  /  /   `#                                                                                            

		\n""".format(fg, fr, fg, sn)
		
    print(banner)


def getoption():
    print("{}[1]{} Single Site".format(fg, fw))
    print("{}[2]{} Multiple Site".format(fg, fw))
    choiceoption=input('Put Number => ')
    if choiceoption=='1':
        url = input("\n\033[92m[!]\033[91m ENTER WEBSITE : ")
        cmsfilter(url)
        
    elif choiceoption=='2':
        start_raw = input("\n\033[92m[!]\033[91m ENTER LIST OF WEBSITES : ")
        try:
            with open(start_raw, 'r') as f:
                url = f.read().splitlines()
        except IOError:
            pass
        start = timer()
        ThreadPool = Pool(100)
        Threads = ThreadPool.map(cmsfilter, url)
        print('PrivateBot Finished in : ' + str(timer() - start) + ' seconds')

def cmsfilter(url):
	
	
    try:
        if requests.get(url + "/administrator/manifests/files/joomla.xml", verify=False).status_code == 200:
            joomla = requests.get(url + "/administrator/manifests/files/joomla.xml", verify=False)
            joomla_version = re.findall('<version>(.*?)<\/version>', joomla.text)
            print("\033[0m[$] \033[92mURL:",url)
            print("\033[0m[!]\033[92m Found Version: " + joomla_version[0])
            print("\033[0m[!]\033[92m CMS: Joomla")
            open('CMS/Joomla.txt', 'a').write(url+'\n')
        elif requests.get(url + "/language/en-GB/en-GB.xml", verify=False).status_code == 200:
            joomla = requests.get(url + "/language/en-GB/en-GB.xml", verify=False)
            joomla_version = re.findall('<version>(.*?)<\/version>', joomla.text)
            print("[$] URL:",url)
            print("\033[0m[!]\033[92m Found Version: " + joomla_version[0])
            print("\033[0m[!]\033[92m CMS: Joomla")
            open('CMS/Joomla.txt', 'a').write(url+'\n')
    except:
        pass
    try:
        Checktwo = requests.get(url, timeout=5)
        if "/wp-content/" in Checktwo.text.encode('utf-8'):
            print('[{}Site]: {} {}	  ==> {}{} WordPress     {}{} Detected  '.format(sb, sd, url, fc,fc, sb,fg))
            open('CMS/Wordpress.txt', 'a').write(url+'\n')
        else:
            print(''.format(sb, sd, url, fc,fc, sb,fr))
    except:
        pass
    try:
        Checktwo = requests.get(url, timeout=5)
        if "/sites/default/" in Checktwo.text.encode('utf-8'):
            print('[{}Site]: {} {}	  ==> {}{} Drupal     {}{} Detected  '.format(sb, sd, url, fc,fc, sb,fg))
            open('CMS/Drupal.txt', 'a').write(url+'\n')
    except:
        pass	
    try:		
        Checktwo = requests.get(url, timeout=5)
        if "prestashop" in Checktwo.text.encode('utf-8'):
            print('[{}Site]: {} {}	  ==> {}{} Prestashop     {}{} Detected  '.format(sb, sd, url, fc,fc, sb,fg))
            open('CMS/Prestashop.txt', 'a').write(url+'\n')
    except:
        pass
    try:		
        CheckOsc = requests.get(url + '/admin/images/cal_date_over.gif')
        CheckOsc2 = requests.get(url + '/admin/login.php')
        if 'GIF89a' in CheckOsc.text.encode('utf-8') or 'osCommerce' in CheckOsc2.text.encode('utf-8'):
            print('[{}Site]: {} {}	  ==> {}{} osCommerce     {}{} Detected  '.format(sb, sd, url, fc,fc, sb,fg))
            open('CMS/osCommerce.txt', 'a').write(url+'\n')
    except:
        pass
    try:		

        Checktree = requests.get(url + '/application/configs/application.ini')

        if "APPLICATION_PATH" in Checktree.text.encode('utf-8'):
            print('[{}Site]: {} {}	  ==> {}{} CMS Zen     {}{} Detected  '.format(sb, sd, url, fc,fc, sb,fg))
            open('CMS/zen.txt', 'a').write(url+'\n')
    except:
        pass
    try:		
		
        Checktwo = requests.get(url, timeout=5)

        if "Magento" in Checktwo.text.encode('utf-8'):
            print('[{}Site]: {} {}	  ==> {}{} Magento     {}{} Detected  '.format(sb, sd, url, fc,fc, sb,fg))
            open('CMS/Magento.txt', 'a').write(url+'\n')					
    except:
        pass
    try:		
		
        Checktwo = requests.get(url, timeout=5)

        if "OpenCart" in Checktwo.text.encode('utf-8'):
            print('[{}Site]: {} {}	  ==> {}{} OpenCart     {}{} Detected  '.format(sb, sd, url, fc,fc, sb,fg))
            open('CMS/OpenCart.txt', 'a').write(url+'\n')					
    except:
        pass
    try:		
		
        Checktwo = requests.get(url, timeout=5)

        if "vBulletin" in Checktwo.text.encode('utf-8'):
            print('[{}Site]: {} {}	  ==> {}{} vBulletin     {}{} Detected  '.format(sb, sd, url, fc,fc, sb,fg))
            open('CMS/vBulletin.txt', 'a').write(url+'\n')					
    except:
        pass
banners()
getoption()


