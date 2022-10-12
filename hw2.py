from pymongo import MongoClient
import pprint
client = MongoClient("mongodb+srv://1092936:1234@cluster0.azqipfn.mongodb.net/?retryWrites=true&w=majority")
db = client["hw2"]
#drop database"hw2"
db.hw2.drop()
db = client["big_data_hw2"]
class_colle = db["class"]
class_colle.delete_many({})
class_colle.insert_one({"class_id":"c1", "class_name": "Underwater basket weaving"})
class_colle.insert_one({"class_id":"c2", "class_name": "Home fusion made easy"})
class_colle.insert_one({"class_id":"c3", "class_name": "How to train an attack iguana"})
class_colle.insert_one({"class_id":"c4", "class_name": "Learn SQL for fun and profit"})
stu_colle = db["stu"]
stu_colle.delete_many({})
stu_colle.insert_one({"stu_id":"s1", "stu_name": "Brett"})
stu_colle.insert_one({"stu_id":"s2", "stu_name": "Rick"})
stu_colle.insert_one({"stu_id":"s3", "stu_name": "Susanna"})
stu_colle.insert_one({"stu_id":"s4", "stu_name": "Jennifer"})
grade_colle = db["grade"]
grade_colle.delete_many({})
grade_colle.insert_one({"stu_id":"s1", "class_id":"c1", "grade":2})
grade_colle.insert_one({"stu_id":"s2", "class_id":"c1", "grade":99})
grade_colle.insert_one({"stu_id":"s3", "class_id":"c1", "grade":65})
grade_colle.insert_one({"stu_id":"s4", "class_id":"c1", "grade":3})
grade_colle.insert_one({"stu_id":"s2", "class_id":"c2", "grade":38})
grade_colle.insert_one({"stu_id":"s3", "class_id":"c2", "grade":88})
grade_colle.insert_one({"stu_id":"s4", "class_id":"c2", "grade":48})
grade_colle.insert_one({"stu_id":"s1", "class_id":"c3", "grade":7})
grade_colle.insert_one({"stu_id":"s4", "class_id":"c3", "grade":32})
grade_colle.insert_one({"stu_id":"s1", "class_id":"c4", "grade":94})
grade_colle.insert_one({"stu_id":"s2", "class_id":"c4", "grade":63})
grade_colle.insert_one({"stu_id":"s3", "class_id":"c4", "grade":75})
grade_colle.insert_one({"stu_id":"s4", "class_id":"c4", "grade":20})
print("students who took the course named ”Home fusion made easy”")
for x in grade_colle.find({"class_id":"c2"}):
    list_of_stu_id = x["stu_id"]
    for y in stu_colle.find({"stu_id":list_of_stu_id}): 
        print(y["stu_name"])
print("Jennifer’s grade on the course named ”Learn SQL for fun and profit.”")
for x in grade_colle.find({"stu_id":"s4", "class_id":"c4"}):
    print(x["grade"])