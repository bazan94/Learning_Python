def main():
  print("* * The Wizard Game * *")
  firstQuestion= input("\nHow many Questions do you want to ask the Wizard? ")
  if firstQuestion.isdigit():
    processQuestions(int(firstQuestion))
  else:
    print("That's not a number. The Wizard wants you to go away now!\n\nEND OF PROGRAM")

def processQuestions(num):
  for i in range(num):
    pQuestion= input("\nWhat's your question? ")
    if pQuestion.lower() == "bye":
      print("END OF PROGRAM")
    else:
      answers= getAnswer(pQuestion)
      print(str(i+1)+". " + answers)

  print("You may not ask any more questions!\nEND OF PROGRAM")

def getAnswer(question):
  if question.startswith("Who"):
    return "The Wizard answers: Who, Who... isn't that a sound an owl makes?"
  elif question.startswith("What"):
   return "The Wizard answers: What is the meaning of life?"
  elif question.startswith("How"):
   return "The Wizard answers: How do you do?"
  else:
   return "The Wizard answers: I don't know"

main()
