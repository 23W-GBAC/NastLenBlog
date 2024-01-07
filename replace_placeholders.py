# replace_placeholders.py
import requests
from generate_facts_about_animals import generate_random_animal_fact

def replace_fact_placeholder(file_names):
    data = []
    for file_name in file_names:

        random_fact = generate_random_animal_fact().strip()

        with open(file_name, "rt", encoding="utf-8") as file:
            for line in file:
                if "Did you know? **" in line:
                    data.append(f"Did you know? **{random_fact}**\n")
                else:
                    data.append(line)

        with open(file_name, "wt", encoding="utf-8") as file:
            file.writelines(data)

        print("Updated content:")
        print(random_fact)
        data.clear()
        print('Hello world')
    
if __name__ == '__main__':
    replace_fact_placeholder(['Second_Post.md', 'Third_Post.md', 'Fourth_Post.md'])
