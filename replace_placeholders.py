# replace_placeholders.py
from generate_facts_about_animals import generate_random_animal_fact

def replace_fact_placeholder(file_path):
    random_fact = generate_random_animal_fact()

    with open(file_path, "r", encoding="utf-8") as file:
        content = file.read()

    updated_content = content.replace("[Random Animal Fact]", random_fact)

    with open(file_path, "w", encoding="utf-8") as file:
        file.write(updated_content)

if __name__ == "__main__":
    replace_fact_placeholder("https://raw.githubusercontent.com/23W-GBAC/NastLenBlog/main/Second_Post.md")
    replace_fact_placeholder("third.md")
    replace_fact_placeholder("fourth.md")
