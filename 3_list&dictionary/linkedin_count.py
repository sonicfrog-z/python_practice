def get_skills(endorsements):
    result = {}

    for name, skills in endorsements.items():
        for skill in skills:
            result.setdefault(skill, [])
            result[skill].append(name)

    return result


endorsements = {
    'Bob': ['Python', 'Java', 'HTML', 'CSS', 'C++'],
    'David': ['Python', 'WebDev', 'JavaScript'],
    'Eric': ['Java', 'HTML', 'SQL'],
    'Frank': ['CSS', 'Python']
}

skills = get_skills(endorsements)
print(skills)
# {'Python': 3, 'Java': 2, 'HTML': 1, 'CSS': 2, 'C++': 1, ...}
# {'Python': ['Bob', 'David', 'Frank'], 'Java': ['Bob', 'Eric'], ...}
