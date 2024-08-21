<!-- markdownlint-disable MD030 -->

# AgenticProtocol UI

English 

React frontend ui for AgenticProtocol.

1. Install all dependencies of all modules:

  

```bash

pnpm install

```

  

2. Build all the code:

  

```bash

pnpm build

```

  

3. Start the app:

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

- Run

  

```bash
cd AgenticProtocol/ai-app-builder/packages/ui/
pnpm dev

```

  

Any code changes will reload the app automatically on [http://localhost:3032](http://localhost:3032)

  

## 🙋 Support

Feel free to ask any questions, raise problems, and request new features in [discussion](https://github.com/likaho/agenticprotocol/discussions)

## 🙌 Contributing

Thanks go to these awesome original creators of Flowise.ai

## 📄 License

Source code in this repository is made available under the [Apache License Version 2.0](https://github.com/likaho/AgenticProtocol/blob/master/LICENSE.md).
