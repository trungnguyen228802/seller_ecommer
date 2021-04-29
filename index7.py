
#imports here
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
import time
import random
# connect mysql
import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  passwd="",
  database="data_facebook"
)
mycursor = mydb.cursor()



#thank you pythonjar

chrome_options = webdriver.ChromeOptions()
prefs = {"profile.default_content_setting_values.notifications" : 2}
chrome_options.add_experimental_option("prefs",prefs)

#specify the path to chromedriver.exe (download and save on your computer)
driver = webdriver.Chrome('./chromedriver.exe', chrome_options=chrome_options)

#open the webpage
driver.get("http://www.facebook.com")

#target username
username = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "input[name='email']")))
password = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "input[name='pass']")))

#enter username and password
username.clear()
username.send_keys("0365424126")
password.clear()
password.send_keys("Family#228801!@")

#target the login button and click it
button = WebDriverWait(driver, 2).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button[type='submit']"))).click()

#We are logged in!
time.sleep(6)
images = ["https://www.facebook.com/groups/505458450201812/members", "https://www.facebook.com/groups/3396320380473206/members", "https://www.facebook.com/groups/dhtm.group/members"]
for page in images:
	driver.get(page)
	time.sleep(16)

	# for j in range(1, 3):
	# 	driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
	# 	time.sleep(5)
	# 	# div_name = driver.find_elements_by_tag_name("a")
	# 	div_name = driver.find_element_by_css_selector(".rq0escxv.l9j0dhe7.du4w35lb.j83agx80.cbu4d94t.buofh1pr.tgvbjcpo.muag1w35.enqfppq2")
	# 	# div_name = driver.find_elements_by_css_selector(".ow4ym5g4.auili1gw.rq0escxv.j83agx80.buofh1pr.g5gj957u.i1fnvgqd.oygrvhab.cxmmr5t8.hcukyx3x.kvgmc6g5.nnctdnn4.hpfvmrgz.qt6c0cv9.jb3vyjys.l9j0dhe7.du4w35lb.bp9cbjyn.btwxx1t3.dflh9lhu.scb9dxdr")
	# 	name_user = div_name.find_elements_by_tag_name("a")
	# 	for user in name_user:
	# 		name_id = str(user.get_attribute("aria-label"))
	# 		# if name_id in globals() or name_id in locals() :
	# 		# 	name_id='null'
	# 		href = user.get_attribute("href")
	# 		print("name:"+name_id+"- link:"+str(href))
	# 		sql = "INSERT INTO tbl_user_id (user_link, user_name) VALUES (%s, %s)"
	# 		val = (href, name_id)
	# 		mycursor.execute(sql, val)

	# 		mydb.commit()

	n_scrolls = 300
	l=0
	for j in range(1, n_scrolls):
		driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
		time.sleep(2)
		print(l)
		l+=1
	# time.sleep(15)
	# div_name = driver.find_element_by_css_selector(".rq0escxv.l9j0dhe7.du4w35lb.j83agx80.cbu4d94t.pfnyh3mw.d2edcug0.aahdfvyu.tvmbv18p")
	div_name = driver.find_elements_by_css_selector(".rq0escxv.l9j0dhe7.du4w35lb.j83agx80.cbu4d94t.buofh1pr.tgvbjcpo.muag1w35.enqfppq2")
	print(len(div_name));
	K=0
	for item_name in div_name:
		name_user = item_name.find_elements_by_tag_name("a")
		print(len(name_user))
		for user in name_user:
			name_id = str(user.get_attribute("aria-label"))
			if name_id=="None":
				name_id ="None"
			href = user.get_attribute("href")
			print("name:"+name_id+"- link:"+str(href))
			sql = "INSERT INTO tbl_user_id (user_link, user_name) VALUES (%s, %s)"
			val = (href, name_id)
			mycursor.execute(sql, val)
			mydb.commit()
		print(K)
		K+=1

# print("den lan thu:"+m)
driver.close()
		# print("link:"+href)
	# print(div_name);
	# anchors = driver.find_elements_by_tag_name('a')
	# for url in anchors:
	# 	print(url)
	# anchors = [a.get_attribute('href') for a in anchors]
	# anchors = [a for a in anchors if str(a).startswith("href="https://www.facebook.com/hades.laanh"")]

	# for k in div_name:
	# 	list_name = k.find_elements_by_tag_name("a")
	# 	for item_name in list_name:
	# 		href = item_name.get_attribute("href")
	# 		print(href)


# for i in ['photos_all', 'photos_albums']:
# 	driver.get("https://www.facebook.com/profile.php?id=100064642727317&sk="+i)
# 	time.sleep(10)
# 	n_scrolls = 2
# 	for j in range(1, n_scrolls):
# 		driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
# 		time.sleep(5)

# 		anchors = driver.find_elements_by_tag_name('a')
# 		anchors = [a.get_attribute('href') for a in anchors]
# 		anchors = [a for a in anchors if str(a).startswith("https://www.facebook.com/photo")]
# 		# print(anchors)
# 		for a in anchors:
# 			driver.get(a)
# 			time.sleep(6)
# 			img = driver.find_elements_by_tag_name("img")
# 			images.append(img[1].get_attribute("src"))
			
# images
# import os
# import wget
# path = os.getcwd()
# path = os.path.join(path, "ScrapedPhotos" )

# #create the directory
# os.mkdir(path)

# path


# #download images
# counter = 0
# for image in images:
#     save_as = os.path.join(path, str(counter) + '.jpg')
#     wget.download(image, save_as)
#     counter += 1

# #nadle NOT NOW
# not_now = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//button[contains(text(), "Not Now")]'))).click()
# not_now2 = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//button[contains(text(), "Not Now")]'))).click()


# #search keywords
# import time

# #target the search input field
# searchbox = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//input[@placeholder='Search']")))
# searchbox.clear()

# #search for the hashtag cat
# keyword = "#cat"
# searchbox.send_keys(keyword)
 
# # Wait for 5 seconds
# time.sleep(5)
# searchbox.send_keys(Keys.ENTER)
# time.sleep(5)
# searchbox.send_keys(Keys.ENTER)
# time.sleep(5)

# #scroll down to scrape more images
# driver.execute_script("window.scrollTo(0, 4000);")

# #target all images on the page
# images = driver.find_elements_by_tag_name('img')
# images = [image.get_attribute('src') for image in images]
# images = images[:-2]

# print('Number of scraped images: ', len(images))


# # Save images to computer¶
# # First we'll create a new folder for our images somewhere on our computer.
# # Then, we'll save all the images there.

# import os
# import wget

# path = os.getcwd()
# path = os.path.join(path, keyword[1:] + "s")

# #create the directory
# os.mkdir(path)

# path


# #download images
# counter = 0
# for image in images:
#     save_as = os.path.join(path, keyword[1:] + str(counter) + '.jpg')
#     wget.download(image, save_as)
#     counter += 1