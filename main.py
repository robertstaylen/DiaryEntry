import datetime

def create_entry():
  date = input("Enter Today's Date (YYYY-MM-DD): ")
  text = input("Write today's entry:")

  entry = f"{date}: {text}"
  with open("diary.txt",'a') as file:
    file.write(entry + "\n")
  print("Diary Entry created successfully!")

def read_entries():
  lockout_count = 0
  while lockout_count < 3:
    passcode = input ("PASSCODE: ")
    if passcode == "#401243":
      with open("diary.txt", "r") as file:
        entries = file.readlines()
      if not entries:
        print("No entries found.")
      else:
        for index, entry in enumerate(entries,start=1):
          print(f"Entry {index}:{entry}")
      break
    else:
      lockout_count += 1
      print(f"Access Denied. Try Again. {3-lockout_count} attempts remaining.")
  if lockout_count == 3:
    print("Account locked. Please try again later.")


while True:
  print("1. Create a new entry.")
  print("2. Read previous entries.")
  print("3. Exit")
  choice = input("Enter your choice (1-3): ")


  if choice == "1":
    create_entry()
  elif choice == "2":
    read_entries()
  elif choice == "3":
    break
  else:
    print("Please Try Again.")
  


