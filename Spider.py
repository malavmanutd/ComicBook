import requests, time, os
from bs4 import BeautifulSoup
from selenium import webdriver

driver = webdriver.Chrome(r'C:\Users\iis.B201-55\Desktop\chromedriver')
driver.get('https://www.comicextra.com/comic-list')
# time.sleep(15)
dict = {

}
list = driver.find_elements_by_xpath('/html/body/main/div/div/div/div[1]/div/div[3]/div/ul/li/a')
list2 = driver.find_elements_by_xpath('/html/body/main/div/div/div/div[1]/div/div[4]/div/ul/li/a')
i = 0





for l in list:
    i += 1
    print(i)
    folder_name = str(i) + '). ' + l.text.replace(':', '').replace('/', '-').replace('?', '').replace('&',
                                                                                                      'and').replace(
        '\\',
        '-').replace(
        '<', '').replace('>', '').replace('*', '').replace('|', '').replace('"', '').replace("'", "")

    print('E:/temp/' + folder_name)
    try:
        os.mkdir('E:/temp/' + folder_name)
        source_code = requests.get(l.get_attribute("href"))
        #  print(source_code)
        plain_text = source_code.text
   
            # print(plain_text)
        soup = BeautifulSoup(plain_text, "html.parser")
        chaps = soup.find_all('tr')
   
        for c in chaps:
            a = c.find('td')
            sub_folder = []
            chap_name = str(a.text.replace(':', '').replace('/', '-').replace('#', '').replace('&', 'and').replace('\\',
                                                                                                                       '-').replace(
                    '<', '').replace('>', '').replace('*', '').replace('|', '').replace('"', '').replace("'", "").replace(
                    '\xa0', ' '))
            sub_folder.append(('E:/temp/' + folder_name + '/' + chap_name[1:]).rstrip('\n'))
                #print(chap_name)
            print(sub_folder[0])
            try:
                os.mkdir(sub_folder[0])
            except:
                pass
            source_code = requests.get(a.find('a').get('href'))
                #  print(source_code)
            plain_text = source_code.text
   
                # print(plain_text)
            soup = BeautifulSoup(plain_text, "html.parser")
            if soup.find('div', {'class': 'label1'}):
                number_of_pages = soup.find('div', {'class': 'label1'})
   
                number_of_pages = number_of_pages.text[3:]
                    # print(number_of_pages)
                for j in range(1, int(number_of_pages)):
                        # print(a.find('a').get('href') + '/' + str(i))
                    file1 = open(sub_folder[0] + "/myfile.txt", "a")
                    file1.writelines(a.find('a').get('href') + '/' + str(j) + '\n')
                    file1.close()
    except:
        pass
   



   

# print(list.text)
#spider(dict)
