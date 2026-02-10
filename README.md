# Sun Devil GPT

**Sun Devil GPT** is a demo library-focused chatbot developed for the **Intro to AI Engineering Open Lab** at Data Science and Analytics Unit, Hayden Library at Arizona State University.  The chatbot is designed to answer questions about library services, resources, and policies using a retrieval-augmented generation (RAG) approach that grounds AI responses in authoritative content.

---

## Overview

Sun Devil GPT demonstrates how large language models can be combined with institutional knowledge to create practical, domain-specific AI assistants. The project serves as a teaching and learning tool for exploring modern AI engineering concepts, including prompt design, RAG pipelines, and deployment in lightweight web environments.

---

## Architecture

In a full production deployment, Sun Devil GPT includes the following components:

- **User Interface:** Streamlit  
- **Chatbot Orchestration:** LlamaIndex  
- **Vector Database:** ChromaDB  
- **Web Scraping:** Scrapy  
- **Usage Analytics:** MySQL  
- **Large Language Model:** OpenAI ChatGPT API

---

## Limitations of This Distribution

This repository contains a simplified, shareable version of Sun Devil GPT intended for demonstration and instructional use.
To enable fast deployment on Streamlit Community Cloud and similar environments, this distribution includes only:

- The Streamlit user interface  
- Chatbot control logic  
- Connection to the OpenAI API  

The following production components are not included in this repository:

- Vector database generation and ingestion workflows  
- Web scraping pipelines  
- Usage analytics and logging infrastructure  

These components are managed outside the Streamlit environment in the full system.

---

## Quick Start

To deploy your own copy of Sun Devil GPT, you will need:

- A GitHub account  
- A Streamlit Community Cloud account  
- An OpenAI API key  

### Deployment Steps

1. Fork this repository on GitHub  
2. Deploy the app on Streamlit Community Cloud  
   - Set the **main file path** to:
     ```
     llamainchatbot.py
     ```
3. Before running the app, add your OpenAI API key to Streamlit **Secrets**
   - The app expects the key under:
     ```
     openai.key
     ```
   - Manage secrets through Streamlit’s web interface  
   - **Do not** commit a `secrets.toml` file to your repository  

Once deployed, you can customize the chatbot’s prompt, behavior, and interface by editing `llamainchatbot.py`.

---

## Educational Use

This project was developed as a **demonstration for the Intro to AI Engineering Open Lab**.  
It is intended for instructional, exploratory, and prototyping purposes rather than full production deployment.

Students and instructors are encouraged to extend the project by:

- Adding their own document sources  
- Implementing a local vector database  
- Experimenting with prompt engineering and retrieval strategies  

---

## Acknowledgments

Sun Devil GPT is adapted from **KingbotGPT**, developed by the San José State University Library.

More information on the original project can be found in:

*Library-Led AI: Building a Library Chatbot as Service and Strategy*  
ACRL 2025 Conference Proceedings

