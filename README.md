# 🧠 AI Company Brochure Generator

Generate professional company brochures using Large Language Models (LLMs) by intelligently analyzing a company's website.

Instead of sending only a homepage to an LLM, this application first identifies the most relevant pages (such as About, Products, Careers, and Company pages), gathers their content, and then generates a comprehensive brochure suitable for prospective customers, investors, and job seekers.

---

## 📖 Overview

Large Language Models perform significantly better when given relevant context.

Rather than asking an LLM to summarize only a company's homepage, this project follows a multi-step pipeline:

1. Scrape the company's homepage.
2. Extract all available internal links.
3. Use an LLM to determine which links are most relevant.
4. Scrape the content from those relevant pages.
5. Combine all collected information into a structured prompt.
6. Generate a professional brochure in Markdown.

This approach provides richer context, resulting in higher-quality summaries.

---

## 🚀 Features

- Website scraping
- Automatic extraction of internal links
- AI-powered link selection
- Multi-page content aggregation
- Professional brochure generation
- Markdown output
- Streaming response support (optional)

---

## 🏗️ System Architecture

```text
                Company URL
                     │
                     ▼
        Scrape Homepage & Extract Links
                     │
                     ▼
      LLM Selects Relevant Website Pages
                     │
                     ▼
     Scrape Content From Selected Pages
                     │
                     ▼
        Build Structured Prompt Context
                     │
                     ▼
             GPT Generates Brochure
                     │
                     ▼
          Professional Markdown Output
```

---

## 🧠 Engineering Workflow

### Step 1 — Extract Website Links

The application scrapes the homepage and extracts all internal links.

Example:

- About
- Careers
- Products
- Blog
- Contact
- Privacy Policy
- Terms of Service

---

### Step 2 — AI Link Selection

Not every page is useful for building a brochure.

An LLM analyzes the extracted links and identifies the pages most likely to contain useful business information.

Typical selections include:

- About
- Company
- Products
- Careers
- Customers
- Solutions

This demonstrates using an LLM for **reasoning**, rather than simple text generation.

---

### Step 3 — Content Collection

The scraper visits each selected page and retrieves its content.

The collected information is merged into a single context document.

---

### Step 4 — Brochure Generation

A second LLM call receives:

- Company name
- Homepage content
- Relevant page content

The model generates a professional brochure in Markdown format.

---

## 📂 Project Structure

```text
.
├── app.py
├── scraper.py
├── README.md
├── requirements.txt
└── .env
```

---

## 🛠️ Technologies Used

- Python
- OpenAI API
- BeautifulSoup
- Requests
- Markdown
- JSON
- dotenv

---

## 📌 AI Concepts Demonstrated

This project demonstrates several practical AI engineering concepts:

- Prompt Engineering
- Context Engineering
- Multi-step LLM Pipelines
- Structured JSON Output
- Website Scraping
- Data Preprocessing
- LLM-based Decision Making
- Markdown Generation

---

## 📈 Data Flow

```text
Website URL
      │
      ▼
Extract Website Links
      │
      ▼
Relevant Links (LLM)
      │
      ▼
Scrape Page Contents
      │
      ▼
Merge Context
      │
      ▼
Generate Brochure (LLM)
      │
      ▼
Markdown Output
```

---

## 💻 Installation

Clone the repository:

```bash
git clone https://github.com/yourusername/your-repository.git
```

Navigate into the project:

```bash
cd your-repository
```

Install dependencies:

```bash
pip install -r requirements.txt
```

---

## 🔑 Environment Variables

Create a `.env` file:

```env
OPENAI_API_KEY=your_api_key_here
```

---

## ▶️ Usage

Run the application:

```bash
python app.py
```

Example:

```python
create_brochure(
    company_name="HuggingFace",
    url="https://huggingface.co"
)
```

---

## Example Output

```markdown
# HuggingFace

## About

Hugging Face is an AI company focused on democratizing machine learning...

## Products

- Transformers
- Datasets
- Spaces
- Inference Endpoints

## Careers

The company promotes open collaboration and remote work...

## Customers

Used by researchers, startups, and Fortune 500 companies.
```

---

## 🎯 Why This Project Matters

Many AI applications perform poorly because they provide an LLM with insufficient context.

This project demonstrates an important AI Engineering principle:

> **Use traditional programming to gather high-quality information, then use an LLM for reasoning and generation.**

Rather than relying on the model to "figure everything out," the application first performs deterministic tasks (scraping, link extraction, data collection) before asking the LLM to perform tasks that require understanding.

---

## 📚 Key Learnings

While building this project, I learned:

- How to integrate website scraping into an AI workflow.
- When to use traditional Python versus an LLM.
- How to engineer prompts using richer context.
- How to use structured JSON responses from an LLM.
- How multi-step AI pipelines improve output quality.

---

## 🚧 Possible Improvements

Future enhancements include:

- Streamlit web interface
- FastAPI backend
- Async website scraping
- Caching scraped pages
- PDF brochure export
- Company logo extraction
- Brand color detection
- Multi-language brochure generation
- Support for local LLMs via Ollama
- RAG-based company knowledge retrieval

---

## 📸 Demo

> *Add screenshots or a GIF of the application here after deployment.*

---

## 🤝 Contributing

Contributions, issues, and feature requests are welcome.

If you have suggestions or improvements, feel free to open an issue or submit a pull request.

---

## 📄 License

This project is licensed under the MIT License.

---

## 👨‍💻 Author

**Shaib Godsfavour**

Backend Developer | AI Engineering Learner | Building Practical AI Systems

- GitHub: https://github.com/favou23
- LinkedIn: https://linkedin.com/in/yourprofile

---

## ⭐ If you found this project interesting...

Consider giving it a ⭐ on GitHub!