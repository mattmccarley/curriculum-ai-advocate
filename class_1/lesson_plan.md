# LLMs

## Introduction

## Core Competencies

- How LLMs work and how it affects our prompts
- Understand the various types of LLM messages
- Zero/one/few shot prompts
- Context and prompts
- Give the LLM more context than you think
- Structured outputs

Examples
- File Ingestion - Category Selector
- Few shot
- Context is King
- Movie reviews
- Model variation
- Prompts change based on the LLM
- Prompt Optimizer
- LLMs creating their own prompts


### The student must demonstrate...

1. 

## Class Sections

1. **Whole Task: What We'll be Doing**
   
   - **Core Competency:** 
        Understanding the big picture of this course. 
   
   - **Relevance:** 
        You're in this course to become an AI advocate. What does an AI advocate do? What is their role and what value do they bring? How do I influence my team/department/team when it comes to AI? Many other questions may exist, and this section will show you what that's like at a 10,000 ft level. 
   
   - **Procedure:**
      1. Overview of what an AI advocate needs to know about AI
        - course overview
      2. How to start influencing your team. 
        - Adding "AI" to your job title can be particularly impactful here
        - educate your team on relevant AI topics
        - explain what is possible with AI
        - teach others on how to think about AI projects
      3. Lead project development projects
        - AI projects are different than other software engineering projects
            - datasets and evaluations (to measure output and success)
            - expertise on the process we're automating at hand is required (you're not necessarily the expert)
            - feedback systems and continual maintanance
                - human in the loop
                - llm feedback
                - prompt optimization
            - Knowing when to use AI and when not to


   - **Code:**
        Chart of everything we need to do and how we advocate for each part (mind map of curiculum with an extra box on how to talk about it with the team)


1. **What LLMs actually bring to the table**
   
   - **Core Competency:** 
        - How LLMs work and how it affects our prompts
        - Understand the various types of LLM messages
        - Understanding the capabilities of simple LLMs and their real use cases
   
   - **Relevance:** 
        LLMS are the foundational tool in generative AI apps. Using LLMs effectively goes beyond simple prompting, but to understand how it works, it helps to know the principles behind how LLMs work. These principles also make it easier to identify LLM use cases back at the office.

   
   - **Procedure:**
      1. High level overview of how LLMs work
        - tokens
        - generation
        - training
      2. LLM message roles
        - system, user, assistant
        - chat history and it's impact
      3. Use cases:
        - anything where a human reads something and then produces something as a result
        - file ingestion
        - responding to reviews
        - code generation
        - extracting dates (what are LLMs bad at vs good at; don't use AI when you can do the same thing easier using something else)

   - **Code:**
    
    - **Check For Understanding:** 

1. **Title**
   
   - **Core Competency:** 
        - Zero/one/few shot prompts
        - Context and prompts
        - Give the LLM more context than you think
   
   - **Relevance:** 
   Prompting strategies help the LLM produce the best outputs. Some of these strategies like zero/few shot may seem trivial today, but understanding why they work will higlight. More complex strategies like chain of thought have opened new opportunities to what LLMs are capable of. Regardless of the strategy, they all follow one critical LLM principle: tokens are predicting based on the prompt and what has already been generated. 
   
   - **Procedure:**
    1. Quick example of zero/one/few shot prompts
        - highlight that I rarely use zero, I often use one, and occasionally I use few shot prompts.
    2. Show how context impacts the results
        - proprietary data is what makes your AI apps powerful
        - genearlly better to add more context than is needed
    3. Ship it!
        - A good prompt likely needs context. Identify who owns the context and bring them onto the project.

   - **Code:**
    
    - **Check For Understanding:** 

1. **Structured outputs**
   
   - **Core Competency:** 
        - Structured outputs
   
   - **Relevance:** 
    Nearly all LLMs these days follow structure instructions really well, and this is good; we can pull specific data out if it's structured correctly. We'll cover APIs that are specific for structured output, but you don't need them. In fact, many prompts I've seen that need structure often have the structure as part of their prompt.
   
   - **Procedure:**
      1. Chain of Thought
        - structure and effectiveness
        - The principle that LLMs predict the next token by when was given and what was already produced is highlighted strongly by this prompting idea. We can leverage this to produce better outputs in our apps
      2. Ship it!
        - Use structure to extract specific pieces of information.

   - **Code:**
    - movie review example
    
    - **Check For Understanding:** 


### Challenge 1: 

**Objective:** 

## Conclusion




