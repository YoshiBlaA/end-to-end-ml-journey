import operator

def person_lister(f):
    def inner(people):
        sorted_people = sorted(people, key=lambda p: int(p[2]))
        formatted_people = [f(person) for person in sorted_people]
        return formatted_people
    return inner

"""
def person_lister(f):
    def inner(people):
        sorted_people = sorted(people, key=lambda p: int(operator.itemgetter(2)(p)))
        formatted_people = [f(person) for person in sorted_people]
        return formatted_people
    return inner
"""

@person_lister
def name_format(person):
    return ("Mr. " if person[3] == "M" else "Ms. ") + person[0] + " " + person[1]
"""
    name_format = person_lister(name_format(person))
    name_format = inner(people)
"""



if __name__ == '__main__':
    people = [input().split() for i in range(int(input()))]
    
    """
    people =[
             ['Mike', 'Thomson', '20', 'M'],
             ['Robert', 'Bustle', '32', 'M'],
             ['Andria', 'Bustle', '30', 'F']
            ]
    """
    
    print(*name_format(people), sep='\n')