import openai
import speech_recognition as sr

#Vocal to Text

def recognition (filename):

    r = sr.Recognizer()
    
    with sr.AudioFile(filename) as source:
        #Listen data from file
        audio_data = r.record(source)
        #Recognize and transcribe
        text = r.recognize_google(audio_data)
        print(text)
        print("Done")
        return text 

def request (request):
    api_key = "Replace with API"
    openai.api_key = api_key
    response = openai.Completion.create(
        engine="davinci",
        prompt = 'request',
        max_tokens = 50
    )
    generated_text = response.choices[0].text
    print(generated_text)
    return(generated_text)

