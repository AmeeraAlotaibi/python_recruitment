def get_skills():
    # Add at least 3 random skills for the user to select from
    return ["JavaScript", "Python", "Flutter"]


def show_skills(skills):
    # Pretty print skills to the user
    # Write your code here
    print("Skills: ")
    for i, skill in enumerate(skills, 1):
        print(f"{i}. {skill}")

    

# returns a list
def get_user_skills(skills):
    # Show the available skills and have user pick from them
    # Write your code here
    user_skills = []
    first_skill = input("Choose a skill from above by typing its number: ")
    if first_skill == "1":
        user_skills.append(get_skills()[0])
    elif first_skill == "2":
        user_skills.append(get_skills()[1])
    elif first_skill == "3":
        user_skills.append(get_skills()[2])
    else: 
        print("Invalid number")
    
    second_skill = input("Choose another skill: ")
    if second_skill == "1":
        user_skills.append(get_skills()[0])
    elif second_skill == "2":
        user_skills.append(get_skills()[1])
    elif second_skill == "3":
        user_skills.append(get_skills()[2])
    else: 
        print("Invalid number")

    return user_skills

    

# returns a Dictionary
def get_user_cv(name, age, exp, skills):
    # Get the users CV from their inputs
    # Write your code here
    cv = {"name": name, "age": age, "experience": exp, "skills": skills}
    return cv
    
    


def check_acceptance(cv, desired_skill):
    # Check if the cv is acceptable or not and return a boolean based on that
    # Write your code here
    if cv["age"] >= 25 & cv["age"] < 40:
        if cv["experience"] > 3:
            if desired_skill in cv["skills"]:
                return True
            else:
                return False
        else: 
            return False
    else: 
        return False
    


def main():
    # Write your main logic here by combining the functions above into the
    # desired outcome
    print("Welcome to the special recruitment program, please answer the following questions:")
    name = input("Whats your name? ")
    age = int(input("How old are you? "))
    exp = int(input("How many years of experience do you have? "))
    cv = get_user_cv(name, age, exp, get_user_skills(show_skills(get_skills())))
    
    if check_acceptance(cv, "Python") == True:
        print(f"Congrats {cv['name']}, You have been ACCEPTED")
    else: 
        print(F"Sorry {cv['name']}, You have been Rejected.")
    

    


if __name__ == "__main__":
    main()
