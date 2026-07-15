import streamlit as st
import ollama
def check_ollama():
     try:
          ollama.list()
          return True
     except:
          st.error("Ollama is not Running")
          st.info("Start Ollama and try again")
          st.stop()
          return False
st.set_page_config(page_title="AI Question Generator",page_icon="🤖")
if "current_file" not in st.session_state: #preventing the same file to be scanned again and again,because by default streamlit does
      st.session_state.current_file = None
if "txt" not in st.session_state:
      st.session_state.txt = None
from pathlib import Path
from file_to_text import DocxToText,PdfToText,PptxToText,TxttoText
from q_gen import Q_gen
st.title("AI Question Generator")
filename = st.file_uploader("Select the document",type=["pdf","docx","pptx","txt"])
if filename:
    file_id = (filename.name,filename.size)
    if st.session_state.current_file!=file_id:
          st.write("Processing Document")
          upload_dir = Path("uploads")
          upload_dir.mkdir(exist_ok=True)
          file_path = upload_dir/filename.name
          st.write(filename.name)
          st.write(file_path)
          with open(file_path,"wb") as f:
              f.write(filename.getbuffer())
          file_format_verified = False
          
          if file_path.suffix==".pdf":
                pdftotxt = PdfToText(str(file_path))
                progress_bar = st.progress(0)
                status = st.empty()
                def update_progress(current,total):
                    progress_bar.progress(current/total)
                    status.text(f"Processing page {current}/{total}")
                txt = pdftotxt.extract_text(progress_callback=update_progress)
                file_format_verified = True
                progress_bar.empty()
                status.success("Document processed Sucessfully")
          elif file_path.suffix==".docx":
                docxtotext = DocxToText(filename)
                txt = docxtotext.extract_text()
                file_format_verified = True
                st.success("Document processed successfully!")
          elif file_path.suffix==".pptx":  
                pptxtotext = PptxToText(str(file_path))
                progress_bar = st.progress(0)
                status = st.empty()
                def update_progress(current,total):
                    progress_bar.progress(current/total)
                    status.text(f"Processing slide {current}/{total}")

                txt = pptxtotext.extract_text(progress_callback=update_progress)
                file_format_verified = True
                progress_bar.empty()
                status.success("Document Processed Sucessfully")
          elif file_path.suffix.lower()==".txt":
                txtToText = TxttoText(str(file_path))
                txt = txtToText.extract_text()
                file_format_verified = True
                st.success("Document processed successfully!")
          with open("tmp.txt","w",encoding="utf-8") as f:
                for i,j in txt.items():
                        f.write(f"\n\n\nPage Number : {i}\n\n\n")
                        f.write(j)
          st.session_state.txt = txt
          st.session_state.current_file = file_id
    txt = st.session_state.txt
    oper = st.selectbox("What do you want to do ?",
                        ["MCQ Question","Short Answer Question",
                         "Long Answer Question","Summary of the PDF"])
    if oper!="Summary of the PDF":
        q_type = st.selectbox("Select the Difficulty",
                              ["Easy","Medium","Hard"])
    else:
        q_type = None
    no_of_q = st.number_input("Number of Questions",
                                  min_value=1,max_value=100,value=10,step=1)
    
    if check_ollama():
         st.success("🟢 Ollama is Connected")
    else:
         st.error("🔴 Ollama Status: Not Running")
    if st.button("Generate",disabled=not check_ollama()):
             
        q_gen = Q_gen()
        with st.spinner("Questions are getting Generated"):
            response = q_gen.question_gen(txt,no_of_q,lvl=q_type,question_type=oper)
        st.session_state.questions = response
        st.switch_page("pages/View_question.py")