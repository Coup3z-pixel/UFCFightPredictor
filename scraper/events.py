from bs4 import BeautifulSoup
import requests

def main(): 
    events_page = requests.get("http://ufcstats.com/statistics/events/completed?page=all").content

    soup = BeautifulSoup(events_page, "html.parser")

    event_links = soup.find_all("a", {"class": "b-link"})
    event_dates = soup.find_all("span", {"class": "b-statistics__date"})
    event_links = event_links[1:] # skips the first due to web page design

    with open('../files/event_links.txt', 'w') as f:
        for link, date in zip(event_links, event_dates):
            print(link.get("href"))
            print(date.get_text())

            f.write(f"{link.get("href")}\n")
    
if __name__ == "__main__":
    main()
