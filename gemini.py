import google.generativeai as genai
import pandas as  pd

model = genai.GenerativeModel('gemini-pro')
GOOGLE_API_KEY='AIzaSyCDW52posgyQZVxtjkVz9SoGkRDmD9P_oo'
genai.configure(api_key=GOOGLE_API_KEY)


def gemini(prompt1,prompt2,prompt3,prompt4):
    format = [
            {
                "action": "Add a description action in string format that the user needs to take",
                "amount": "Add a numerical value according to you in int form"
            },
            {
                "action": "Add a description action in string format that the user needs to take",
                "amount": "Add value according to you"
            },
            {
                "action": "Add a description action in string format that the user needs to take",
                "amount": "Add value according to you"
            },
            {
                "action": "Add a description action in string format that the user needs to take",
                "amount": "Add value according to you"
            },
            {
                "action": "Add a description action in string format that the user needs to take",
                "amount": "Add value according to you"
            },
            {
                "action": "Add a description action in string format that the user needs to take",
                "amount": "Add value according to you"
            }
    ]
    while True:
        try:
            full_prompt = f"i have a salary of : {prompt1} ruppes per month, my needs are that : {prompt2}, some things to note are : {prompt3} and finally my goal is :  {prompt4}, generate a comprehensive, yet concise,monthly budget plan on how i should spend my money this month to achieve my goals, please reply in following format ONLY :- {format}"
            response =  model.generate_content(full_prompt)
            solution = (response.text)
            if solution[0]=="`":
                solution = solution.replace("`","")
            solution = eval(solution)
            break
        except:
            continue
    return solution

def Taxation(age,location,family,investment,debt,salary,needs,goal,message):
    while True:
        try:
            tax_format = [
                '(Dont add anything here such as 1,2,3,4..)Your answers Here as a list members To add anything else except proper english words and give me around 8 list members',
            ]
            taxation_prompt = f"""I live in {location} iam {age} years old
            have {family} family members
            {investment} rupees in investments in stocks
            mortgage on house worth {debt} monthly
            based on ths information plus the fact that 
            my salary is {salary} per month, i need {needs} every month, my goal {goal}, and note of the fact {message}, please tell me how i can try to save on my taxes
            dont include any written paragraph reply everthing as a string inside a python list dont include anything else except words inside the string Heres a format to help you please reply in the following prompt only : {tax_format} """
            taxation_response =  model.generate_content(taxation_prompt)
            Taxsolution = (taxation_response.text)
            Taxsolution = eval(Taxsolution)
            break
        except:
            continue
    return Taxsolution

def csv(data , name):
    frame =  pd.DataFrame(data)
    frame.index = [i for i in range(1,len(data["Tax Redemption methods"]) + 1)]
    frame.to_csv(f"./static/{name}.csv")

if __name__ == "__main__":
    print(type(Taxation()))