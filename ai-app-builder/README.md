<!-- markdownlint-disable MD030 -->


# AgenticProtocol - Build LLM Apps Easily

### Prerequisites

* Meta Mask extension [installed](https://support.metamask.io/getting-started/getting-started-with-metamask/) on your web browser
a new EVM account for development purposes.
* A Citrea devnet [account](https://docs.citrea.xyz/user-guide/how-to-use-bridge) for creating NFT
* Some [Citrea devnet tokens](https://docs.citrea.xyz/user-guide/how-to-use-bridge) on the account you are using.
* Create a Lighthouse [API Key](https://docs.lighthouse.storage/lighthouse-1/quick-start#create-an-api-key) for uploading JSON file to FileCoin storage

### Setup

  

1. Clone the repository

  

```bash

git clone https://github.com/likaho/AgenticProtocol.git

```

  

2. Go into individual repository folder, for example ai-app-builder

  

```bash

cd AgenticProtocol/ai-app-builder

```

  

3. Install all dependencies of all modules:

  

```bash

pnpm install

```

  

4. Build all the code:

  

```bash

pnpm build

```

5. Create .env files  

- Create `.env` file and specify the `VITE_PORT` and other environment variables (refer to `.env.example`) in `packages/ui`

```bash
cp .env.example .env
```

- Create `.env` file and specify the `PORT` and other environment variables (refer to `.env.example`) in `packages/server`

```bash
cp .env.example .env
```

 - Edit .env file
 - Set LIGHTHOUSE_API_KEY to an API key of Lighthouse storage account
 - Set PRIVATE_KEY to the private key of Citrea devnet account 


6. Start the app:


- Run


```bash

pnpm start

```

  

Any code changes will reload the app automatically on [http://localhost:3031](http://localhost:3031)

  

6. For development build:

  

```bash

pnpm run dev

```

  

You can now access the app on [http://localhost:3032](http://localhost:3032)
  
  
## Run Docker 
### 1. Create .env files and private keys:

- Create `.env` file and specify environment variables (refer to `.env.example`) in `packages/ui`

    ```bash
    cp .env.example .env
    ```

- Create `.env` file and specify environment variables (refer to `.env.example`) in `packages/server`

    ```bash
    cp .env.example .env
    ```

 - Edit .env file
 - Set LIGHTHOUSE_API_KEY to an API key of Lighthouse storage account
 - Set PRIVATE_KEY to the private key of Citrea devnet account 


### 2. Build a docker image:

```bash
docker build -t ai-app-builder .
```

### 3. Run a docker container:

```bash
docker run --name ai-app-builder -p 3031:3031 ai-app-builder
```  

## 🙋 Support

Feel free to ask any questions, raise problems, and request new features in [discussion](https://github.com/likaho/agenticprotocol/discussions)

## 🙌 Contributing

Thanks go to these awesome original creators of Flowise.ai

## 📄 License

Source code in this repository is made available under the [Apache License Version 2.0](LICENSE.md).
