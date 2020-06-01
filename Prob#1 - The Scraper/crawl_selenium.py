from selenium import webdriver
import csv
bannLINK = []
bannData = []
driver = webdriver.Firefox()
driver.get("https://rubnongkaomai.com/baan/")
driver.implicitly_wait(2)
selectSize = driver.find_elements_by_xpath('//div[@role="tab"]')
for size in selectSize:
    size.click()
bannLink = driver.find_elements_by_xpath("//a[contains(@href, '/baan/')]")
for i in bannLink:
    bannLINK.append(i.get_attribute('href'))
for link in bannLINK:
    nowbannLINK = link
    driver.get(nowbannLINK)
    bannName = driver.find_elements_by_xpath('//h1[@type="header"]')
    bannDesc = driver.find_elements_by_xpath('//h3[@type="header"]')
    bannData.append([bannName[0].text,bannDesc[0].text])
driver.close()
f = open("text.txt","w",encoding="UTF-8")
f.write('Baan#Slogan\n')
for i in range(len(bannData)):
    f.write(str(bannData[i][0])+'#')
    Slogan = bannData[i][1].split("\n")
    for j in range(len(Slogan)-1):
        f.write(str(Slogan[j])+'^')
    f.write(str(Slogan[len(Slogan)-1])+"\n")
f.close()



