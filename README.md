# DiaryEntry
A simple diary entry program with password encryption.
lockout_count = 0: Initializes the lockout counter to zero at the start of the read_entries() function.
while lockout_count < 3:: A while loop runs as long as lockout_count is less than 3, allowing up to 3 attempts.
lockout_count += 1: If the passcode is incorrect, the counter is incremented.
print(f"Access Denied. Try Again. {3-lockout_count} attempts remaining."): A message is printed informing the user of incorrect attempts and remaining attempts.
if lockout_count == 3:: After 3 incorrect attempts, the account is locked, and a message is printed.
break: The break statement exits the while loop if the correct passcode is entered.
Now, if the user enters the wrong passcode three times, they'll be locked out, and the read_entries() function will stop
