import course_dao
course_id = int(input("Enter course id to be updated: "))

df = course_dao.get_course_by_id(course_id)

if(df.empty):
    print(f"Course with id = {course_id} not Found!!")
else:
    print(df)
    updated_course_name = input("Enter updated course name: ")
    updated_course_duration = input("Enter updated course duration: ")
    updated_course_desc = input("Enter updated course description: ")
    course_dao.update_course(course_id, updated_course_desc, updated_course_name, updated_course_duration)
    print(course_dao.get_all_courses())