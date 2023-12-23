# replace_placeholders.py

def replace_fact_placeholder(file_path, random_fact):
    with open(file_path, "r", encoding="utf-8") as file:
        content = file.read()

    updated_content = content.replace("[Random Animal Fact]", random_fact)

    with open(file_path, "w", encoding="utf-8") as file:
        file.write(updated_content)

if __name__ == "__main__":

    replace_fact_placeholder("Second_Post.md", random_fact)
    replace_fact_placeholder("third.md", random_fact)
    replace_fact_placeholder("fourth.md", random_fact)
