# Langchain_document_loaders

📦 What are Document Loaders?
Document Loaders:

Load raw data from various sources (files, web, APIs)

Convert them into LangChain Document format

Are often used with text splitting, embedding, and vector stores

| Loader               | Use Case                             |
| -------------------- | ------------------------------------ |
| `TextLoader`         | Load plain text files                |
| `PyPDFLoader`        | Extract text from PDFs               |
| `WebBaseLoader`      | Scrape and load from a web URL       |
| `DirectoryLoader`    | Load multiple files from a folder    |
| `UnstructuredLoader` | Parse complex formats (tables, etc.) |

| Feature          | Description                        |
| ---------------- | ---------------------------------- |
| Easy integration | Plug into pipelines easily         |
| Multiple formats | Text, PDF, HTML, CSV, Notion, etc. |
| Metadata support | Source-tracking built-in           |
| Extensible       | Create custom loaders if needed    |
