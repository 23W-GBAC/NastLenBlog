# replace_placeholders.py
import requests
from generate_facts_about_animals import generate_random_animal_fact

def replace_fact_placeholder(file_names):
    random_fact = generate_random_animal_fact()
    data = []
    for file_name in file_names:

        with open(file_names, "rt", encoding="utf-8") as file:
            for line in file:
                if "Did you know? **" in line:
                    data.append(f"Did you know? **{random_fact}**\n")
                else:
                    data.append(line)

        with open(file_names, "wt", encoding="utf-8") as file:
            file.writelines(data)

        print("Updated content:")
        print(random_fact)
    
if __name__ == '__main__':
    replace_fact_placeholder(['Second_Post.md', 'Third_Post.md', 'Fourth_Post.md'])
