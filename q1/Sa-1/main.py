class AssignmentSubmissions:


    def __init__(self, student_name: str, student_id: str, assignment_title: str, due_date: str):
        self.student_name = student_name
        self.student_id = student_id
        self._assignment_title = assignment_title
        self._due_date = due_date
        self.__is_submitted = False
        self.__grade = "Not Graded"
        self.__submitted_files = []
   
    def __validate_grade(self, score: float) -> bool:
        return True if 0.0 <= score <= 100.0 else False

    def __check_submission_status(self) -> bool:
        self.__is_submitted = len(self.__submitted_files) > 0
        return self.__is_submitted

    def is_duplicate_file(self, file_name: str) -> bool:
            return file_name in self.__submitted_files

    def add_file(self, file_name: str) -> None:
            if self.is_duplicate_file(file_name):
                print(f"--> [Warning] '{file_name}' already exists in the submission.")
            else:
                self.__submitted_files.append(file_name)
                self.__is_submitted = True
                print(f"--> [Success] {self.student_name} attached '{file_name}'. Total files: {len(self.__submitted_files)}")

    def remove_file(self, file_name: str) -> None:
            if self.__grade != "Not Graded":
                print(f"--> [Warning] {self.student_name} cannot remove files after grading. Assignment is already graded.")
                return
            if file_name in self.__submitted_files:
                self.__submitted_files.remove(file_name)
                print(f"--> [Success] {self.student_name} removed '{file_name}'.")

    def assign_grade(self, score: float) -> None:
            if self.__check_submission_status() == False:
                print(f"--> [Error] Cannot grade. No files submitted for {self.student_name}.")
                return
            if self.__validate_grade(score):
                self.__grade = score
                print(f"--> [Success] Grade {score} officially assigned to {self.student_name}.")
           
    def view_files(self) -> str:
        return ', '.join(self.__submitted_files) if self.__submitted_files else "No files submitted."

    def get_status_report(self) -> str:
        return f"ID: {self.student_id} | Name: {self.student_name} | Status: {'Submitted' if self.__check_submission_status() else 'Missing'} ({len(self.__submitted_files)} files) | Grade: {self.__grade}"

    def get_grade(self) -> str:
        return self.__grade

print("--- INITIALIZNG DROPBOX FOR STUDENTS ---")
student1 = AssignmentSubmissions(student_name="Alex Gonzaga", student_id="pshs-1090-x", assignment_title="CS-101", due_date="2026-10-01")
student2 = AssignmentSubmissions(student_name="Adelle", student_id="pshs-1920-x", assignment_title="CS-103", due_date="2026-10-01")
student3 = AssignmentSubmissions(student_name="Juan dela Cruz", student_id="pshs-1033-x", assignment_title="CS-101", due_date="2026-10-01")
student4 = AssignmentSubmissions(student_name="Maria Santos", student_id="pshs-1044-x", assignment_title="CS-101", due_date="2026-10-01")
student5 = AssignmentSubmissions(student_name="Jose Reyes", student_id="pshs-1055-x", assignment_title="CS-101", due_date="2026-10-01")
print()

print("--- TEST SCENARIO 1: Multiple Files via List ---")
student1.add_file("main.py")
student1.add_file("report.pdf")
student1.assign_grade(95)
print(f"Alex's Files: {student1.view_files()}\n")

print("--- TEST SCENARIO 2: Removing Files from List ---")
student2.add_file("wrong_homework.docx")
student2.remove_file("wrong_homework.docx")
student2.add_file("correct_project.py")
student2.assign_grade(88)
print(f"Adelle's Files: {student2.view_files()}\n")

print("--- TEST SCENARIO 3: Preventing Duplicate Files ---")
student3.add_file("script.py")
student3.add_file("script.py")  #Should trigger private duplicate check
print(f"Juan's Files: {student3.view_files()}\n")

print("--- TEST SCENARIO 4: Removing file after being graded ---")
student4.add_file("exam_answers.pdf")
student4.assign_grade(75)
student4.remove_file("exam_answers.pdf")  #Blocked by grading status
print()

print("--- TEST SCENARIO 5: Empty List Handling ---")
student5.add_file("draft.txt")
student5.remove_file("draft.txt")
student5.assign_grade(100) #Should fail because list is empty
print()

print("--- FINAL SYSTEM REPORT ---")
print(student1.get_status_report())
print(student2.get_status_report())
print(student3.get_status_report())
print(student4.get_status_report())
print(student5.get_status_report())
