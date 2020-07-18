# run sound take and after it process and sent result message to manager
import numpy as np
import matplotlib.pyplot as plt
import wave
import numpy
import pylab

def mic_main(fname):
    # Read file to get buffer                                                                                                  
    ifile = wave.open(fname)
    samples = ifile.getnframes()
    Fs = ifile.getframerate()
    audio = ifile.readframes(samples)

    # Convert buffer to float32 using NumPy                                                                                 
    audio_as_np_int16 = numpy.frombuffer(audio, dtype=numpy.int16)
    audio_as_np_float32 = audio_as_np_int16.astype(numpy.float32)

    # Normalise float32 array so that values are between -1.0 and +1.0                                                      
    max_int16 = 2**15
    audio_normalised = audio_as_np_float32 / max_int16

    thrh = fft_block(audio_normalised, Fs, True, True, fname.split('.wav')[0]+'_FFT.png')
    graph_spectrogram(fname)
    return thrh*10000

def get_wav_info(wav_file):
    wav = wave.open(wav_file, 'r')
    frames = wav.readframes(-1)
    sound_info = pylab.fromstring(frames, 'Int16')
    frame_rate = wav.getframerate()
    wav.close()
    return sound_info, frame_rate

def graph_spectrogram(wav_file):
    sound_info, frame_rate = get_wav_info(wav_file)
    pylab.figure(num=None, figsize=(19, 12))
    pylab.subplot(111)
    pylab.title('spectrogram of %r' % wav_file)
    pylab.specgram(sound_info, Fs=frame_rate)
    pylab.savefig(wav_file.split('.wav')[0]+'_spectrogram.png')


def fft_block(Xdata, Fs, isplot, issave, fname='data/AxisX_pass.png'):
    
    Ts = 1.0/Fs # sampling interval
    t = np.arange(0,len(Xdata)/Fs,Ts) # time vector
    y = Xdata - np.mean(Xdata)
    n = len(y) # length of the signal
    k = np.arange(n)
    T = n/Fs
    frq = k/T # two sides frequency range    
    frq = frq[range(int(n/2))] # one side frequency range
    Y = np.fft.fft(y)/n # fft computing and normalization
    Y = Y[range(int(n/2))]    
    
    percen_thr=0.09 # 9% of max energy holds
    thrh= np.mean(np.sort(abs(Y))[-int(len(Y)*percen_thr):-1])
    if isplot:
        fig, ax = plt.subplots(2, 1)
        ax[0].plot(t,y)
        ax[0].set_xlabel('Time')
        ax[0].set_ylabel('Amplitude')
        ax[1].plot(frq,abs(Y),'b',frq,thrh+abs(Y)*0,'r') # plotting the spectrum
        ax[1].vlines([70, 190 ], 0, np.max(abs(Y)),  colors='r')
        ax[1].vlines([ 370, 505 ], 0, np.max(abs(Y)),  colors='g')
        ax[1].vlines([ 730, 850 ], 0, np.max(abs(Y)),  colors='y')
        # ax[1].vlines([ 565, 630 ], 0, np.max(abs(Y)),  colors='g')
        ax[1].set_xlim(0,1200)
        ax[1].set_xlabel('Freq (Hz)')
        ax[1].set_ylabel('|Y(freq)|')
        ax[0].grid(True)
        ax[1].grid(True)
        if issave:
            plt.savefig(fname)
        else:            
            plt.show()
    return thrh    

if __name__ == "__main__":
    fname = 'data/cry/test_01.wav' 
    print(mic_main(fname))