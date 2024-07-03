
<!-- markdownlint-disable MD030 -->

  
  

# AgenticProtocol - Build LLM Apps Easily

  

### There are five main directories in your project:

  

1.  **chat-ui**: This folder is dedicated to the chat web client.

2.  **contracts**: Here, you'll find all the NFT (AGENTL) and ERC20 (AGEN) contracts.

3.  **core**: The core folder includes both client and server-side projects. It provides a no-code agent building tool and serves as the marketplace.

4.  **function_calling_llm**: In this folder, you'll find Python scripts responsible for function calling. They act as a proxy, deciding which tool or agent to call or redirecting calls to the Galadriel network.

5.  **galadriel**: This folder contains an Express web service that handles chat services. It forwards prompts to the Galadriel network.

  
  

### For the Core Project Setup

  

1. Clone the repository

  

```bash

git clone https://github.com/likaho/AgenticProtocol.git

```

  

2. Go into repository folder

  

```bash

cd AgenticProtocol

```

  

3. Install all dependencies of all modules:

  

```bash

pnpm install

```

  

4. Build all the code:

  

```bash

pnpm build

```

  

5. Start the app:

  

```bash

pnpm start

```

  

You can now access the app on [http://localhost:3000](http://localhost:3000)

  

6. For development build:

  

- Create `.env` file and specify the `VITE_PORT` (refer to `.env.example`) in `packages/ui`

- Create `.env` file and specify the `PORT` (refer to `.env.example`) in `packages/server`

- Run

  

```bash

pnpm dev

```

  

Any code changes will reload the app automatically on [http://localhost:8080](http://localhost:8080)

  
  
  

## 🙋 Support

  

Feel free to ask any questions, raise problems, and request new features in [discussion](https://github.com/likaho/agenticprotocol/discussions)

  

## 🙌 Contributing

  

Thanks go to these awesome original creators of Flowise.ai

  

## 📄 License

  

Source code in this repository is made available under the [Apache License Version 2.0](LICENSE.md).