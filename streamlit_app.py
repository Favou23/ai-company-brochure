import streamlit as st
from main import create_brochure

st.set_page_config(
    page_title="AI Company Brochure Generator",
    page_icon="🌐",
    layout="centered"
)

st.title("BrochureAI")

st.markdown(
    """
Generate a professional company brochure from any company's website using AI.

This application:

- 🌐 Scrapes the company's website
- 🔍 Finds the most relevant pages
- 🧠 Uses AI to build rich context
- 📄 Generates a professional brochure
"""
)

st.divider()

# company_name = st.text_input(
#     "Company Name",
#     placeholder="e.g. Hugging Face"
# )

# website = st.text_input(
#     "Website URL",
#     placeholder="https://huggingface.co"
# )

company_name = st.text_input(
    "Company Name",
    value="Hugging Face",
    help="Enter the company's name."
)

website = st.text_input(
    "Website URL",
    value="https://huggingface.co",
    help="Enter the company's homepage URL."
)

generate = st.button(
    "🚀 Generate Brochure",
    use_container_width=True
)

if generate:

    if not company_name.strip():
        st.warning("Please enter a company name.")
        st.stop()

    if not website.strip():
        st.warning("Please enter a website URL.")
        st.stop()

    try:

        with st.spinner("Analyzing website..."):

            brochure = create_brochure(
                company_name,
                website
            )

        st.success("Brochure generated successfully!")

        st.divider()
        
        with st.expander("View Generated Brochure", expanded=True):
            st.markdown(brochure)

        # st.markdown(brochure)

        st.download_button(
            label="📥 Download Markdown",
            data=brochure,
            file_name=f"{company_name.lower().replace(' ', '_')}_brochure.md",
            mime="text/markdown"
        )

    except Exception as e:

        st.error(str(e))


with st.sidebar:

    st.header("About")

    st.write(
        """
This project demonstrates practical AI Engineering concepts:

- Prompt Engineering
- Context Engineering
- Website Scraping
- Multi-step LLM Pipelines
- Structured JSON Outputs
- Google Gemini API
        """
    )

    st.divider()

    st.caption(
        "Built by Shaib Godsfavour"
    )