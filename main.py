def main():
    from tkinter import Tk
    from tkinter.filedialog import askopenfilename
    from file_to_text import DocxToText,PdfToText,PptxToText,TxttoText
    from q_gen import Q_gen
    root = Tk()
    root.withdraw()
    filename = askopenfilename(title = "Select the File",filetypes=[
          ("Supported Files","*.pdf *.docx *.pptx *.txt"),
          ("PDF Files","*.pdf"),("Word Documents","*.docx"),("PowerPoint Presentation","*.pptx"),("Text Files","*.txt")])
    if not filename:
          print("No File Selected!!!")
          return
    file_format_verified = False
    root.destroy()
    if filename.endswith(".pdf"):
       pdftotxt = PdfToText(filename)
       txt = pdftotxt.extract_text()
       file_format_verified = True
    elif filename.endswith(".docx"):
          docxtotext = DocxToText(filename)
          txt = docxtotext.extract_text()
          file_format_verified = True
    elif filename.endswith(".pptx"):
          pptxtotext = PptxToText(filename)
          txt = pptxtotext.extract_text()
          file_format_verified = True
    elif filename.endswith(".txt"):
          txtToText = TxttoText(filename)
          txt = txtToText.extract_text()
          file_format_verified = True
    if file_format_verified:
       with open("tmp.txt","w",encoding="utf-8") as f:
              for i,j in txt.items():
                     f.write(f"\n\n\nPage Number : {i}\n\n\n")
                     f.write(j)
       no_of_q = int(input("Tell the total number of question required ? :"))
       q_gen = Q_gen()
       print("What do you want to do:\n1.MCQ Questions\n2.Short Answer Questions\n3.Long Answer Questions\n4.Summary of the PDf")
       ch = {1:"McQ Questions",2:"Short Answer Question",3:"Long Answer Question",4:"Summary of the Pdf"}
       choice = int(input("Enter the Operation: "))
       while choice not in [1,2,3,4]:
              print("Invalid Operation Entered: ")
              choice = int(input(("What do you want to do:\n1.MCQ Questions\n2.Short Answer Questions\n3.Long Answer Questions\n4.Summary of the PDf")))
       if choice!=4:
              q_type = input("Enter the type of Question You want (Easy,Medium,Hard): ")
              level = ["easy","medium","hard"]
              while q_type.lower() not in level:
                     print("Invalid Level Type")
                     q_type = input("Enter the type of Question You want (Easy,Medium,Hard): ")
       else:
              q_type = 0
       response = q_gen.question_gen(txt,no_of_q,lvl=q_type,question_type=ch[choice])
       with open("response.txt","w",encoding="utf-8") as res:
              res.write(response)
       print("Questions Stored in the response.txt")
    else:
          print("Unsupported File Type!!!")
          return
main()
