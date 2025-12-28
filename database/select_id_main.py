import course_dao

df = course_dao.get_course_by_id(200)

if(df.empty):
    print("No Data Found!, Please Insert")
else:
    print(df)