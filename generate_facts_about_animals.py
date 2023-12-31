# generate_facts.py
import requests
from bs4 import BeautifulSoup
import random

def generate_random_animal_fact():
    url = "https://www.emdonenilodge.com/50-best-fun-random-facts-animals/"
    response = requests.get(url)
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, "html.parser")
        fact_elements_section = soup.find_all("section", class_="entry-content cf")
        fact_elements = fact_elements_section[0].find_all("li")
        facts = [fact.get_text() for fact in fact_elements]
        return random.choice(facts)
    else:
        return "Failed to retrieve animal facts."
    
if __name__ == "__main__":
    random_fact = generate_random_animal_fact()
    print("Random Animal Fact:")
    print(random_fact)
