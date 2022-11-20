import time
import random
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import csv

PATH = '/Users/boaty_mcboatface/Desktop/chromedriver'
options = webdriver.ChromeOptions()
options.add_argument("user-data-dir=/Users/boaty_mcboatface/Library/Application Support/Google/Chrome/Default")
driver = webdriver.Chrome(PATH, options=options) 
driver.get('https://digital.asahi.com/senkyo/shuinsen/2021/asahitodai/?_requesturl=senkyo/shuinsen/2021/asahitodai/');
wait_v_short = round(random.uniform(0.1,0.6), 2)
wait_long = round(random.uniform(4,5), 2)
time.sleep(wait_long) 

all_cands = []

def write_cands():
	with open("cands2.csv", "w") as file:
		headers = [
			"name",
			"age",
			"party",
			"dist",
			"status",
			"defense_strength",
			"preemtive_strike",
			"north_korea",
			"nuclear_3_no",
			"futenma",
			"anpo",
			"china",
			"social_services",
			"public_works",
			"fiscal_stimulus",
			"consumption_tax",
			"competitiveness",
			"income_tax",
			"corporate_tax",
			"competitiveness",
			"protectionism",
			"bonds",
			"constitution",
			"immigration",
			"privacy",
			"fukushima",
			"marriage_name",
			"traditional_marriage",
			"lgbt",
			"nuclear",
			"malapportionment"
			]
		csv_writer = csv.DictWriter(file,fieldnames=headers)
		csv_writer.writeheader()
		for cand in all_cands:
			csv_writer.writerow(cand)

def scrape_cand():
	profile = driver.find_element(By.ID, "koho_Profile")
	dd_tags_p = profile.find_elements(By.TAG_NAME, "dd")
	answers = driver.find_element(By.ID, "koho_Answer")
	dd_tags = answers.find_elements(By.TAG_NAME, "dd")
	all_cands.append({
		"name": profile.find_element(By.CLASS_NAME, "name").text,
		"age": dd_tags_p[0].find_element(By.TAG_NAME, "p").text,
		"party": dd_tags_p[1].find_element(By.TAG_NAME, "p").text,
		"dist": dd_tags_p[2].find_element(By.TAG_NAME, "p").text,
		"status": dd_tags_p[3].find_element(By.TAG_NAME, "p").text,
		"defense_strength": dd_tags[0].find_element(By.TAG_NAME, "div").text,
		"preemtive_strike": dd_tags[1].find_element(By.TAG_NAME, "div").text,
		"north_korea": dd_tags[2].find_element(By.TAG_NAME, "div").text,
		"nuclear_3_no": dd_tags[3].find_element(By.TAG_NAME, "div").text,
		"futenma": dd_tags[4].find_element(By.TAG_NAME, "div").text,
		"anpo": dd_tags[5].find_element(By.TAG_NAME, "div").text,
		"china": dd_tags[6].find_element(By.TAG_NAME, "div").text,
		"social_services": dd_tags[7].find_element(By.TAG_NAME, "div").text,
		"public_works": dd_tags[8].find_element(By.TAG_NAME, "div").text,
		"fiscal_stimulus": dd_tags[9].find_element(By.TAG_NAME, "div").text,
		"consumption_tax": dd_tags[10].find_element(By.TAG_NAME, "div").text,
		"income_tax": dd_tags[11].find_element(By.TAG_NAME, "div").text,
		"corporate_tax": dd_tags[12].find_element(By.TAG_NAME, "div").text,
		"competitiveness": dd_tags[13].find_element(By.TAG_NAME, "div").text,
		"protectionism": dd_tags[14].find_element(By.TAG_NAME, "div").text,
		"bonds": dd_tags[15].find_element(By.TAG_NAME, "div").text,
		"constitution": dd_tags[16].find_element(By.TAG_NAME, "div").text,
		"immigration": dd_tags[17].find_element(By.TAG_NAME, "div").text,
		"privacy": dd_tags[18].find_element(By.TAG_NAME, "div").text,
		"fukushima": dd_tags[19].find_element(By.TAG_NAME, "div").text,
		"marriage_name": dd_tags[20].find_element(By.TAG_NAME, "div").text,
		"traditional_marriage": dd_tags[21].find_element(By.TAG_NAME, "div").text,
		"lgbt": dd_tags[22].find_element(By.TAG_NAME, "div").text,
		"nuclear": dd_tags[23].find_element(By.TAG_NAME, "div").text,
		"malapportionment": dd_tags[24].find_element(By.TAG_NAME, "div").text 
		})


with open("cands_urls.csv", "r") as file:
	csv_reader = csv.reader(file)
	poop = list(csv_reader)
all_cand_urls = []
for url in poop:
	all_cand_urls.append(''.join(url))

for url in all_cand_urls:
	driver.get(url);
	time.sleep(wait_v_short)
	try:
		profile = WebDriverWait(driver, 30).until(
			EC.presence_of_element_located((By.ID, "koho_Profile"))
		)
		scrape_cand()
		time.sleep(wait_v_short)
	except:
		pass
write_cands()




