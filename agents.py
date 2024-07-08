import os
os.environ["CUDA_VISIBLE_DEVICES"] = "4" # GPU(s) that the model will load on to/forward pass
from transformers import AutoTokenizer, AutoModelForCausalLM
import torch


class GemmaAgent:
    """Gemma class to interact with Gemma2:27b-instruct model from HuggingFace"""
    def __init__(self) -> None:
        """Initializes Gemma2:27b-instruct tokenizer & model from HuggingFace"""
        self.tokenizer = AutoTokenizer.from_pretrained("google/gemma-2b-it", model_max_length=8192)
        self.model = AutoModelForCausalLM.from_pretrained(
            "google/gemma-2-27b-it",
            device_map="auto",
            torch_dtype=torch.bfloat16,
            attn_implementation='eager'
        )
    
    def send_query(self, prompt:str):
        """Sends prompt to model and returns model output"""
        input_text = prompt
        print(len(self.tokenizer.tokenize(prompt)))
        input_ids = self.tokenizer(input_text, return_tensors="pt").to("cuda")
        outputs = self.model.generate(**input_ids, max_new_tokens=10000)
        return self.tokenizer.decode(outputs[0])