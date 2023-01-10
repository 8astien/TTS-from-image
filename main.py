import torch
import torchaudio
from easyocr import Reader
import matplotlib.pyplot as plt


device = 'cpu'
reader = Reader(['en'])
symbols = '_-!\'(),.:;? abcdefghijklmnopqrstuvwxyz'
look_up = {s: i for i, s in enumerate(symbols)}
symbols = set(symbols)
bundle = torchaudio.pipelines.TACOTRON2_WAVERNN_PHONE_LJSPEECH
processor = bundle.get_text_processor()
tacotron = bundle.get_tacotron2().to(device)
vocoder = bundle.get_vocoder().to(device)

file = input('URL / LOCAL PATH: ')
results = reader.readtext(file)

extract = []
for r in results:
    extract.append(r[1])

print(extract)

txt = str(extract)

def text_sequence(text):
    text = text.lower()
    return [look_up[s] for s in text if s in symbols]

print(text_sequence("String sequence : " + txt))


# TTS
# GENERATE SPECTOGRAM FROM TEXT SEQUENCE

with torch.inference_mode():
    processed, lengths = processor(txt)
    processed = processed.to(device)
    lengths = lengths.to(device)
    spec, spec_lengths, _ = tacotron.infer(processed, lengths)
    waveforms, lengths = vocoder(spec, spec_lengths)

plt.imshow(spec[0].cpu().detach())
plt.show()

# SAVE TTS AUDIO FILE

torchaudio.save("tts.wav", waveforms[0:1].cpu(), sample_rate=vocoder.sample_rate)



