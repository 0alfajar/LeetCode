# Write your MySQL query statement below
SELECT Students.student_id, Students.student_name, Subjects.subject_name, COUNT(Examinations.student_id) AS attended_exams
FROM Students
CROSS JOIN Subjects
LEFT JOIN Examinations ON Examinations.subject_name = Subjects.subject_name AND Examinations.student_id = Students.student_id
GROUP BY Students.student_id, Students.student_name, Subjects.subject_name
ORDER BY Students.student_id;