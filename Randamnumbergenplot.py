import matplotlib.pyplot as plt
import numpy as np


x = np.random.normal(500,100, 1000)
mean = np.mean(x)
std_dev = np.std(x)

print(f"Mean: {mean}")
print(f"Standard Deviation: {std_dev}")


plt.plot(x, linestyle='solid', color='red')
plt.grid()
plt.title('Series of Random Numbers')
plt.xlabel('Index')
plt.ylabel('Value')
plt.savefig('plot_line.png', format='png')
plt.show()


bins = range(0, 1010, 10)
plt.hist(x, bins=bins, color='green')
plt.xticks(range(0, 1010, 10))
plt.grid()
plt.title('Histogram of Random Numbers')
plt.xlabel('Value')
plt.ylabel('Frequency')
plt.savefig('plot_histogram.png', format='png')
plt.show()

fft = np.fft.fft(x)
frequency = np.fft.fftfreq(len(x))

plt.plot(frequency[:len(frequency)//2], np.abs(fft)[:len(fft)//2], color='blue')
plt.grid()
plt.title('FFT of Random Numbers')
plt.xlabel('Frequency')
plt.ylabel('Amplitude')
plt.savefig('plot_fft.png', format='png')
plt.show()