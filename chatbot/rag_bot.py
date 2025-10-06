#!/usr/bin/env python3

from memory import memory
from chain import generate_response_from_llm, docsearch

def ask_question(question: str) -> str:
    if not question:
        return "Por favor, proporciona una pregunta."

    docs = docsearch.similarity_search(question)
    if not docs:
        return "No se encontraron documentos relevantes."

    context = memory.load_memory_variables({})["chat_history"]
    response = generate_response_from_llm(question, context, docs)
    memory.save_context({"human_input": question}, {"AI_response": response})
    return response

if __name__ == "__main__":
    while True:
        q = input("Pregunta: ")
        if q.lower() in ["salir", "exit"]:
            break
        print("Mia:", ask_question(q))
