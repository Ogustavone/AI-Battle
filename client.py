from google import genai

AI = genai.Client(
    api_key="YOUR_API_KEY"
)

def request_completion(prompt):
    """
    Generates a response for a prompt using the Gemini AI model.
    Args:
        prompt (str): The input prompt to be sent to the AI model for content generation.
    Returns:
        response.text: The generated content returned by the AI model.
    """
    response = AI.models.generate_content(
        model="gemini-2.0-flash-lite",
        contents=str(prompt)
    )
    return response.text