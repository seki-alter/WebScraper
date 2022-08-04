import requests
from bs4 import BeautifulSoup
import time

""" URL = "https://www.petycjeonline.com/"
page = requests.get(URL) """

def scrape():

    for page_num in range(1,5):
        URL = "https://www.petycjeonline.com/browse.php?order_by=stats_signatures_last_24_hours&page_number="+str(page_num)
        page = requests.get(URL)
        soup = BeautifulSoup(page.content, "html.parser")
        results = soup.find(id="main")

        petitions = results.find_all("h2")[1:]

        for petition in petitions:
            title_element = petition.find("a")
            url_element = "https://www.petycjeonline.com"+petition.find_all("a")[0]["href"]
            print(title_element.text)
            print(f"Podpisz petycję: {url_element}\n")

if __name__ == "__main__":
    while True:
        scrape()
        time_wait = 5
        print(f"Czekam {time_wait} minut...")
        time.sleep(time_wait*60)