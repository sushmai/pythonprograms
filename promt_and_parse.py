from sys import argv

script, user_name = argv
prompt = '>'
promt = "*"

print(f"Hi {user_name}, I am {script}.")
print("I would like to ask few questions.")
print(f"do you like me {user_name}?")
likes = input(prompt)

print(f"where do you live {user_name}?")
lives = input(prompt)

print(f"so you said {likes} about me and lives at {lives}")
