# 🦾 AI Agents 

## what are ai agents
- anything that can perceive the environment and act upon it
  - agents can be software/hardware (like cars, manufacturing machines)
  - environment can be road (for cars), game env (for gameplay agents)
  - gather information - in software it could be text, voice, images and sensors, cameras for hardware
  - agent then does something with the information obtained (browsing the web, creating files, etc)
- standard definitions focus on llm powered ai agents
- sense-think-act loop
- eg.: chatgpt, claude-sonnet
- use cases: customer chatbot agent, coding agent, writing agent
> "ai agents will be the future of how we interact with computers"

## workflows
- non-agentic workflow - like a straight line - input to output
- agentic workflow - gets feedback from the environment and iterates to get better results
  - fully autonomous agents haven't happened yet (as of july 2025)
- don't have to hardcode the workflow - agents can figure out what to do next based on our natural language prompt
- currently, accuracy falls as the complexity/number of steps increase
  - that's why agents work best when they have a singular puprose, narrow scope 

## ways to build 
1. no-code/lowcode - n8n, flowise, bubble, replit
    - less customisation, subscription fees
2. from scratch
   - frameworks: langchain, llmaindex (by meta, for documents), crewai, openai agent sdk