## Blog Post 1: Problem and Context of the Automation

#### I’ve always been fascinated by animals, and as I began writing my first about human interaction with animals [*human interaction with animals*](https://github.com/23W-GBAC/NastLenBlog/blob/main/First_Post.md), I realised that there is a good opportunity to improve my educational blog by adding some entertaining and interesting facts about creatures. This thought sparked the idea of creating an auto-generator of intriguing facts about animals.
<hr>
We know that it might be rather time-consuming to manually search for new facts that we want to provide in our articles. Imagine having to manually sift through numerous websites, articles, and resources to find the most interesting and relevant information for each article you write. Moreover, using a manual search increases the likelihood of discovering the same facts over and over again. Such repetition not only reduces the novelty of the content, but can also lead to a lack of variety in the facts presented, potentially turning off the audience.In light of these challenges, the need for a more efficient and streamlined approach becomes clear. The decision to start down the automation path is driven by a desire to overcome these obstacles while ensuring that we continually provide fresh, diverse, and accurate facts about animals without compromising the quality of the blog's educational content. 

<hr>

So what if we will try to kill two birds with one stone: implement the solution which would not only save time but also represent the educational value of the overall blog? 
 
 ### For this I set the next objectives

- [x] Find a suitable website containing facts about animals
- [x] Read the necessary data from this site
- [x] Organize the facts in the form of an unordered list
- [x] Insert one random fact into each post (starting from the second one)

There were several challenges I faced with. I have been trying to figure out for a long time how can we extract one specific fact from the website and integrate it in one particular post. For this task I read some articles about managing the ordered/unordered lists and the opportunities of web scraping with the help of the great tool called “Inspect Element”. This exploration was especially crucial in developing a strategy to fetch relevant data from a chosen website. Leveraging my existing coding skills, I crafted the generate_facts_about_animals.py script to retrieve facts from a reliable source, ensuring accuracy and reliability. Before I had some experience of working with HTML, CSS, and low-level languages. Despite this, it was a more nuanced approach. 

**Why Python?**
Python is well-known for its simplicity, readability, and structures which almost anyone can comprehend. Of course, it’s not the best in terms of speed (compared to low-level languages), but for small projects and applications it would be more than enough. Besides, Pyhton’s ability to manipulate and manage lists was proved invaluable. Through careful coding, I ensured that the resulting facts retained their original format and were easily integrated into the narrative structure of my blog posts. The use of indentation to denote blocks of code not only enforces a clean and organized structure but also eliminates the need for excessive punctuation, making Python code visually intuitive. This readability aspect is especially beneficial for beginners, easing the learning curve and promoting a smooth transition into the programming realm.
Therefore, writing a script in Python and applying my knowledge was a manageable task. 

Automating the creation of animal facts not only simplified the content creation process, but also added a dynamic element to each post. The ability to provide fresh and varied facts for each article increased reader engagement, creating a sense of curiosity and excitement.

**In conclusion**, the problem and context of automation in my blog is rooted in the desire to supplement educational content with fun facts about animals. The problems of manual fact-finding were solved by using Python scripts, using web scraping techniques, and "Inspect Element" capabilities. The result is an effective autogenerator that not only simplifies the content creation process, but also enriches the reader's experience with many fascinating facts about animals. Join me in the next post where I will share the solutions explored and the evolution of this automation path.


