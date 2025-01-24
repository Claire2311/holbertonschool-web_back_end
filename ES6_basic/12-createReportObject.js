export default function createReportObject(employeesList) {
  return {
    allEmployees: employeesList,
    getNumberOfDepartments: (obj) => Object.keys(obj).length,
  };
}
