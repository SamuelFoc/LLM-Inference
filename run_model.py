from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from transformers import AutoModelForCausalLM, AutoTokenizer
import torch

# Initialize FastAPI app
app = FastAPI()

# Load model and tokenizer
MODEL_NAME = "microsoft/Phi-3-mini-128k-instruct"  # Replace with your preferred model
device = "cuda" if torch.cuda.is_available() else "cpu"

print(f"Loading model to {device}...")
model = AutoModelForCausalLM.from_pretrained(MODEL_NAME).to(device)
tokenizer = AutoTokenizer.from_pretrained(MODEL_NAME)
print("Model loaded successfully.")

# Define request body schema
class Prompt(BaseModel):
    text: str
    max_length: int = 50  # Optional: Limit the maximum response length

@app.post("/generate/")
async def generate_text(prompt: Prompt):
    """
    Generate text from the model based on the user's input.
    """
    try:
        # Tokenize the input prompt
        inputs = tokenizer.encode(prompt.text, return_tensors="pt").to(device)
        
        # Generate the response
        outputs = model.generate(
            inputs,
            max_length=prompt.max_length,
            pad_token_id=tokenizer.eos_token_id
        )
        
        # Decode the generated responses
        responses = [tokenizer.decode(output, skip_special_tokens=True) for output in outputs]
        return {"responses": responses}
    
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error generating text: {str(e)}")
