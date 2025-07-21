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

## workflows
- non-agentic workflow - v straightforward - input to output
- agentic workflow - gets feedback from the environment and iterates to get better results
  - fully autonomous agents haven't happened yet
- accuracy falls as the complexity/number of steps increase
  - that's why agents work best when they have a singular puprose, narrow scope 
> the future of how we interact with 
## ways to build 
1. no-code/lowcode - n8n, flowise, bubble, replit
    - less customisation, subscription fees
2. from scratch
   - frameworks: langchain, llmaindex (by meta, for documents), crewai, openai agent sdk