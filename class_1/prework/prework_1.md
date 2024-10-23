# Prework: 5-Minute Environment Setup Walkthrough

In this course, we’ll be using Python. If you’ve never used Python before, don’t worry. We will provide most of the code you'll need. We use Python to provide a common place for all of us to work in during class. We will also be leveraging AI tools to help us develop code, so you don’t need to be expert or even be experienced in Python to get the most out of this course.

Outside of class, if you want to build AI apps using other languages, we will be providing extra code examples in JavaScript and Java for you to use. 

#### Setting Up Your IDE with Cursor
Cursor is an IDE with embedded AI tools. These tools increase development output and will expose you to good AI UX. We will discuss later in this course how to get the most out of Cursor and how it effects the development workflow. For now, let's just get it installed.

1. Go to https://www.cursor.com/
2. Click the download button, which will download the install package to your computer. Open the package to install Cursor.
3. Once installed, make sure you can open Cursor. 

#### Setting Up UV
UV is an extremely fast Python package and project manager, written in Rust. We’ll use this to install Python packages we need (including Python itself). 

1. Open your terminal and run the following command:
- Mac: `curl -LsSf https://astral.sh/uv/install.sh | sh` 
- Windows: `powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"`
2. Follow the instructions to add it to your PATH.
3. Restart your terminal.

#### Installing Python  
We'll use the latest Python version for this course. 
With UV, this one is easy. 
1. Run `uv python install` in your terminal. 

#### Installing Pip 
Pip is a Python package manager used to install Python libraries.

1. Pip is automatically included with Python. To check if it’s installed, open terminal/command prompt and type:
   ```bash
   pip --version
   ```

#### Get an OpenAI API Key
We will be using the OpenAI API to access LLMs in our code. 

1. Visit the [OpenAI API website](https://platform.openai.com/).
2. Sign up or log in.
3. Click [here to open the API Keys section](https://platform.openai.com/api-keys) and generate a new API key (you may need to verify your phone number first). Make sure to copy the key.
4. Now you'll save the API key to an environment variable.

   <details>
   <summary>On Mac:</summary>

   - Open your `.bash_profile` file with a text editor: `open ~/.bash_profile`
   - Add the line `export OPENAI_API_KEY={your key}`
   - Save the file and close it

   </details>

   <details>
   <summary>On Windows:</summary>

   - Go to "Control Panel" > "System and Security" > "System"
   - Click "Advanced system settings"
   - Select the "Advanced" tab and click "Environment Variables"
   - Under "User variables", click "New"
   - Enter the variable name as "OPENAI_API_KEY" and the value as your key.
   - Click "OK" to save

   </details>
