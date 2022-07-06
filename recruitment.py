def get_skills():
    # Add at least 3 random skills for the user to select from
    return ["JavaScript", "Python", "Flutter"]


def show_skills(skills):
    # Pretty print skills to the user
    print("Skills: ")
    for i, skill in enumerate(skills, 1):
        print(f"{i}. {skill}")
    

def get_user_skills(skills):
    # Show the available skills and have user pick from them
    selections = get_skills()
    show_skills(selections)
    user_choices = [
        int(input("Choose a skill from above by typing its number: ")), 
        int(input("Choose another skill: "))
        ]
    user_skills = [(selections[choice - 1]) for choice in user_choices]
    return user_skills
    

def get_user_cv(skills):
    # Get the users CV from their inputs
    name = input("Whats your name? ")
    age = int(input("How old are you? "))
    exp = int(input("How many years of experience do you have? "))
    get_skills = get_user_skills(skills)
    cv = {
        "name": name, 
        "age": age, 
        "experience": exp, 
        "skills": get_skills
        }
    return cv
    
    


def check_acceptance(cv, desired_skill):
    # Check if the cv is acceptable or not and return a boolean based on that
    if (cv["age"] >= 25 and 
        cv["age"] < 40 and 
        cv["experience"] > 3 and 
        desired_skill in cv["skills"]
       ):
        print(f"Congrats, {cv['name']}! You have been Accepted!")
        return True
    else: 
        print(f"Sorry, {cv['name']}. You have been Rejected!")
        return False
    


def main():
    # Write your main logic here by combining the functions above into the
    # desired outcome
    print("Welcome to the special recruitment program, please answer the following questions:")
    skills = get_skills()
    cv = get_user_cv(skills)
    check_acceptance(cv, "Python")    
    

    


if __name__ == "__main__":
    main()
