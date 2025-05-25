from flask import Flask, render_template, request
from langchain_ollama.llms import OllamaLLM
from langchain_core.prompts import ChatPromptTemplate
from vector import retriever

app = Flask(__name__)

# Modèle LLM
model = OllamaLLM(model="llama3.2")

# Prompt template
template = """
You are an expert in answering questions about a pizza restaurant.

Here are some relevant reviews: {reviews}

Here is the question to answer: {question}
"""
prompt = ChatPromptTemplate.from_template(template)
chain = prompt | model

@app.route("/", methods=["GET", "POST"])
def index():
    answer = ""
    question = ""
    if request.method == "POST":
        question = request.form["question"]
        reviews = retriever.invoke(question)
        answer = chain.invoke({"reviews": reviews, "question": question})
    return render_template("index.html", answer=answer, question=question)

if __name__ == "__main__":
    app.run(debug=True)
