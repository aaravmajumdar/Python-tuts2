student_report = {
    "name":"Shubham",
    "standard":"12th",
    "roll_no":"123",
    "marks":98,
    "eligible":"pass"
}

print(student_report["name"])
print(student_report.get("marks"))
print(student_report.items())
print(student_report.keys())
print(student_report.values())

student_report["dob"] = "12/03/2000"
print(student_report)

student_report.update({"marks":99})
print(student_report)

# student_report.clear()
# student_report.pop("eligible")
# student_report.popitem()

del student_report["roll_no"]
student_report["eligible"] = "fail" 
del student_report
print(student_report)