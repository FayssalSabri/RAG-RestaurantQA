from flask import Flask, render_template, request, session, redirect, url_for
from vector import retriever
from langchain_ollama.llms import OllamaLLM
from langchain_core.prompts import ChatPromptTemplate

app = Flask(__name__)
app.secret_key = "super-secret-key"

# Initialisation du modèle et du prompt (à faire une seule fois)
model = OllamaLLM(model="llama3.2")

template = """
You are an expert in answering questions about a pizza restaurant

Here are some relevant reviews: {reviews}

Here is the question to answer: {question}
"""
prompt = ChatPromptTemplate.from_template(template)
chain = prompt | model

@app.route("/", methods=["GET", "POST"])
def index():
    if "chat_history" not in session:
        session["chat_history"] = []

    if request.method == "POST":
        question = request.form.get("question", "").strip()
        if question:
            # Récupération des reviews pertinentes via le retriever
            reviews_docs = retriever.invoke(question)
            reviews_text = "\n\n".join([doc.page_content for doc in reviews_docs]) if reviews_docs else "No relevant reviews found."

            # Génération de la réponse via le modèle
            result = chain.invoke({"reviews": reviews_text, "question": question})

            # Sauvegarde dans la session
            session["chat_history"].append({"question": question, "answer": result})
            session.modified = True

        return redirect(url_for("index"))

    return render_template("index.html", chat_history=session["chat_history"])

if __name__ == "__main__":
    app.run(debug=True)
