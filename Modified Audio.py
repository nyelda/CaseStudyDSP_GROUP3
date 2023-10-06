from google.colab import drive
drive.mount('/content/drive')


import os
import numpy as np
import scipy.signal as signal
import librosa
import soundfile as sf


#CHIPMUNK#
# Set the directory paths
input_directory = '/content/drive/MyDrive/DSP - CASE STUDY DUB/Original Audio '
output_directory = '/content/drive/MyDrive/DSP - CASE STUDY DUB/Modified Audio'  # New output directory

# Get a list of all audio files in the input directory
audio_files = [f for f in os.listdir(input_directory) if f.endswith('.wav')]

# Process each audio file
for audio_file_name in audio_files:
    # Load the audio file
    audio_file_path = os.path.join(input_directory, audio_file_name)
    audio_file, sr = librosa.load(audio_file_path, sr=None)

    # Adjust the pitch (n_steps) to control the pitch change
    shifted_audio = librosa.effects.pitch_shift(audio_file, n_steps=5, sr=sr)  # Increase n_steps for a higher-pitched voice

    # Adjust the resampling factor to control the time stretching
    stretched_audio = signal.resample(shifted_audio, int(len(shifted_audio) * 0.9))  # Decrease the factor for less time stretching

    # Adjust the cutoff frequency as needed for filtering
    cutoff_hz = 4000
    nyquist = 0.5 * sr
    normal_cutoff = cutoff_hz / nyquist

    # Design a low-pass Butterworth filter
    b, a = signal.butter(6, normal_cutoff, btype='low', analog=False)

    # Apply the filter to the audio
    filtered_audio = signal.filtfilt(b, a, stretched_audio)

    # Get the output file path in the new directory
    output_file_path = os.path.join(output_directory, audio_file_name.replace('.wav', '_filtered.wav'))

    # Save the processed audio as a WAV file in the new directory
    sf.write(output_file_path, filtered_audio, sr)


#ROBOCOP#
# Set the directory paths
input_directory = '/content/drive/MyDrive/DSP - CASE STUDY DUB/Original Audio '
output_directory = '/content/drive/MyDrive/DSP - CASE STUDY DUB/Modified Audio - Robocop'  # New output directory

# Get a list of all audio files in the input directory
audio_files = [f for f in os.listdir(input_directory) if f.endswith('.wav')]

# Process each audio file
for audio_file_name in audio_files:
    # Load the audio file
    audio_file_path = os.path.join(input_directory, audio_file_name)
    audio_file, sr = librosa.load(audio_file_path, sr=None)

    # Adjust the pitch (n_steps) to create a "Robocop" effect
    shifted_audio = librosa.effects.pitch_shift(audio_file, n_steps=-5, sr=sr)  # Decrease n_steps for a lower-pitched voice

    # Adjust the resampling factor to control the time stretching
    stretched_audio = signal.resample(shifted_audio, int(len(shifted_audio) * 0.9))  # Decrease the factor for less time stretching

    # Adjust the cutoff frequency as needed for filtering
    cutoff_hz = 4000
    nyquist = 0.5 * sr
    normal_cutoff = cutoff_hz / nyquist

    # Design a low-pass Butterworth filter
    b, a = signal.butter(6, normal_cutoff, btype='low', analog=False)

    # Apply the filter to the audio
    filtered_audio = signal.filtfilt(b, a, stretched_audio)

    # Get the output file path in the new directory
    output_file_path = os.path.join(output_directory, audio_file_name.replace('.wav', '_robocop.wav'))

    # Save the processed audio as a WAV file in the new directory
    sf.write(output_file_path, filtered_audio, sr)


#ALIEN#
# Set the directory paths
input_directory = '/content/drive/MyDrive/DSP - CASE STUDY DUB/Original Audio '
output_directory = '/content/drive/MyDrive/DSP - CASE STUDY DUB/Modified Audio - Alien'  # New output directory

# Get a list of all audio files in the input directory
audio_files = [f for f in os.listdir(input_directory) if f.endswith('.wav')]

# Process each audio file
for audio_file_name in audio_files:
    # Load the audio file
    audio_file_path = os.path.join(input_directory, audio_file_name)
    audio_file, sr = librosa.load(audio_file_path, sr=None)

    # Adjust the pitch (n_steps) to create an "alien" effect
    shifted_audio = librosa.effects.pitch_shift(audio_file, n_steps=-10, sr=sr)  # Decrease n_steps for a lower-pitched voice

    # Adjust the resampling factor to control the time stretching
    stretched_audio = signal.resample(shifted_audio, int(len(shifted_audio) * 0.9))  # Decrease the factor for less time stretching

    # Adjust the cutoff frequency as needed for filtering
    cutoff_hz = 4000
    nyquist = 0.5 * sr
    normal_cutoff = cutoff_hz / nyquist

    # Design a low-pass Butterworth filter
    b, a = signal.butter(6, normal_cutoff, btype='low', analog=False)

    # Apply the filter to the audio
    filtered_audio = signal.filtfilt(b, a, stretched_audio)

    # Get the output file path in the new directory
    output_file_path = os.path.join(output_directory, audio_file_name.replace('.wav', '_alien.wav'))

    # Save the processed audio as a WAV file in the new directory
    sf.write(output_file_path, filtered_audio, sr)
