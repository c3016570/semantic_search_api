from transformers import pipeline

generator = pipeline("text-generation",model = "gpt2")

def generate_answer(query, context):
    prompt = f"""
    Answer the question using ONLY the context.

    If the answer is not present in the context, say "I don't know".

    Context
    {context}

    Question
    {query}

    Answer in 2 sentences.
    """

    response = generator(
        prompt,
        max_new_tokens = 60,
        temperature = 0.7,
        repetition_penalty = 1.2,
        do_sample = True)
        
    generated_text = response[0]["generated_text"]

    answer = generated_text[len(prompt):]

    return answer.strip()

