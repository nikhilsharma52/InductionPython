from datetime import datetime

with open("activity.txt", "a") as file:
    file.write("Program ran at " + str(datetime.now()) + "\n")
