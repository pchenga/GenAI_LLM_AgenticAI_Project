from transformers import pipeline

pipe = pipeline(
    "text-generation",
    model="TinyLlama/TinyLlama-1.1B-Chat-v1.0"
)

prompt = """
<|user|>
explain hugging face transformers and  pipeline and how does it work?.
<|assistant|>
"""

response = pipe(
    prompt,
    max_new_tokens=120,
    temperature=0.7
)

print(response[0]["generated_text"])