## Prerequisites

* Learn how to use the shell/terminal/console/bash on your device
  * Get familiar with basic commands like `cd`, `ls` and `mkdir`
  * Learn how to execute packages, scripts and commands on your device
* Install python tools on your device
  * [Python](https://www.python.org/downloads/)
  * [Pip](https://pip.pypa.io/en/stable/installation/)
* Install python tools on your device
  * [Python](https://www.python.org/downloads/)
  * [Pip](https://pip.pypa.io/en/stable/installation/)  
* Troubleshoot how to install `sqlite` as part of `ChromaDB` requirements
  * Docs: [SQLite](https://docs.trychroma.com/troubleshooting#sqlite)
* Learn how to use `venv` to create and manage virtual environments
  * Docs: [Python venv](https://docs.python.org/3/library/venv.html)

  ### 1. Installation

Clone the repository:

```bash
git clone https://github.com/likaho/AgenticProtocol.git
cd AgenticProtocol/llm-proxy-server
```
### 2. Create virtual environment in bash shell in Linux:

```bash
python3 -m venv venv
source ./venv/bin/activate
```

### 3. Install all dependencies of all modules:

```bash
pip install -r requirements.txt
```

### 4. Create environment variables:

Create `.env` file and specify environment variables (refer to `.env.example`) in `llm-proxy-server`

```bash
cp .env.example .env
```

### 5. Run Server:

```bash
python3 app.py
# or for Windows
py app.py
```

The server app should be running on http://localhost:8080


## Run Docker 
### 1. Create environment variables:

Create `.env` file and specify environment variables (refer to `.env.example`) in `llm-proxy-server`

```bash
cp .env.example .env
```

### 2. Build a docker image:

```bash
docker build -t llm-proxy-server .
```

### 3. Run a docker container:

```bash
docker run --name llm-proxy-server -p 8080:8080 llm-proxy-server
```
