import voice_text.record as record
import random
import voice_text.transcriptions as transcriptions
import os

def main():
    unique_id = ''.join(random.choices('0123456789abcdef', k=6))
    print(unique_id)
    user_audio_file = os.path.join(os.getcwd(), f"recorded-files/user_audio{unique_id}.wav")
    # save the recorded sound in the location
    record.voice(user_audio_file)
    transcriptions.voice_to_text(user_audio_file)

if __name__ == "__main__":
    main()