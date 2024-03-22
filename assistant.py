from openai import OpenAI
from typing_extensions import override
import time

client = OpenAI(api_key='')

def run_audio(audio):
    audio_file= open("", "rb")
    transcription = client.audio.transcriptions.create(
    model="whisper-1", 
    file=audio_file
    )
    print(transcription.text)

def run (inp):

    assistant = client.beta.assistants.retrieve('asst_oZdMzOOHGLxc4sA0pup9bc71')

    thread = client.beta.threads.create()

    message = client.beta.threads.messages.create(
        thread_id=thread.id,
        role="user",
        content=inp
    )

    run = client.beta.threads.runs.create(
      thread_id=thread.id,
      assistant_id=assistant.id,
      instructions='''You are a chatbot designed to assess the grade level of the user you are speaked to. Please respond as follows:
                      Follow up question here, such as "How are you, do you have any hobbies?"\n
                      Question difficulty here, such as "Asked 7th grade level question"\n
                      Previous answer analysis here, such as "The user's previous answer was at a 5th grade level\n
                      Question analysis here, such as "I'm asking the user a 7th grade level because the conversation 
                      hasn't been too long, and they may be at a higher grade level than 5th grade'''
    )

  
    while run.status in ['queued', 'in_progress', 'cancelling']:
        time.sleep(1) # Wait for 1 second
        run = client.beta.threads.runs.retrieve(
            thread_id=thread.id,
            run_id=run.id
    )

    if run.status == 'completed': 
        messages = client.beta.threads.messages.list(
            thread_id=thread.id
        )
        response = messages.data[0].content[0].text.value.split('\n')
        #print (response[1:])
        return response
    else:
        print('I FAILED ', run.status)
    
    return messages.data[0].content[0].text.value