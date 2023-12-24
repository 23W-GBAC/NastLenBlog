# replace_placeholders.py
from generate_facts_about_animals import generate_random_animal_fact

def replace_fact_placeholder(file_url):
    random_fact = generate_random_animal_fact()

    response = requests.get(file_url)

    if response.status_code == 200:
        content = response.text

        updated_content = content.replace("[Random Animal Fact]", random_fact)

        with open("output.md", "w", encoding="utf-8") as file:
            file.write(updated_content)

        print("Updated content:")
        print(updated_content)
    else:
        print(f"Failed to retrieve content from {file_url}")
