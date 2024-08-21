<!-- markdownlint-disable MD030 -->


# AgenticProtocol - Build LLM Apps Easily


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

  

5. Start the app:

  

- Create `.env` file and specify the `VITE_PORT` and other environment variables (refer to `.env.example`) in `packages/ui`

- Create `.env` file and specify the `PORT` and other environment variables (refer to `.env.example`) in `packages/server`

```bash
cp .env.example .env
```

- Run


```bash

pnpm dev

```

  

Any code changes will reload the app automatically on [http://localhost:3032](http://localhost:3032)

  

6. For production build:

  

```bash

pnpm start

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

- Create a private key

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
