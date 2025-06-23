import streamlit as st
from transformers import pipeline
import PyPDF2
from fpdf import FPDF
import base64

# Load the summarization model once
@st.cache_resource
def load_model():
    return pipeline("summarization", model="facebook/bart-large-cnn")

summarizer = load_model()

# Extract text from PDF
def extract_text_from_pdf(uploaded_file):
    pdf_reader = PyPDF2.PdfReader(uploaded_file)
    text = ""
    for page in pdf_reader.pages:
        text += page.extract_text() or ""
    return text

# Export summary to PDF and make it downloadable
def export_summary_to_pdf(summary_text):
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=12)
    for line in summary_text.split('\n'):
        pdf.multi_cell(0, 10, line)

    filename = "summary_output.pdf"
    pdf.output(filename)

    with open(filename, "rb") as f:
        base64_pdf = base64.b64encode(f.read()).decode("utf-8")

    download_link = f'<a href="data:application/pdf;base64,{base64_pdf}" download="{filename}">📄 Click here to download your summary PDF</a>'
    st.markdown(download_link, unsafe_allow_html=True)

# Streamlit UI
st.set_page_config(page_title="AI Notes Summarizer", layout="centered")
st.title("📚 AI Notes Summarizer")
st.write("Summarize your long notes or PDFs instantly using AI (BART Transformer model)")

# Input options
option = st.radio("Choose Input Type:", ["Paste Text", "Upload PDF"])

input_text = ""

if option == "Paste Text":
    input_text = st.text_area("Paste your notes here 👇", height=300)
else:
    uploaded_pdf = st.file_uploader("Upload a PDF file with notes", type=["pdf"])
    if uploaded_pdf:
        input_text = extract_text_from_pdf(uploaded_pdf)
        st.success("✅ Text extracted from PDF successfully!")

# Summarization and export
if st.button("🧠 Summarize Notes"):
    if input_text.strip() == "":
        st.warning("Please provide some input text first.")
    else:
        with st.spinner("Summarizing... please wait"):
            # Limit input size to 1024 tokens
            input_text = input_text[:1024]
            summary = summarizer(input_text, max_length=150, min_length=40, do_sample=False)
            summary_text = summary[0]['summary_text']

            st.subheader("📝 Summary:")
            st.success(summary_text)

            # Offer PDF export
            st.markdown("### 📤 Export as PDF:")
            export_summary_to_pdf(summary_text)
