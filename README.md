# Asahi-Scrape

 This is a script to scrape data from a legislative candidate
 [survey](https://www.asahi.com/senkyo/shuinsen/2021/asahitodai/) that was published online via Asahi Shimbun in the leadup
 to the 2021 general elections in Japan. 



 There are over 25,000 observations to record from the survey, spread 
 across roughly 800 pages. The script collects these observations and 
 saves them into a CSV file. 

 I use a webdriver (Selenium) because the site uses session cookies to 
 autheticate users on every single page (over 800) that's requested.
 You'll need to first create a free account on the site, using Chrome as
 your browser, and then revisit the main survey page before running 
 the script.

 The script navigates to each candidate's page direcly via a URL, rather
 than making Selenium interact with the site's nav system, and scrapes 
 these pages in a loop. The URLs were scraped in a seperate script and
 saved to a CSV file (cands_urls.csv), which is imported here. This is 
 much faster and more reliable approach as it avoids the intermediary 
 steps of switching window tab focus and clicking on nav buttons for
 every new set of candidates.  

 I use artificial time delays to be more friendly to Asahi's server, 
 with randomly generated time intervals to make the requests seem human. 
