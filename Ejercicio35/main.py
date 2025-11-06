def repeat_subjects():
    subjects = ['Matemáticas', 'Física', 'Química', 'Historia','Lingua']
    failed_subjects = []
    marks = []
    counter= 0
    while len(marks) < len(subjects):

        mark = float(input(f"Introduce tu nota en {subjects[counter]} :"))
        if 1 <= mark <= 10: 
            marks.append(mark)
        else:
            print("Introduzca una nota valida(1-10)")

        counter+=1
    
    for i in range(0,len(subjects)):
        if marks[i] < 5:
            failed_subjects.append(subjects[i])

    print("Tiene que repetir: "+",".join(failed_subjects))
repeat_subjects()