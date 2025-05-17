import numpy as np
import matplotlib.pyplot as plt

# Frequency range: 4 GHz to 7 GHz
frequencies = np.linspace(4e9, 7e9, 500)
Z0 = 50  # System reference impedance (Ohms)

# Simulated antenna impedance at Port 1 and Port 2
def Z_antenna_port1(f):
    return Z1* np.sin(2 * np.pi * (f - 4e9) / 3e9)

def Z_antenna_port2(f):
    return Z2 * np.cos(2 * np.pi * (f - 4e9) / 3e9)

# Reflection coefficient formula
def reflection_coeff(Z):
    return (Z - Z0) / (Z + Z0)

# Transmission coefficient (S12) - synthetic model (can be replaced with actual data)
def transmission_coeff(f):
    return 0.1 * np.exp(-1j * 2 * np.pi * f / 1e10)  # e.g., low coupling

# Compute S-parameters
Z1 = Z_antenna_port1(frequencies)
Z2 = Z_antenna_port2(frequencies)
S11 = reflection_coeff(Z1)
S22 = reflection_coeff(Z2)
S12 = transmission_coeff(frequencies)

# Convert to dB
S11_dB = 20 * np.log10(np.abs(S11))
S22_dB = 20 * np.log10(np.abs(S22))
S12_dB = 20 * np.log10(np.abs(S12))

# Plotting
plt.figure(figsize=(10, 6))
plt.plot(frequencies / 1e9, S11_dB, label='|S11| (dB)')
plt.plot(frequencies / 1e9, S22_dB, label='|S22| (dB)', linestyle='--')
plt.plot(frequencies / 1e9, S12_dB, label='|S12| (dB)', linestyle=':')
plt.xlabel('Frequency (GHz)')
plt.ylabel('Magnitude (dB)')
plt.title('S-parameters vs Frequency (4 GHz - 7 GHz)')
plt.grid(True)
plt.legend()
plt.tight_layout()
plt.show()