## Blog Post 3: Final Solution

### At the end I decided to choose my own strategy and develop 2 essential Python Scripts for my Automation Project. Especally some articles written on "BuiltIn" helped me to figure out how to manage ordered and unordered lists in Python : 

<p float="left"> 
  <img src="images_of_animals/Screenshot.png" alt="Alt Text" width="300" align="right">
</p>

<hr>

**The [generate_facts_about_animals.py](https://github.com/23W-GBAC/NastLenBlog/blob/main/generate_facts_about_animals.py) script** retrieves facts from the chosen website.


### Some Commands and Functionality for generate_facts_about_animals.py

#### Libraries Imported:

- requests: Used for making HTTP requests to the website to fetch content.
- BeautifulSoup: A library for web scraping, employed to parse the HTML content and extract relevant information.

#### Function generate_random_animal_fact():

- Establishes a connection to the specified website and retrieves the HTML content.
- Utilizes BeautifulSoup to locate and extract animal facts from the HTML structure.
- Randomly selects one fact from the obtained list and returns it.

#### Execution in __main__ block:

- Calls the generate_random_animal_fact() function.
- Prints the randomly selected animal fact to the console.


**Advantages**:

- The script fetches animal facts from a website, ensuring that your blog always has fresh and engaging content. This enhances reader interest and provides a continuously evolving experience.

- The script automates the process of retrieving facts, saving you time and effort that would be required to manually search for and update facts in each blog post.

- The use of random.choice() ensures that the facts inserted into your posts are diverse, preventing repetitive or monotonous content.

- The script checks for the success of the HTTP request and gracefully handles cases where the retrieval of facts fails.


**Disadvantages**:

- The script relies on the external website for content. If the website structure changes or becomes unavailable, the script might fail.

- Since the facts are fetched from an external source, you have limited control over the specific facts that are retrieved. This might result in occasional irrelevant or less contextually fitting content.

<hr>

Another my .py skript **file [replace_placeholders.py](https://github.com/23W-GBAC/NastLenBlog/blob/main/replace_placeholders.py)** seamlessly replaces designated placeholders in my blog posts with dynamically generated facts.

### Some Commands and Functionality:
#### Libraries Imported:

- requests: Similar to the other script, used for making HTTP requests to fetch content.
- generate_random_animal_fact: Importing the function from your first script for obtaining random animal facts.

#### Function replace_fact_placeholder(file_names):

- Accepts a list of file names (your blog posts in Markdown format).
- For each file, reads its content line by line.
Searches for a specific placeholder (**"Did you know? **"**) and replaces it with the dynamically generated animal fact.
- Writes the updated content back to the file.

#### Execution in __main__ block:

- Calls replace_fact_placeholder() with a list of your blog posts (['[Second_Post.md](https://github.com/23W-GBAC/NastLenBlog/blob/main/Second_Post.md)', '[Third_Post.md](https://github.com/23W-GBAC/NastLenBlog/blob/main/Third_Post.md)', '[Fourth_Post.md](https://github.com/23W-GBAC/NastLenBlog/blob/main/Fourth_Post.md)']).
- Prints the updated content to the console.
<hr>
Additional Notes:
This script is designed to be run after creating your blog posts, ensuring that the placeholders are correctly positioned in your Markdown files.
