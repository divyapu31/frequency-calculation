import math
# Constants
c = 3e8  # Speed of light in m/s
m = 1    # Dominant mode
n = 1

def compute_frequencies(w1_eff, w2_eff, d, s, epsilon_reff):
    # Compute physical widths from effective widths
    w1 = w1_eff + (d ** 2) / (0.95 * s)
    w2 = w2_eff + (d ** 2) / (0.95 * s)

    # Equation (1): fL
    fL = c / (2 * math.sqrt(epsilon_reff)) * math.sqrt((m / w1_eff) ** 2 + (n / w1) ** 2)
    
    # Equation (2): fH
    fH = c / (2 * math.sqrt(epsilon_reff)) * math.sqrt((m / w2_eff) ** 2 + (n / w2) ** 2)

    return fL, fH

# Example usage (units in meters, epsilon_reff is unitless)
w1 = 0.03    # 30 mm
w2= 0.026    # 20 mm
d = 0.0008        # 0.8 mm
s = 1.1         # 1.1 mm
epsilon_reff = 2.2

fL, fH = compute_frequencies(w1_eff, w2_eff, d, s, epsilon_reff)

print(f"fL_110(HM) = {fL/1e9:.3f} GHz")
print(f"fH_110(HM) = {fH/1e9:.3f} GHz")