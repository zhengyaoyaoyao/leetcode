from typing import List


class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        for i in range(len(sandwiches)):
            if sandwiches[i] in students:
                students.remove(sandwiches[i])
            else:
                break
        return len(students)


if __name__ == '__main__':
    print(8*24*2*2)