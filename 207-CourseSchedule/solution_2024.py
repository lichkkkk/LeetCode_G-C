class Solution:
    def canFinish(self, num_courses: int, prereqs: List[List[int]]) -> bool:
        course_no_prereq = []
        course_num_prereq_map = [0] * num_courses
        course_prereq_reverse_map = [[] for i in range(num_courses)]

        # construct initial state
        for course, prereq in prereqs:
          course_num_prereq_map[course] += 1
          course_prereq_reverse_map[prereq].append(course)
        for course in range(num_courses):
          if not course_num_prereq_map[course]:
            course_no_prereq.append(course)

        # start to take courses
        num_course_taken = 0
        while course_no_prereq:
          course_taked = course_no_prereq.pop()
          num_course_taken += 1
          for course_impacted in course_prereq_reverse_map[course_taked]:
            course_num_prereq_map[course_impacted] -= 1
            if not course_num_prereq_map[course_impacted]:
              course_no_prereq.append(course_impacted)

        return num_course_taken == num_courses
