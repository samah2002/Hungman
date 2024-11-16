import random
# art hang man
hangman_art = ['''
  +---+
  |   |
      |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========''']

# أعطاء تلميح وجعل الكومبيوتر يختار عشوائيا
country = random.choice(["syria", "egypt", "lebanon", "italy", "germany", "japan", "china"])
fruit = random.choice(["apple", "banana", "mango", "pear", "cherry", "watermelon"])
arabic_name = random.choice(["ahmed", "samer", "yamen", "ammar", "fatima", "reem", "wafaa","laila"])
random_choice = random.choice([country , fruit , arabic_name])
if random_choice == country:
    print ("I'll give you a hint, the word is : country")
elif random_choice == fruit:
    print ("I'll give you a hint, the word is : fruit")
else:
    print ("I'll give you a hint, the word is : arabic_name")

# تشفيير
encryption = list("_" * len(random_choice))
print (f"You have 6 attempts \n{hangman_art[0]}")

#نطلب  تخمين مع تحديد عدد المحاولات 
test = 0
fulse_guess = []
while "_" in encryption and test < 6 :
    print ("    ".join(encryption))
    user_guees = input ("Please, gusse a letter:  ").lower()
    
    # الحصر  ب 6 محاولات خاطئة وعدم تكرار الخطأ لحرف مذكور سابقا
    if user_guees not in random_choice:
        if user_guees in fulse_guess:
            print ("You already guessed that. Try again.")
            continue
        test += 1
        fulse_guess.append(user_guees)
    # استبدال الحرف الصحيح ب مسافة 
    for letter in range (len(random_choice)):

        if random_choice[letter] == user_guees:
            encryption[letter] = user_guees
    # رسم تدريجي للرجل المشنوق + ذكر عدد المحاولات الخاطئة
    print (hangman_art[test])


# تحديد فوز أو خسارة
if "_" not in encryption:
    print ("""      
_____.___.               __      __.__        
\__  |   | ____  __ __  /  \    /  \__| ____
/   |   |/  _ \|  |  \ \   \/\/   /  |/     \ 
\____   (  <_> )  |  /  \        /|  |   |   \ 
/ ______|\____/|____/    \__/\  / |__|___|  /
\/                           \/          \/                           
""")

else:
    print(f"""
          
_____.___.             .__                 __   
\__  |   | ____  __ __ |  |   ____  ______/  |_ 
/   |   |/  _ \|  |  \ |  |  /  _ \/  ___\   __/
\____   (  <_> |  |  / |  |_(  <_> \___ \ |  |
/ ______|\____/|____/  |____/\____/____  >|__|
\/                                     \/          
 {hangman_art[-1]}                                           
""")
