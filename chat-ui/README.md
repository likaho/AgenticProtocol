### 1. Installation

Clone the repository:

```bash
git clone https://github.com/likaho/AgenticProtocol.git
cd AgenticProtocol/chat-ui
```

### 2. Install all dependencies of all modules:

```bash
npm install
```

### 3. Run Server:

```bash
npm run dev
# or
yarn dev
# or
pnpm dev
```

The server app should be running on http://localhost:3000

## Run Docker 
### 1. Build a docker image:

```bash
docker build -t chat-ui .
```

### 2. Run a docker container:

```bash
docker run --name chat-ui -p 3000:3000 chat-ui
```