# News Article Summarizer and Translator (NAST)

This Streamlit app allows users to summarize and translate news articles. The app is built using the Hugging Face `transformers` library for text summarization and the `deep-translator` library for translating non-English articles into English. It also automatically detects the language of the input article using the `langdetect` library.

## 🚀 Features

- **Summarization**: Uses Hugging Face’s `transformers` library to provide concise summaries of news articles.
- **Translation**: Automatically detects the language of the article and translates non-English articles to English using the `deep-translator` library.
- **Language Detection**: Automatically detects the input language using `langdetect`.
- **PyTorch Support**: Utilizes PyTorch backend for transformer models, ensuring compatibility with Keras 3 and the latest libraries.
- **Interactive UI**: Input fields and output sections are styled with borders and colors for easy navigation and user interaction.
