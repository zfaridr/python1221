tutors = [
    'Иван', 'Анастасия', 'Петр', 'Сергей',
    'Дмитрий', 'Борис', 'Елена'
]
klasses = [
    '9А', '7В', '9Б', '9В', '8Б', '10А'
]
tutors_klasses_tutors_gen = (tutor for tutor in tutors)
tutors_klasses_klasses_gen = (klass for klass in klasses)

for i in range(len(tutors)):
    if i > (len(klasses) - 1):
        a = (next(tutors_klasses_tutors_gen), 'None')
    else:
        a = (next(tutors_klasses_tutors_gen), next(tutors_klasses_klasses_gen))
    print (type(a), a)

next(tutors_klasses_tutors_gen)
next(tutors_klasses_klasses_gen)

