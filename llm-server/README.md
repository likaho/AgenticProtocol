# AgenticProtocol - llm-server

## Overview

AgenticProtocol integrates decentralized AI capabilities using various APIs for enhanced functionality. This backend contains scripts for deploying and interacting with smart contracts to intergate with a LLM model via an Oracle.

## Getting Started

### Prerequisites

- Node.js and npm installed on your machine.
- An Ethereum account with some testnet ETH for deployment.
- Environment variables set in `.env` file.

### 1. Installation

Clone the repository:

```bash
git clone https://github.com/likaho/AgenticProtocol.git
cd AgenticProtocol/llm-server
```

### 2. Install all dependencies of all modules:

```bash
npm install
```

### 3. Create environment variables:

Create `.env` file and specify environment variables (refer to `.env.example`) in `llm-server`

```bash
cp .env.example .env
```
 - Edit .env file
 - Set PRIVATE_KEY to the private key of Galadriel devnet account 

### 4. Create a private key for sending transactions to Galadriel Network:


### 5. Run Server:

```bash
npm start
```

The server app should be running on http://localhost:3001


## Run Docker 
### 1. Create environment variables:

Create `.env` file and specify environment variables (refer to `.env.example`) in `llm-server`

```bash
cp .env.example .env
```
 - Edit .env file
 - Set PRIVATE_KEY to the private key of Galadriel devnet account 


### 2. Build a docker image:

```bash
docker build -t llm-server .
```

### 3. Run a docker container:

```bash
docker run --name llm-server -p 3001:3001 llm-server
```