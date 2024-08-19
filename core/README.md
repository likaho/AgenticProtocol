<!-- markdownlint-disable MD030 -->


# AgenticProtocol - Build LLM Apps Easily


### Setup

  

1. Clone the repository

  

```bash

git clone https://github.com/likaho/AgenticProtocol.git

```

  

2. Go into individual repository folder, for example core

  

```bash

cd AgenticProtocol/core

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
  
  
  

## 🙋 Support

Feel free to ask any questions, raise problems, and request new features in [discussion](https://github.com/likaho/agenticprotocol/discussions)

## 🙌 Contributing

Thanks go to these awesome original creators of Flowise.ai

## 📄 License

Source code in this repository is made available under the [Apache License Version 2.0](LICENSE.md).
