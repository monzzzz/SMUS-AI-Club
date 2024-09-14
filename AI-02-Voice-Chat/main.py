import record
import random
import transcriptions

def main():
    unique_id = ''.join(random.choices('0123456789abcdef', k=6))
    print(unique_id)
    user_audio_file = f"recorded-files/user_audio{unique_id}.wav"
    # save the recorded sound in the location
    record.voice(user_audio_file)
    transcriptions.voice_to_text(user_audio_file)

if __name__ == "__main__":
    main()