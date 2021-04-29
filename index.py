
#imports here
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
import time

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
username.send_keys("trungnguyen228804@gmail.com")
password.clear()
password.send_keys("Family#228801!@")

#target the login button and click it
button = WebDriverWait(driver, 2).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button[type='submit']"))).click()

#We are logged in!
time.sleep(6)
images = []

for i in ['photos_all', 'photos_albums']:
	driver.get("https://www.facebook.com/profile.php?id=100064642727317&sk="+i)
	time.sleep(10)
	n_scrolls = 2
	for j in range(1, n_scrolls):
		driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
		time.sleep(5)

		anchors = driver.find_elements_by_tag_name('a')
		anchors = [a.get_attribute('href') for a in anchors]
		anchors = [a for a in anchors if str(a).startswith("https://www.facebook.com/photo")]
		# print(anchors)
		for a in anchors:
			driver.get(a)
			time.sleep(6)
			img = driver.find_elements_by_tag_name("img")
			images.append(img[1].get_attribute("src"))
			
images
import os
import wget
path = os.getcwd()
path = os.path.join(path, "ScrapedPhotos" )

#create the directory
os.mkdir(path)

path


# #download images
counter = 0
for image in images:
    save_as = os.path.join(path, str(counter) + '.jpg')
    wget.download(image, save_as)
    counter += 1

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