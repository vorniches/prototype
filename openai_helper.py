import logging
import json
from django.conf import settings
from openai import OpenAI

logger = logging.getLogger(__name__)

def send_prompt_to_openai(
    system_content: str,
    user_prompt: str,
    model: str = "gpt-4o-mini",
    max_tokens: int = 1000,
    temperature: float = 0.7,
):
    """
    Sends a prompt to the OpenAI Chat Completion endpoint using the same style
    of request your code already uses. Returns the content string or None on error.
    """
    try:
        # Create the OpenAI client with the existing approach
        client = OpenAI(api_key=settings.OPENAI_API_KEY)
        
        # Make the chat completion request
        chat_completion = client.chat.completions.create(
            model=model,
            messages=[
                {"role": "system", "content": system_content},
                {"role": "user", "content": user_prompt}
            ],
            max_tokens=max_tokens,
            temperature=temperature
        )
        
        if not chat_completion.choices:
            logger.error("No completion choices returned by OpenAI.")
            return None
        
        response_content = chat_completion.choices[0].message.content.strip()
        logger.debug(f"Raw response from OpenAI: {repr(response_content)}")
        
        return response_content
    
    except Exception as e:
        logger.error(f"Error calling OpenAI: {str(e)}")
        return None

def parse_json_response(response_content: str) -> dict:
    """
    Attempts to parse a string `response_content` as JSON.
    Returns a Python dict on success, or None on failure.
    """
    try:
        # In case the model includes ```json ... ```, remove those
        cleaned = response_content.replace("```json", "").replace("```", "").strip()
        data = json.loads(cleaned)
        return data
    except json.JSONDecodeError as e:
        logger.error(f"JSON parse error: {e}")
        return None
