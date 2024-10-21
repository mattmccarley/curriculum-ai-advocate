# Prework 1: Setup
## Environment Setup

### 5-Minute Setup Walkthrough for Key Development Tools
In this course, we’ll be using Python. If you’ve never used Python before, don’t worry. Nothing that we do here will be super deep, but using Python provides a common place for all of us to work in during class. We will also be leveraging AI tools to help us develop code, so you don’t need to be expert or even be experienced in Python to get the most out of this course.

Outside of class, if you want to build AI apps using other languages, we will be providing extra code examples in JavaScript, Java, Ruby, and C++ for you to use. 

#### Setting Up the Cursor
Cursor is the best AI coding tool currently out there. It will greatly increase the speed at which you develop any application. We will go over how to use Cursor to get the most out of this course and out of your own development workflow.
1. Download from https://www.cursor.com/

#### Setting Up UV
An extremely fast Python package and project manager, written in Rust.
1. Open https://docs.astral.sh/uv/
2. Run `curl -LsSf https://astral.sh/uv/install.sh | sh` for Mac of `powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"` for Windows
   ```bash
   pip install uvicorn
   ```
2. Verify installation by running:
   ```bash
   uvicorn --version
   ```
#### Installing Python  
1. uv python install

#### Installing Pip 
Pip is a Python package manager used to install Python libraries.

1. Pip is automatically included with Python. To check if it’s installed, open terminal/command prompt and type:
   ```bash
   pip --version
   ```

#### Setting Up a Python Project

1. Open a new folder in Cursor
2. Open the terminal in Cursor and run
 ```bash
 uv venv venv
 ```

3. To activate the environment:
   - **Windows**:  
     ```bash
     .\venv\Scripts\activate
     ```
   - **Mac/Linux**:  
     ```bash
     source venv/bin/activate
     ```
4. To deactivate, simply run:
   ```bash
   deactivate
   ```

#### Getting an OpenAI API Key
We will be using the OpenAI API for much of our work. 

1. Visit the [OpenAI API website](https://platform.openai.com/).
2. Sign up or log in.
3. Navigate to the API section, generate a new API key, and save the API key to your local machine.