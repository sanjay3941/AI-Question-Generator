def main():
    import os
    from pdf_to_text import PdfToText
    from q_gen import Q_gen
    filename = input("Enter the file name: ")
    while not filename.lower().endswith(".pdf"):
        print("Invalid file type")
        filename = input("Enter the file name: ")
    if not os.path.isfile(filename) :
                print("File does not exist!!!")
                return None
    pdftotxt = PdfToText(filename)
    q_type = input("Enter the type of Question You want (Easy,Medium,Hard): ")
    level = ["easy","medium","hard"]
    while q_type.lower() not in level:
           print("Invalid Level Type")
           q_type = input("Enter the type of Question You want (Easy,Medium,Hard): ")
    txt = pdftotxt.extract_text()
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
    response = q_gen.question_gen(txt,no_of_q,lvl=level)
    with open("response.txt","w",encoding="utf-8") as res:
           res.write(response)
main()
