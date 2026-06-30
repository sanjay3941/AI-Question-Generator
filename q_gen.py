import ollama
class Q_gen:
    def __init__(self):
        ...
    def question_gen(self,context,no_of_q,question_type,lvl = 0,):
        response  = ollama.chat(model="qwen2.5:3b",messages=[{"role": "user","content": f"""Generate exactly {no_of_q} questionsfrom the following notes:{context}
            note:No of questions must between 1 to {no_of_q}.
            Rules: 
            - Make sure the question is at {lvl} level.
            - Also mention the page number from which the question was taken
            - The Question type is {question_type}
            - Make sure there are {no_of_q} questions 
            - if the question type is mcq type ,it must have 4 options and one correct options
            - make sure to add the answer at the end not immediately after the questions
            - Also mention the respective question number near the answer."""}])
        return response["message"]["content"]
        