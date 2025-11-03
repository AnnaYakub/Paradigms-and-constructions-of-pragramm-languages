class Student:
    """Класс «Студент», содержащий поля:
    ● ID записи о студенте;
    ● Фамилия студента;
    ● Средний балл (количественный признак);
    ● ID записи о группе. (для реализации связи один-ко-многим)"""
    
    def __init__(self, student_id, last_name, average_grade, group_id):
        self.student_id = student_id
        self.last_name = last_name
        self.average_grade = average_grade
        self.group_id = group_id
    
    def __repr__(self):
        return f"Student(ID={self.student_id}, Фамилия='{self.last_name}', Средний балл={self.average_grade}, GroupID={self.group_id})"
class StudyGroup:
    def __init__(self, group_id, group_name):
        self.group_id = group_id
        self.group_name = group_name
    
    def __repr__(self):
        return f"StudyGroup(ID={self.group_id}, Наименование='{self.group_name}')"
class StudentCourse:
    """Класс «Студенты курса», содержащий поля:
    ● ID записи о студенте;
    ● ID записи о группе.
    (Для реализации связи многие-ко-многим)"""
    
    def __init__(self, student_id, group_id):
        self.student_id = student_id
        self.group_id = group_id
    
    def __repr__(self):
        return f"StudentCourse(StudentID={self.student_id}, GroupID={self.group_id})"
def main():
    print("=" * 80)
    print("РУБЕЖНЫЙ КОНТРОЛЬ №1")
    print("Предметная область: Студенческая группа и Учебный курс")
    print("=" * 80)
    groups = [
        StudyGroup(1, "ИТ-101"),
        StudyGroup(2, "ПИ-202"),
        StudyGroup(3, "Отдел математики"),
        StudyGroup(4, "ФИ-404"),
        StudyGroup(5, "Отдел программирования")
    ]
    students = [
        Student(1, "Иванов", 4.5, 1),
        Student(2, "Петров", 3.8, 1),
        Student(3, "Сидоров", 4.2, 2),
        Student(4, "Кузнецов", 3.9, 2),
        Student(5, "Смирнов", 4.8, 3),
        Student(6, "Васильев", 4.1, 4),
        Student(7, "Попов", 3.7, 5)
    ]
    student_courses = [
        StudentCourse(1, 1),  
        StudentCourse(2, 1),  
        StudentCourse(3, 2),  
        StudentCourse(4, 2), 
        StudentCourse(5, 3),  
        StudentCourse(6, 4),  
        StudentCourse(7, 5),  
        StudentCourse(1, 3),  
        StudentCourse(3, 5)   
    ]
    
    print("\nТЕСТОВЫЕ ДАННЫЕ")
    print("-" * 40)
    
    print("\nУчебные группы:")
    for group in groups:
        print(f"  {group}")
    
    print("\nСтуденты:")
    for student in students:
        print(f"  {student}")
    
    print("\nСвязи студентов и групп (многие-ко-многим):")
    for sc in student_courses:
        print(f"  {sc}")
    print("\n" + "=" * 80)
    print("РЕЗУЛЬТАТЫ ВЫПОЛНЕНИЯ ЗАПРОСОВ")
    print("=" * 80)
    print("\nЗАПРОС 1: Список всех связанных студентов и групп (отсортированный по группам)")
    print("-" * 60)
    groups_dict = {group.group_id: group for group in groups}
    students_by_group = {}
    for student in students:
        if student.group_id not in students_by_group:
            students_by_group[student.group_id] = []
        students_by_group[student.group_id].append(student)
    sorted_groups = sorted(groups, key=lambda g: g.group_name)
    
    for group in sorted_groups:
        group_students = students_by_group.get(group.group_id, [])
        print(f"\nГруппа: {group.group_name}")
        if group_students:
            for student in sorted(group_students, key=lambda s: s.last_name):
                print(f"  └─ {student.last_name} (средний балл: {student.average_grade})")
        else:
            print("  └─ В группе нет студентов")
    print("\nЗАПРОС 2: Список групп с суммарным средним баллом студентов")
    print("-" * 60)
    group_total_grades = [
        (group, 
         sum(student.average_grade for student in students if student.group_id == group.group_id),
         len([student for student in students if student.group_id == group.group_id]))
        for group in groups
    ]
    group_total_grades.sort(key=lambda x: x[1], reverse=True)
    
    for group, total_grade, student_count in group_total_grades:
        avg_per_student = total_grade / student_count if student_count > 0 else 0
        print(f"\nГруппа: {group.group_name}")
        print(f"  Количество студентов: {student_count}")
        print(f"  Суммарный средний балл: {total_grade:.2f}")
        print(f"  Средний балл на студента: {avg_per_student:.2f}")
    print("\nЗАПРОС 3: Список всех групп с 'отдел' в названии и их студенты")
    print("-" * 60)
    
    department_groups = [group for group in groups if "отдел" in group.group_name.lower()]
    
    students_dict = {student.student_id: student for student in students}
    
    for group in department_groups:
        print(f"\nГруппа: {group.group_name}")
        group_student_ids = [sc.student_id for sc in student_courses if sc.group_id == group.group_id]
        group_students = [students_dict[student_id] for student_id in group_student_ids]
        
        if group_students:
            for student in sorted(group_students, key=lambda s: s.last_name):
                print(f"  └─ {student.last_name} (средний балл: {student.average_grade})")
        else:
            print("  └─ В этой группе нет студентов")
    print("\n" + "=" * 80)
    print("ДОПОЛНИТЕЛЬНЫЙ АНАЛИЗ")
    print("=" * 80)
    student_group_count = {}
    for sc in student_courses:
        student_group_count[sc.student_id] = student_group_count.get(sc.student_id, 0) + 1
    
    multi_group_students = [(student_id, count) for student_id, count in student_group_count.items() if count > 1]
    
    if multi_group_students:
        print("\nСтуденты, обучающиеся в нескольких группах:")
        for student_id, count in multi_group_students:
            student = students_dict[student_id]
            student_groups = [groups_dict[sc.group_id].group_name for sc in student_courses if sc.student_id == student_id]
            print(f"  {student.last_name}: {count} групп - {', '.join(student_groups)}")
    else:
        print("\nНет студентов, обучающихся в нескольких группах")


if __name__ == "__main__":
    main()