import audio
from scipy.io import wavfile


sample_rate = 16000
nfft = 256
fbank = 40
mean_norm = True
wav_file="audio.demo.wav"

fbank_mat = audio.filter_bank(sample_rate, nfft, fbank)
sample_rate, signal = wavfile.read(wav_file)

feats = audio.extract_fbank(signal, fbank_mat, sample_rate=sample_rate)

if mean_norm:
    feats = feats - feats.mean(axis=0, keepdims=True)

