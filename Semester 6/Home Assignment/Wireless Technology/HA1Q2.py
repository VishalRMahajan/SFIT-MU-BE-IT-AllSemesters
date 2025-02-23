import math

def erlang_B(traffic, m):
    B = 1.0
    for i in range(1, m + 1):
        B = (traffic * B) / (i + traffic * B)
    return B

def find_offered_traffic(m, target_B, tol=1e-6, max_iter=1000):
    low = 0.0
    high = m * 2.0
    while erlang_B(high, m) < target_B:
        high *= 2.0

    iter_count = 0
    while (high - low) > tol and iter_count < max_iter:
        mid = (low + high) / 2.0
        B_mid = erlang_B(mid, m)
        if B_mid < target_B:
            low = mid  
        else:
            high = mid
        iter_count += 1

    return (low + high) / 2

def calc_S_over_I(N, gamma=4):
    ratio_linear = ((math.sqrt(3 * N)) ** gamma) / 6.0
    ratio_dB = 10 * math.log10(ratio_linear)
    return ratio_linear, ratio_dB

def main():
    total_channels = 395            
    call_duration_sec = 120         
    call_duration_hr = call_duration_sec / 3600.0  
    blocking_probability = 0.02     
    reuse_factors = [4, 7, 12]      

    print("Cellular System Analysis \n")

    for N in reuse_factors:
        print(f"\nFor Reuse Factor N = {N}:")
        
        channels_per_cell = total_channels // N
        print(f" - Channels per cell: {channels_per_cell}")

        offered_traffic = find_offered_traffic(channels_per_cell, blocking_probability)
        carried_traffic = offered_traffic * (1 - blocking_probability)  # Carried traffic
        
        call_capacity_per_cell = carried_traffic / call_duration_hr
        print(f" - Offered Traffic: {offered_traffic:.2f} Erlangs")
        print(f" - Carried Traffic: {carried_traffic:.2f} Erlangs")
        print(f" - Call Capacity per Cell: {call_capacity_per_cell:.2f} calls/hour")

        S_I_linear, S_I_dB = calc_S_over_I(N)
        print(f" - Mean S/I Ratio: {S_I_linear:.2f} (linear)")
        print(f" - Mean S/I Ratio: {S_I_dB:.2f} dB")

if __name__ == "__main__":
    main()
