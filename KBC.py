#-------------------------------------------------------------------------------
# Name:        module3
# Purpose:
#
# Author:      ADARSH RANJAN
#
# Created:     01-04-2023
# Copyright:   (c) ADARSH RANJAN 2023
# Licence:     <your licence>
#-------------------------------------------------------------------------------

#WELCOME TO "KON BANEGA CROREPATI" SEASON = 11 ==>

questions = [
["Who was the first law minister of independent India?", "Bhimrao Ambedkar", "Mahatma Gandhi", "Adarsh", "J Lal Nehru", 1],

["Who was the first president of independent India?", "Bhimrao Ambedkar", "Mahatma Gandhi", "Rajendra Prasad", "J Lal Nehru", 3],

["Who was the first Prime Minister of independent India?", "Bhimrao Ambedkar", "Mahatma Gandhi", "Adarsh", "J Lal Nehru", 4],

["Who is the captain of Indian cricket team?", "Virat Kohli", "MS Dhoni", "KL Rahul", "Rohit Sharma", 4],

["Who is the owner of TCS?", "Ratan Tata", "Tata", "Mahindra", "Tata Steel", 1],

["What is the full form of HP?", "Hindustan Petroleum", "Hewlands Package", "Adarsh", "None", 2],

["Who was the first law minister of independent India?", "Bhimrao Ambedkar", "Mahatma Gandhi", "Adarsh", "J Lal Nehru", 1],

["Who was the first law minister of independent India?", "Bhimrao Ambedkar", "Mahatma Gandhi", "Adarsh", "J Lal Nehru", 1],

["Who was the first law minister of independent India?", "Bhimrao Ambedkar", "Mahatma Gandhi", "Adarsh", "J Lal Nehru", 1],

["Who was the first law minister of independent India?", "Bhimrao Ambedkar", "Mahatma Gandhi", "Adarsh", "J Lal Nehru", 1],

["Who was the first law minister of independent India?", "Bhimrao Ambedkar", "Mahatma Gandhi", "Adarsh", "J Lal Nehru", 1],

["Who was the first law minister of independent India?", "Bhimrao Ambedkar", "Mahatma Gandhi", "Adarsh", "J Lal Nehru", 1],

["Who was the first law minister of independent India?", "Bhimrao Ambedkar", "Mahatma Gandhi", "Adarsh", "J Lal Nehru", 1],

["Who was the first law minister of independent India?", "Bhimrao Ambedkar", "Mahatma Gandhi", "Adarsh", "J Lal Nehru", 1],

["Who was the first law minister of independent India?", "Bhimrao Ambedkar", "Mahatma Gandhi", "Adarsh", "J Lal Nehru", 1],

["Who was the first law minister of independent India?", "Bhimrao Ambedkar", "Mahatma Gandhi", "Adarsh", "J Lal Nehru", 1],

["Who was the first law minister of independent India?", "Bhimrao Ambedkar", "Mahatma Gandhi", "Adarsh", "J Lal Nehru", 1],
]

levels = [1000, 2000, 3000, 5000, 10000, 20000, 40000, 80000, 160000, 320000, 640000, 1250000, 2500000, 5000000, 10000000, 50000000, 70000000]

for i in range(0,len(questions)):
    question=questions[i]
    print(f"\n\nQuestions for Rs. {levels[i]}/-")
    print(questions[i][0])
    print(f"a. {question[1]}       b. {question[2]}")
    print(f"c. {question[3]}       d. {question[4]}")
    reply=int(input("Enter your Answer: "))
    if(reply == question[-1]):
        print(f"Correct answer! Wohoooo u have won Rs. {levels[i]}/-")
        if(i < 4):
            money = 0
        elif(i == 4):
            money = 10000
        elif(i == 9):
            money = 320000
        elif(i == 14):
            money = 10000000
        elif(i == 17):
            money = 70000000
        else:
            money = 0
    else:
        print("Wrong answer Don't Worry!!")
        break

print(f"Your take home money is {money}")