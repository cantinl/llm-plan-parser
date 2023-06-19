import openai

# Set up your OpenAI API credentials
openai.api_key = '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'

def generate_response(prompt):
    # Call the OpenAI API to generate a response
    response = openai.Completion.create(
        engine='text-davinci-003',  # Use the gpt-3.5-turbo engine for chat-based prompts
        prompt=prompt,
        max_tokens=1000,  # Adjust the max tokens based on your requirements
        temperature=0.7,  # Adjust the temperature for more or less randomness
        n = 1, # Number of responses to generate
        stop=None,  # You can add a stop string to indicate the end of the response
        timeout=None  # You can set a timeout (in seconds) for the API call
    )

    # Extract and return the generated response
    return response.choices[0].text.strip()

