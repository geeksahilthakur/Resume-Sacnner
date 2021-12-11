import pyttsx3
import docx2txt
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
print(voices)
engine.setProperty('voice', voices[0].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


job_description = docx2txt.process("D:\Mocker AI Data\Resume Scanner\Job description.docx")
resume = docx2txt.process("D:\Mocker AI Data\Resume Scanner\Resume1.docx")

content = [job_description, resume]
cv = CountVectorizer()
matrix = cv.fit_transform(content)
similarity_matrix = cosine_similarity(matrix)
print(similarity_matrix)

print(' The % of correct answer is : '+ str(similarity_matrix[1][0]*100)+ '%')
speak(' The % of correct answer is : '+ str(similarity_matrix[1][0]*100)+ '%')


