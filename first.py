import requests
from bs4 import BeautifulSoup
from time import sleep


headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.0.0 Safari/537.36"}

for count in range(1, 8):

    sleep(3)
    url = f"https://scrapingclub.com/exercise/list_basic/?page={count}"

    response = requests.get(url, headers=headers)

    soup = BeautifulSoup(response.text, "lxml")

    data = soup.find_all("div", class_="col-lg-4 col-md-6 mb-4")

    for i in data:

        name = i.find("h4", class_="card-title").text.strip("\n")
        price = i.find("h5").text
        url_img = "https://scrapingclub.com" + i.find("img", class_="card-img-top img-fluid").get("src")

        print(name + "\n" + price + "\n" + url_img + "\n\n")

