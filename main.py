from fastapi import FastAPI
import re
from schema import InputBase

app = FastAPI()

user_id = "Balaji_M_30092004"
email = "balaji.m2022@vitstudent.ac.in"
roll_no = "22BCE3090"

def findAlternatingCaps(word):
    word = word[::-1]
    res = ""
    flag = True
    for i in word:
        if flag:
            res += i.upper()
        else:
            res += i.lower()
        flag = not flag
    return res

@app.post("/bfhl")
async def bfhl(input: InputBase):
    try:
        odd = []
        even = []
        alpha = []
        special = []
        total_sum = 0
        total_alpha = ""
        
        for i in input.data:
            if re.fullmatch(r"^-?\d+$", i):
                num = int(i)
                if num % 2 == 0:
                    even.append(i)
                else:
                    odd.append(i)
                total_sum += num
            elif i.isalpha():
                alpha.append(i.upper())
                total_alpha += i
            else:
                special.append(i)

        response = {
            "is_success": True,
            "user_id": f"{user_id}",
            "email": email,
            "roll_number": roll_no,
            "odd_numbers": odd,
            "even_numbers": even,
            "alphabets": alpha,
            "special_characters": special,
            "sum": str(total_sum),
            "concat_string": findAlternatingCaps(total_alpha),
        }

        return response

    except Exception as e:
        return {
            "is_success": False,
            "user_id": f"{user_id}",
            "email": email,
            "roll_number": roll_no,
            "error": str(e),
        }