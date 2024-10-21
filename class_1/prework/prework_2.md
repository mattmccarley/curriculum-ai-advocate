# Creating an AI Application in Pyton

We will setup a Python project and run our first Open AI call.

1. Create a new folder and open it in cursor.
2. We'll first setup a virtual environment so any packages we install are only used in this project. Open the terminal by either selecting the terminal icon in the top right of the Cursor window or hitting cmd/cntl+J. 
    In the terminal, we'll create a virtual environment folder by typing
    ```bash
    uv venv venv
    ```
    Our dependencies will live in this folder. We need to activate the virtual environment before we install anything.

    Mac:
    ```bash
    source venv/bin/activate
    ```

    Windows:
    ```bash
    venv/bin/activate
    ```

    With our virtual environment activated, we can now install the OpenAI library:
    ```bash
    uv pip install openai
    ```

3. Create a new file called `main.py`. In that file, paste the following:

    ```python
    from openai import OpenAI
    import os

    client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

    # Set up your OpenAI API key

    def analyze_sentiment(review):
        response = client.chat.completions.create(model="gpt-4o-mini",
        messages=[
            {"role": "user", "content": f"You are a sentiment analysis expert. Analyze the sentiment of the following movie review and respond with either 'Positive', 'Negative', or 'Neutral'. {review}"}
        ])
        return response.choices[0].message.content.strip()

    # Example movie review
    movie_review = """
    The latest superhero blockbuster was a rollercoaster of emotions. 
    The special effects were mind-blowing and the action sequences kept me on the edge of my seat. 
    However, the plot felt a bit predictable at times, and some character development was lacking. 
    Overall, it was an entertaining experience, but not as groundbreaking as I had hoped.
    """

    # Analyze the sentiment
    sentiment = analyze_sentiment(movie_review)

    print(f"Movie Review:\n{movie_review}\n")
    print(f"Sentiment: {sentiment}")
    ```

4. Now run the file by running this command in the terminal:

    ```
    python main.py
    ```

5. Instead of explaining what this code does here, it would be better if you use Cursor do it.

    Open the AI panel by either hitting ctrl/cmd+L or clicking the AI panel icon in the top right (next to the terminal icon).

    In the chat window, you can ask anything about the open file. Ask Cursor to explain any part of the code that you do not understand until you have a good grasp for how the code works. You could even prompt Cursor to change the code.

    We'll go over more about writing AI applications and using Cursor in class. You are now done with today's prework.