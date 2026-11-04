def is_adult(age):
    if age < 18:
        return "PENDING"
    elif age > 120:
        return "SERIOUSLY?"
    else:
        return "VALIDATION IN PROGRESS ... PLEASE WAIT..."


# Handles bachelor degree input variations cleanly
def degree_2_options(degree_input):
    # .lower() ensures we catch 'yes', 'Yes', 'YES' all at once
    if degree_input.strip().lower() == "yes":
        return "PLEASE WAIT"
    elif degree_input.strip().lower() == "no":
        return "PLEASE HOLD ON"
    else:
        return "PLEASE ANSWER WITH 'YES' OR 'NO': "


# Full validation of the candidate based on numerical age
def complete_validation(age):
    if age > 120:
        return "... ARE YOU A ROBOT?"
    elif age >= 18:
        return "VALIDATION SUCCESSFUL"
    else:
        return " ... YOU ARE NOT AN ELIGIBLE CANDIDATE FOR THIS OFFER"


# ==========================================
# 2. TERMINAL USER INPUT & PROCESSING
# ==========================================

# Safe age input loop (filters out letters/symbols)
while True:
    try:
        age_input = input("Please type in your age: ")
        age = int(age_input)  # Successfully updates 'age' as an integer
        break  # Escapes the loop if conversion works
    except ValueError:
        print("❌ Please type in your age")

print("ARE YOU A UNIVERSITY GRADUATE: ")
degree = input()

print("DO YOU HAVE A BACHELORS DEGREE IN YOUR FIELD OF STUDY (YES,NO)? ")
degree_2 = input()

print("DO YOU PREFER WORKING AT HOME?")
job_offer = input()

# Process inputs through our corrected functions
result = is_adult(age)
credit = degree_2_options(degree_2)
validation = complete_validation(age)    

# Print terminal summary
print(f"{credit} ... {result}   {validation}")


# ==========================================
# 3. FLASK WEB SERVER BLOCK
# ==========================================
# CRITICAL FIX: This must stay at the absolute bottom. 
# Once app.run() executes, it blocks further code execution to run the server.

