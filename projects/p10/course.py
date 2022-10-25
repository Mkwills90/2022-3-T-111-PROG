class Student:
    
    def __init__(self, first_name, last_name, id):
        """Constructs a new instance of a Student."""
    
        self.first_name = first_name
        self.last_name = last_name
        self.id = id

    def __str__(self):
        """Returns a string representation of self."""
    
        return f"{self.first_name} {self.last_name}, {self.id}"
    
    
class Course:

    def __init__(self, name):
        """Constructs a new instance of a Course."""
        
        self.name = name
        self.student_list = []
    
    def __str__(self):
        """Returns a string representation of self."""

        return_str = f"{self.name}:"
        for student in self.student_list:
            return_str += f"\n{str(student):>40}"

        return return_str

    def add_student(self, student):
        """Adds the given student to the student list."""

        self.student_list.append(student)
    
    def remove_student(self, student):
        """Removes the given student from the student list."""

        self.student_list.remove(student)

    def find_student_by_id(self, id):
        """Returns the student having the given id, or None if not found."""
        
        for student in self.student_list:
            if student.id == id:
                return student
                
        return None
            
    def clear(self):
        """Clears the list of students."""
        
        self.student_list = []