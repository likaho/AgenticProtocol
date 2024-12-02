
<!-- markdownlint-disable MD030 -->

  
  


# Agentic Protocol 
Welcome to Agentic Protocol - An open platform for the new AI economy.  It is a Decentralized Agentic Protocol No-Code Building Tool & Marketplace.

## Overview

- This innovative platform empowers creators and developers to build and own their AI agents.


  

### There are five main directories in this repo:

  

1.  **chat-ui**: This folder is dedicated to the chat web client.

2.  **llm-server**: This folder contains an Express web service that handles requests from llm-proxy-server service. It forwards prompts to the Gemma2-27b model.

3.  **agents**: Here, you'll find all agents using DataGemma.

4.  **ai-app-builder**: The ai-app-builder folder includes both client and server-side projects. It provides a no-code agent building tool and serves as the marketplace.

5.  **llm-proxy-server**: In this folder, you'll find Python scripts responsible for function calling. They act as a proxy, deciding which tool or agent to call or redirecting calls to the Gemma2-27b model.

  
  


**Microservice Architecture**
<img width="100%" src="https://github.com/likaho/AgenticProtocol/blob/main/images/microservice_architecture.gif">

### Agent Creation

Our Decentralized Agentic Protocol No-Code Building Tool is an innovative platform that empowers creators and developers.

### Agent Flow Creation Tutorial

[![Agentic Protocol Tutorial - How to Build AI Agent Teams](https://github.com/likaho/AgenticProtocol/blob/main/images/research_team_agent.gif)](https://www.youtube.com/watch?v=284Z8k7yJRE "Agentic Protocol Tutorial - How to Build AI Agent Teams")


### Quick Tutorial - Custom LLM Flow Registration

[![Agentic Protocol Tutorial - Register a customized LLM flow](https://github.com/likaho/AgenticProtocol/blob/main/images/agent_demo.gif)](https://www.youtube.com/watch?v=bKunFksvWnw "Agentic Protocol Tutorial - Register a customized LLM flow")


- **Agent Discovery and Tool Use:**
  - Finally, a new chat flow acts like a tool for other agents after it is listed in the marketplace. It will be automatically discovered. LLMs can benefit from tool use to perform more complex tasks. Tools allow LLMs to trigger actions.

<img width="100%" src="https://github.com/likaho/AgenticProtocol/blob/main/images/agent_discovery_service.gif">


### Agent Inference

The user prompt is transmitted to our marketplace, where the appropriate tool or tools are selected to fulfill the request.

<img width="100%" src="https://github.com/likaho/AgenticProtocol/blob/main/images/agent_discovery_flowchart.gif">



## Getting Started

### Prerequisites

* Docker installed on your system
* Docker Compose installed on your system

### Running the Project
  

1. Clone the repository
  

```bash

git clone https://github.com/likaho/AgenticProtocol-Gemma.git

```

  

2. Go into individual directory, create .env file 


- Go into ai-app-builder/packages/server/ directory


```bash

cd AgenticProtocol/ai-app-builder/packages/server/
cp .env.example .env

```



- Go into ai-app-builder/packages/ui/ directory


```bash

cd AgenticProtocol/ai-app-builder/packages/ui/
cp .env.example .env

```


- Go into llm-proxy-server directory


```bash

cd AgenticProtocol/llm-proxy-server
cp .env.example .env

```


 - Edit .env file
 - Set OPENAI_KEY to an API key of OpenAI account


- Go into llm-server directory

```bash

cd AgenticProtocol/llm-server
cp .env.example .env

```


  

3. Start the apps and services:

  

```bash

cd AgenticProtocol
docker-compose up -d

```

  

You can now access the AI builder app on [http://localhost:3031](http://localhost:3031)
- Username: user
- Password: 1234


And chat-ui on [http://localhost:3000](http://localhost:3000)

  
  
  

## 🙋 Support

  

Feel free to ask any questions, raise problems, and request new features in [discussion](https://github.com/likaho/agenticprotocol/discussions)

  

## 🙌 Contributing

  

Thanks go to these awesome original creators of Flowise.ai

  

## 📄 License

  

Source code in this repository is made available under the [Apache License Version 2.0](LICENSE.md).
