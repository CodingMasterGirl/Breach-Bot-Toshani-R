#Breach Bot Starter Code
breachYear = 2019

#Greets user
print("Hello! I'm Breach Bot.")
userName = input("What is your name?\n")
print("Nice to meet you " + userName)

#Recounts start of Breach
todaysYear = input("What year is it?\n")
timePassed = int(todaysYear) - breachYear
print("Wow! That means it has been " + str(timePassed) + " years since 2019 FaceBook Breach began!")

print("The field of Cybersecurity started in the 1970s when more and more information started being stored on computer systems and networks!")
input("Press enter to continue\n")

#Describes Cybersecurity
print("Cybersecurity refers to the practices that people use to protect computer systems and networks from digital threats.")
print("These people can be governement, nations, individuals, companies, community organizations, and hackers.\n")

#Introduces breach
print("Would you like to learn about the 2019 FaceBook Breach?")
giveInfo = input("Type 'yes' or 'no'\n")

#Explains breach
while giveInfo.lower() == "yes":
  print("What would you like to learn more about? Enter the lowercase letter of the following options: \n(a) breach details, (b) organization's response, or (c) I would like to hear your reflection")
  topic = input()
  
  if topic.lower() == "a":
    print("Personal Information of 533 million people in 106 countires were stolen from Facebook including but not limited to phone numbers, full names, locations, some email addresses, and other details from the users profiles. The hacker were malicious actors that had scraped the data by exploiting a vulnerability in a now defunct feature on the platform that allowed users to find each other by phone number")
  
  elif topic.lower() == "b":
    print("The actions that were taken by FaceBook's team were insane. They did not tell ANY Facebook user about this incident as they did not know who to tell but for the following years they improved their security and warned users ahead of time of any crisis")
  
  elif topic.lower() == "c":
    break
  
  else:
    print("Sorry, I didn't catch that. Choose one of the options listed.")
  
  input("Press enter to continue\n")

#Introduces my take
print("\n I'm excited to share my prespective with you. Are you ready to hear my take?")
giveInfo = input("Type 'yes' or 'no'\n")

#Share my take
while giveInfo.lower() == "yes":
  print("What would you like to learn more about? Enter the lowercase letter of the following options: \n(a) realation to the CIA Traid, (b) my reaction, or (c) my advice, or (d) none")
  topic = input()

  if topic.lower() == "a":
    print("The information that was taken was their personal information such as phone numbers, full names, locations, some email addresses, and other details from the users profiles from 533 million users in 106 countries.\n")

  elif topic.lower() == "b":
    print("We disagree with the organization's response because they should have informed the Facebook user that their data was breached")

  elif topic.lower() == "c":
    print("If someone I’m close to were a victim of a data breach, I would talk to them seriously and calmly. I’d explain that even if they haven’t seen any harm yet, their information could still be used in the future—maybe to open credit accounts, file fake taxes, or even pretend to be them online.I’d convince them to take action by saying something like: I know this feels overwhelming, but ignoring it could make things worse. Taking a few steps now can protect your money, your credit, and your identity. It’s better to act early than deal with a bigger problem later. My advice would be: Change your passwords—especially for emails, banking, or anything sensitive. Use two-factor authentication on all accounts that offer it. Check your credit reports and bank statements for anything unusual. Place a fraud alert or credit freeze with credit bureaus if needed. Avoid sharing personal info online—especially your name, address, birthday, or anything that could be used to guess your passwords or security questions.")
    
  elif topic.lower() == "d":
    break

  else:
    print("Sorry, I didn't catch that. Choose one of the options listed.")

  input("Press enter to continue\n")


#Chatbot ends conversation
print("Thanks for chatting with me, and I hope you learned something new!")