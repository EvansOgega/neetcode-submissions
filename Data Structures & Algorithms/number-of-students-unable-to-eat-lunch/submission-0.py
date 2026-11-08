class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        num_not_eat = 0
        while num_not_eat < len(students):
            if(students[0] == sandwiches[0]):
                students.pop(0)
                sandwiches.pop(0)
                num_not_eat = 0
            else:
                students.append(students.pop(0))
                num_not_eat = num_not_eat + 1
        return num_not_eat