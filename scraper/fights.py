from bs4 import BeautifulSoup
import requests

def main():

    fight_file = open('../files/fight_links.txt', 'w')

    with open('../files/event_links.txt', 'r') as event_links:
        for index, event_link in enumerate(event_links):
            print(f"{index}: {event_link}")

            event_page = requests.get(event_link[:-1]).content

            soup = BeautifulSoup(event_page, "html.parser")

            event_date = soup.find("li", {"class": "b-list__box-list-item"})
            fights = soup.find_all("tr", {"class": "b-fight-details__table-row__hover"})

            print(event_date.text.strip("\n ")[6:].strip("\n "))
            fight_file.write(f"{event_date.text.strip("\n ")[6:].strip("\n ")}\n")

            for fight in fights:
                print(f"\t{fight['data-link']}")
                fight_file.write(f"{fight['data-link']}\n")
            
    fight_file.close()

if __name__ == "__main__":
    main()
