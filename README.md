# 🍕 Pizza Review RAG Chatbot

Un assistant intelligent capable de répondre à toutes les questions concernant une pizzeria, en s'appuyant sur des avis clients pertinents issus d’un fichier CSV.  
Ce projet utilise le concept de **Retrieval-Augmented Generation (RAG)** avec **LangChain**, **Ollama** (modèle LLaMA 3), **ChromaDB** pour l’indexation vectorielle, et **Flask** pour l’interface web.

---

## 🚀 Fonctionnalités

- 🔍 Recherche intelligente dans des avis de clients (RAG)
- 🤖 Génération de réponses contextuelles avec un modèle LLM local (`llama3.2`)
- 🧠 Vectorisation des documents avec `nomic-embed-text` via Ollama
- 💬 Interface web conversationnelle avec historique de chat
- ♻️ Bouton "Nouveau chat" pour réinitialiser la session

---

## 📁 Arborescence du projet

```
├── app.py                         # Application Flask principale
├── vector.py                      # Construction de la base vectorielle avec LangChain & Chroma
├── realistic_restaurant_reviews.csv  # Base d'avis clients
├── templates/
│   └── index.html                 # Interface utilisateur HTML
├── chrome_langchain_db/          # Dossier généré contenant la base Chroma persistée
└── README.md
```

---

## 🧩 Technologies utilisées

| Composant       | Description                                         |
|-----------------|-----------------------------------------------------|
| 🧠 LangChain     | Orchestration du RAG et du prompt                  |
| 🧊 ChromaDB       | Vector store local pour les documents              |
| 📄 Ollama         | Exécution locale du LLM (LLaMA 3.2 et embeddings) |
| 🌐 Flask          | Interface web minimale mais efficace               |
| 📊 Pandas         | Chargement et traitement du CSV                   |

---

## ⚙️ Installation

1. **Pré-requis** :
   - Python 3.9+
   - [Ollama](https://ollama.com) installé et lancé (`ollama run llama3`)
   - Modules Python suivants :

```bash
pip install flask langchain langchain-community langchain-core langchain-chroma langchain-ollama pandas
```

2. **Lancer le serveur** :

```bash
python app.py
```

3. Accéder à l'interface via :  
👉 `http://127.0.0.1:5000/`

---

## 🧪 Exemple d'utilisation

Posez des questions comme :

- _“Que pensent les clients de la pâte à pizza ?”_  
- _“Les livraisons sont-elles ponctuelles ?”_  
- _“Quelles sont les critiques les plus fréquentes ?”_

Le chatbot utilise les 5 avis les plus pertinents pour générer sa réponse.

---

## 🔄 Réinitialisation

Cliquez sur **“Nouveau Chat”** pour effacer l'historique et démarrer une nouvelle conversation.

---

## 📌 Personnalisation

- **Modèle utilisé** : dans `app.py`, vous pouvez changer `llama3.2` par tout autre modèle compatible Ollama.
- **Nombre de documents récupérés** : changez `k=5` dans `retriever = vector_store.as_retriever(...)`.
- **Prompt système** : modifiez la variable `template` pour ajuster l’"identité" du chatbot.

---

## 📎 Données

Les avis sont stockés dans un fichier CSV nommé `realistic_restaurant_reviews.csv` avec les colonnes :

- `Title` – titre de l’avis
- `Review` – texte complet
- `Rating` – note de l’auteur
- `Date` – date de l’avis

---

## 📜 Licence

Projet personnel réalisé à des fins éducatives.  
N'hésitez pas à le forker et à l’adapter à d’autres contextes métiers.

---
