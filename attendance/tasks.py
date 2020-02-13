import face_recognition
import numpy as np


def get_encodings_from_profile_pic(picture):
    processed_pic = face_recognition.load_image_file(picture)
    face_encodings = face_recognition.face_encodings(processed_pic)[0]
    print(face_encodings)
    return face_encodings.dumps()


def identify_students_in_pic(students,picture):

    
    image = face_recognition.load_image_file(picture)
    encodings = face_recognition.face_encodings(image)

    prescent_student_ids = []

    for encoding in encodings:
        for student in students:
            try:
                student_pic_encodings =  np.loads(student.face_encodings)
                results = face_recognition.compare_faces([encoding], student_pic_encodings)
                if results[0]:
                    if not student.id in prescent_student_ids:
                        prescent_student_ids.append(student.id)

            except:
                print("Student does not have any face encodings")
    return prescent_student_ids