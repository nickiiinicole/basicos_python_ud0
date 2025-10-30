def ask_marks(subjects):

    marks = []
    for subject in subjects:
        input_valid = False
        while not input_valid:
            mark =float(input(f"Introduzca la nota de la asignatura {subject}: "))
            if mark<0 or mark>10:
                print("Porfavor introduzca una nota valida")
            else:
                input_valid=True
        marks.append(mark)     
    return marks

subjects = ["Matemáticas", "Física", "Química", "Historia", "Lingua"]
subjects.sort(key=str.lower)
marks = ask_marks(subjects)
for i in range(0, len(subjects)):
    print(f"En la materia {subjects[i]} sacaste un {marks[i]:.2f}")


