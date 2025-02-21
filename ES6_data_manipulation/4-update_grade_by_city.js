export default function updateStudentGradeByCity(students, city, newGrades) {
  const locStudents = students.filter((student) => student.location === city);

  return locStudents.map((student) => {
    const newGrade = newGrades.filter(
      (grade) => grade.studentId === student.id
    );
    if (newGrade.length > 0) {
      return { ...student, grade: newGrade[0].grade };
    } else {
      return { ...student, grade: "N/A" };
    }
  });
}
