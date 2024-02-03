## Blog Post 2: Possible Solutions and errand attempts to develop a solution

The next step for me was to start looking for some educational sourses. I found a rich source of facts at [emdonenilodge.com](https://www.emdonenilodge.com/50-best-fun-random-facts-animals/) and crafted two Python scripts to address these goals.


There have been at least three solutions of how we can implement my **Auto-Generator of Facts about Animals**:

### 1. Static Fact Database:

**Description**: The concept of a static fact database involves creating a local repository or spreadsheet containing a predetermined set of animal facts. These facts would be manually curated, and the script would reference this database during the blog post creation.

**Pros**:
- Reduced need for online fetching in real-time. By having a local database, the script wouldn't need to make real-time requests to external websites for facts, potentially improving efficiency.
- Easier organization and management of facts. A pre-built database allows for a structured and organized approach to fact storage..
**Cons**:
- Limited to the facts in the database. The major drawback lies in the limited scope of facts available. The database would only contain the facts that have been manually inserted, restricting the variety and spontaneity of the content..
- Still requires manual effort for insertion. Despite having a database, the process of selecting and inserting facts into the blog posts would still require manual effort, defeating the purpose of complete automation.

### 2. External API Integration:

**Description**: The second approach involves exploring and integrating external APIs that provide random animal facts. The script would make API calls to fetch these facts, thereby ensuring a diverse range of content.

**Pros**:
- Potential for a diverse range of facts. By tapping into external APIs, the auto-generator gains access to a potentially extensive and varied pool of animal facts, enhancing the richness of content.
- Automation through API calls. The script can be programmed to make API calls automatically, streamlining the process of fetching facts.
**Cons**:
- Dependency on third-party APIs. Relying on external APIs introduces a dependency on their availability and stability. Any changes or disruptions to these APIs could impact the functionality of the auto-generator.
- May require API key management and potential costs. Some APIs may require authentication keys or come with usage limits, leading to potential costs and key management challenges.


### 3. Interactive User Input:

**Description**: The third approach centers around incorporating an interactive user input system into the blog post creation process. While writing, the user would manually input facts, aided by a user interface or prompts.

**Pros**:
- Retains control over the facts. This approach provides complete control to the user, ensuring that only desired and accurate facts are included.
- Adds an interactive element to the writing process. The inclusion of user input adds an interactive layer to the writing process, making it engaging and personalized.
**Cons**:
- Still involves manual input. Despite the interactive element, the process still involves manual input. This goes against the core idea of full automation, requiring the user to actively participate in generating content.
- Limited to the facts you are aware of or find during the writing process. The variety of facts is limited to what the user knows or discovers during the writing process, potentially reducing the diversity of content.

<hr>
Each solution presents its own trade-offs, balancing between automation and manual involvement. The decision hinges on the desired level of control, diversity of facts, and the balance between automated efficiency and human interaction. For my blog on Pets and Animals, the chosen solution involved real-time fetching from a dynamic online source, as it aligned with the goal of providing fresh and intriguing content in each post. The next blog post in this series will delve into my **final solution**.
