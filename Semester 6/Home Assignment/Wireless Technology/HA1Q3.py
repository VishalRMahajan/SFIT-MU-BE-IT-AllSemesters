import math

f_high = 928
f_low = 902
Bw = f_high - f_low

Rs = 0.5e6
code_symbols = 16
bit_error_rate = 1e-5
antenna_gain = 2.6
beta = 0.5
alpha = 0.9

Gp = 26 / 2

Eb_N0_dB = 10
Eb_N0 = 10 ** (Eb_N0_dB / 10)

M = (Gp / Eb_N0) * (1 / (1 + beta)) * alpha * antenna_gain

Rb = Rs * math.log2(code_symbols)

total_data_rate = M * Rb
eta = total_data_rate / (Bw * 1e6)

print(f"Bandwidth (Bw): {Bw} MHz")
print(f"Bit rate per user (Rb): {Rb / 1e6:.2f} Mbps")
print(f"Number of users supported (M): {round(M)}")
print(f"Bandwidth efficiency (η): {eta:.2f} bps/Hz")

if eta < 0.5:
    capacity_comment = "The system has a low bandwidth efficiency. Increasing the number of users or improving coding techniques could enhance the capacity."
else:
    capacity_comment = "The system has a good bandwidth efficiency and can support multiple users effectively."

print("\nSystem Capacity Analysis:")
print(capacity_comment)
