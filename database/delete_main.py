import course_dao
course_id = int(input("Enter course id to be deleted: "))

df = course_dao.get_course_by_id(course_id)

if(df.empty):
    print(f"Course with id = {course_id} not Found!!")
else:
    course_dao.delete_course(course_id)