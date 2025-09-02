from transformers import pipeline

# Load the model once
email_writer = pipeline("text2text-generation", model="google/flan-t5-large")  # better model

def generate_email(task: str, tone: str, content: str, max_length: int = 300) -> str:
    """
    Generate a well-structured email using FLAN-T5.
    """
    prompt = f"""
    You are an AI assistant that writes professional emails.
    Task: {task} an email.
    Tone: {tone}.
    Content: {content}.
    
    Write a complete email with:
    - Greeting (like Dear Sir/Madam)
    - Body
    - Closing (like Regards, Thank you)
    """
    
    result = email_writer(prompt, max_length=max_length, do_sample=True, temperature=0.7)
    return result[0]['generated_text']
