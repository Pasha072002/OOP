# Exercise
# У цій вправі ви використовуватимете наявну функцію та додасте власну, щоб створити повнофункціональну програму.
# Додайте функцію з іменем, list_benefits() яка повертає такий список рядків:
# "More organized code", "More readable code", "Easier code reuse", "Allowing programmers to share and connect code together"
# Додайте функцію з іменем build_sentence(info), яка отримує один аргумент, що містить рядок, і повертає речення, що починається з 
# заданого рядка та закінчується рядком " is a benefit of functions!"

# Modify this function to return a list of strings as defined above
def list_benefits():
    return "More organized code", "More readable code", "Easier code reuse", "Allowing programmers to share and connect code together"

# Modify this function to concatenate to each benefit - " is a benefit of functions!"
def build_sentence(benefit):
    return "%s is a benefit of functions!" % benefit

def name_the_benefits_of_functions():
    list_of_benefits = list_benefits()
    for benefit in list_of_benefits:
        print(build_sentence(benefit))

name_the_benefits_of_functions()

