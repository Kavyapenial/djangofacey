import face_recognition
import numpy as np



class StudentObject(object):
    def __init__(self,id, name, batch, reg_id, profile, is_present):
        self.id = id
        self.name = name
        self.batch = batch
        self.reg_id = reg_id
        self.profile = profile
        self.is_present = is_present

def get_encodings_from_profile_pic(picture):
    processed_pic = face_recognition.load_image_file(picture)
    face_encodings = face_recognition.face_encodings(processed_pic)[0]
    return face_encodings.dumps()


def identify_students_in_pic(students,picture, StudentObject):

    
    image = face_recognition.load_image_file(picture)
    encodings = face_recognition.face_encodings(image)

    prescent_student_ids= []
    stud_results = []

    print(encodings)

    for encoding in encodings:
        print("hello")
        for student in students:
            student_pic_encodings =  np.loads(student.face_encodings)
            results = face_recognition.compare_faces([encoding], student_pic_encodings)
            print(student.id)
            if results[0]:
                if not student.id in prescent_student_ids:
                    prescent_student_ids.append(student.id)
                    stud_results.append(StudentObject(student.id, student.name, student.batch.id, student.reg_id, student.profile, True))
            
    for student in students:
        if not student.id in prescent_student_ids:
             stud_results.append(StudentObject(student.id, student.name, student.batch.id, student.reg_id, student.profile, False))

    return stud_results

