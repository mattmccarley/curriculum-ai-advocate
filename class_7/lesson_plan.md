# Agents

## Introduction


## Core Competencies

AI workers completing tasks autonomously
Agent control and effectiveness

Topics covered:
Agentic lifecycle
ReAct prompt pattern
Building agents and function calling

Examples:
PBM chatbot
Wikipedia agent

### The student must demonstrate...

1. They understand the agentic lifecycle
2. They can build a funcitoning agent
3. They can plan out how an agent should come together
4. The can observe an agent

## Coding Problems

1. **Agent Overview**
   
   - **Core Competency:** Understand how agents work and when to use them
   
   - **Relevance:** Agents are the hot topic for generative AI. They promise to produce incredible results, and while the promise is not yet realized in every use case, makers of LLMs are training their LLMs to be used in agentic apps. 
   
   - **Procedure:**
      1. Show the agent map and talk about the different parts
      1. Explain tools as functions that the agent can call

   - **Code:**
    
    - **Check For Understanding:** 

1. **Function Calling**
   
   - **Core Competency:** Have the LLM supply the argumetns for a function
   
   - **Relevance:** For agents to actually work with anything internal, we need it to call functions. We can supply a list of functions and their parameters to help it do this. 
   
   - **Procedure:**
      1. Function calling with OpenAI
      1. Function calling with LangChain
      1. Explain the ReAct prompt and how it leans into a structured output. Talk about how the "thought" summarizes your output to produce the right tool.

   - **Code:**
    
    - **Check For Understanding:** 

1. **Planning an Agent**
   
   - **Core Competency:** Identify the tasks needed for the agent to be effective
   
   - **Relevance:** Agents are very novel, and as such, we need to know some good practices to help us build effective ones
   
   - **Procedure:**
      1. The great thing is that the best practices we've addressed also work with agents: context gathering, action, and verify (agent-in-the-loop?) steps
      1. Context gathering
      2. Argument buildling
      3. Verify arguments
      2. Action

   - **Code:**
    
    - **Check For Understanding:** 

1. **Observing Agent**
   
   - **Core Competency:** Learn to see where agents go off track
   
   - **Relevance:** Agents in LangSmith have a lot of information that is worth breaking down 
   
   - **Procedure:**
      1. Identify an agent call
      2. See the react prompt in action
      3. See the tool calls
      4. Cost of agents is something we need to note
      
   - **Code:**
    
    - **Check For Understanding:** 

1. **Evaluating Agents**
   
   - **Core Competency:** Evaluate agents so you can tune the prompts
   
   - **Relevance:** Agents in LangSmith have a lot of information that is worth breaking down 
   
   - **Procedure:**
      1. What do you test? Trajectory - is the agent calling the expected tools in order
      2. Evaluate the agents performance and adjust as needed
      
   - **Code:**
    
    - **Check For Understanding:** 


### Challenge 1: 

**Objective:** 

## Conclusion

