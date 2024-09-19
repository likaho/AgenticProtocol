
<!-- markdownlint-disable MD030 -->

  
  


# Agentic Protocol 
Welcome to Agentic Protocol - An open platform for the new AI economy.  It is a Decentralized Agentic Protocol No-Code Building Tool & Marketplace.

## Overview

- This innovative platform empowers creators and developers to build and own their AI agents.
- Creators mint non-fungible tokens (NFTs) to establish ownership of their agents, providing verifiable proof of authenticity.
- By accepting token payments via an ERC20 contract, creators can monetize their agents directly.
- The agent's blueprint is securely stored within the Filecoin storage network, ensuring immutable ownership.
- Citrea enables agent creators to mint unique NFTs that prove authorship of AI agents.
- These NFTs allow monetization through token (AGEN) payments from users via an ERC20 contract.
- Decentralized node owners can deploy these agents on a decentralized network and earn AGEN Tokens.
- Galadriel ensures agent integrity by providing zkML proofs of inference. These proofs validate agent behavior, especially when using LLMs.

The combination of FileCoin, NFTs, and zkML creates a powerful ecosystem for AI agents!


  

### There are five main directories in this repo:

  

1.  **chat-ui**: This folder is dedicated to the chat web client.

2.  **llm-server**: This folder contains an Express web service that handles requests from llm-proxy-server service. It forwards prompts to the Galadriel network.

3.  **contracts**: Here, you'll find all the NFT (AGENTL) and ERC20 (AGEN) contracts.

4.  **ai-app-builder**: The ai-app-builder folder includes both client and server-side projects. It provides a no-code agent building tool and serves as the marketplace.

5.  **llm-proxy-server**: In this folder, you'll find Python scripts responsible for function calling. They act as a proxy, deciding which tool or agent to call or redirecting calls to the Galadriel network.

  
  

## Technologies Were Used

The project leverages three key components: Filecoin, Citrea, and the Galadriel network.

**Microservice Architecture**
<img width="100%" src="https://github.com/likaho/AgenticProtocol/blob/main/images/microservice_architecture.gif">

1. **Filecoin (Lighthouse):**
   - Filecoin is a decentralized storage network designed to store important information globally.
   - In the context of our project, Filecoin serves as the storage infrastructure for agent-related data.

2. **Citrea:**
   - Citrea enables agent creators to mint unique non-fungible tokens (NFTs, symbol: AGENTL) that prove their authorship of AI agents.
   - These NFTs allow creators to monetize their agents by accepting token (AGEN) payments from users via an ERC20 contract.
   - The agent's definition is stored within the Filecoin storage network, providing proof of ownership.
   - Additionally, decentralized node owners can deploy these agents on a decentralized network and earn AGEN Token.

3. **Galadriel Network:**
   - The Galadriel network plays a crucial role in ensuring agent integrity.
   - It provides zero-knowledge machine learning (zkML) proofs of inference.
   - These proofs validate the correctness and reliability of agent behavior, especially when using large language models (LLMs).

In summary, Citrea and Filecoin collaborate to empower agent creators, while the Galadriel network enhances agent security and reliability.


### Agent Creation

Our Decentralized Agentic Protocol No-Code Building Tool is an innovative platform that empowers creators and developers.

### Agent Flow Creation Tutorial

[![Agentic Protocol Tutorial - How to Build AI Agent Teams](https://github.com/likaho/AgenticProtocol/blob/main/images/research_team_agent.gif)](https://www.youtube.com/watch?v=284Z8k7yJRE "Agentic Protocol Tutorial - How to Build AI Agent Teams")


<h3>Register a customized LLM flow and publish it onto Citrea Network and Lighthouse storage</h3>

### Quick Tutorial - Custom LLM Flow Registration

[![Agentic Protocol Tutorial - Register a customized LLM flow](https://github.com/likaho/AgenticProtocol/blob/main/images/agent_demo.gif)](https://www.youtube.com/watch?v=bKunFksvWnw "Agentic Protocol Tutorial - Register a customized LLM flow")


- **Minting NFTs on Citrea Network:**
  - Publish the chat flow definition and mint unique NFTs on the Citrea network.
  - By minting NFTs, creators establish ownership of their AI agents. These tokens serve as verifiable proof of authenticity.
  - Creators can monetize their agents by accepting token payments from users via an ERC20 contract. It’s a direct way to earn rewards for your work.

- **Storing Definitions on Filecoin:**
  - The agent’s definition—the blueprint for your AI agent—is securely stored within Lighthouse, one of the Filecoin storage providers.

- **Agent Discovery and Tool Use:**
  - Finally, a new chat flow acts like a tool for other agents after it is listed in the marketplace. It will be automatically discovered. LLMs can benefit from tool use to perform more complex tasks. Tools allow LLMs to trigger actions.

<img width="100%" src="https://github.com/likaho/AgenticProtocol/blob/main/images/agent_discovery_service.gif">

This decentralized approach ensures that ownership remains provable and immutable.

### Agent Inference

The user prompt is transmitted to our marketplace, where the appropriate tool or tools are selected to fulfill the request.

<img width="100%" src="https://github.com/likaho/AgenticProtocol/blob/main/images/agent_discovery_flowchart.gif">


- **Using Galadriel Network for zkML Proofs:**
  - Once confirmed, our default gateway redirects the prompt to the Galadriel Network via Oracle. zkML inference is performed to validate the integrity of the inference. 

## Getting Started

### Prerequisites

* Docker installed on your system
* Docker Compose installed on your system
* Meta Mask extension [installed](https://support.metamask.io/getting-started/getting-started-with-metamask/) on your web browser
* A Galadriel devnet [account](https://docs.galadriel.com/setting-up-a-wallet). We recommend creating a new EVM account for development purposes.
* Some [Galadriel devnet tokens](https://docs.galadriel.com/faucet) on the account you are using.
* A Citrea devnet [account](https://docs.citrea.xyz/user-guide/how-to-use-bridge) for creating NFT
* Some [Citrea devnet tokens](https://docs.citrea.xyz/user-guide/how-to-use-bridge) on the account you are using.
* Create a Lighthouse [API Key](https://docs.lighthouse.storage/lighthouse-1/quick-start#create-an-api-key) for uploading JSON file to FileCoin storage

### Running the Project
  

1. Clone the repository
  

```bash

git clone https://github.com/likaho/AgenticProtocol.git

```

  

2. Go into individual directory, create .env file 


- Go into ai-app-builder/packages/server/ directory


```bash

cd AgenticProtocol/ai-app-builder/packages/server/
cp .env.example .env

```


 - Edit .env file
 - Set LIGHTHOUSE_API_KEY to an API key of Lighthouse storage account
 - Set PRIVATE_KEY to the private key of Citrea devnet account 


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

 - Edit .env file
 - Set PRIVATE_KEY to the private key of Galadriel devnet account 


  

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
