import os
from gemini import Gemini

os.environ["GEMINI_LANGUAGE"] = "TW"  
os.environ["GEMINI_ULTRA"] = "0"      # Switch to Gemini-advanced response (Experimental, Optional)

directory_path = ""

cookies = {}
client = Gemini(cookies=cookies) # You can use various args

# prompt = "This image shows a report card for a high school student in Taiwan. Please extract the following information in Traditional Chinese and output it as JSON: student name, scores for each subject, and average score."
prompt = "請判斷此圖是臺灣某學校的學期成績單還是臺灣的戶口名簿，如果是臺灣某學校的學期成績單請用.json 回傳(isTaiwaneseSchoolReportCard:1)，否則回傳0。"
# prompt = "此圖為臺灣高中的學期成績單，請用繁體中文截取以下內容，並輸出成JSON： 學生姓名，各科成績，平均分數"

image_path = "./img/t_r1.webp"
# image_path = "./img/h_half1.webp"
image = directory_path + image_path



response = client.generate_content(prompt, image)
print(type(response))

for key, value in response.response_dict.items():
    if(key == "candidates"):

        for i in range(len(value)):
            if(i == 0):
                print(f"Candidate {i}: ")

                for c_key, c_value in value[i].items():
                    if(1 or c_key == "text" or c_key == "code"):
                        print(f"\t{c_key}: {c_value}")

    else:
        print(key, ":", value)

