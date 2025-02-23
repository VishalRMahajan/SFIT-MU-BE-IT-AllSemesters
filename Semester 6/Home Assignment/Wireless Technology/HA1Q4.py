import math

def mw_to_dbm(mw):
    return 10 * math.log10(mw)

def dbm_to_watts(dbm):
    return 10 ** ((dbm - 30) / 10)

def calculate_snr(received_dbm, noise_dbm):
    snr_db = received_dbm - noise_dbm
    snr_linear = 10 ** (snr_db / 10)
    return snr_db, snr_linear

def shannon_capacity(bandwidth_hz, snr_linear):
    return bandwidth_hz * math.log2(1 + snr_linear)

def main():
    power_mw = 100
    power_dbm = mw_to_dbm(power_mw)
    print("(a) 100 mW in dBm: {:.2f} dBm".format(power_dbm))
    
    noise_dbm = -100
    noise_watts = dbm_to_watts(noise_dbm)
    print("(b) -100 dBm in Watts: {:.2e} W".format(noise_watts))
    
    received_power_dbm = 20 - 90 
    snr_db, snr_linear = calculate_snr(received_power_dbm, noise_dbm)
    print("(c) Received power: {:.2f} dBm".format(received_power_dbm))
    print("    SNR: {:.2f} dB ({:.0f} in linear scale)".format(snr_db, snr_linear))
    
    bandwidth = 20e6 
    capacity = shannon_capacity(bandwidth, snr_linear)
    print("(d) Shannon capacity: {:.2f} Mbps".format(capacity / 1e6))
    
    new_transmit_dbm = mw_to_dbm(200)
    new_received_dbm = new_transmit_dbm - 90
    new_snr_db, new_snr_linear = calculate_snr(new_received_dbm, noise_dbm)
    new_capacity = shannon_capacity(bandwidth, new_snr_linear)
    print("(e) With 200 mW transmit power:")
    print("    New transmit power: {:.2f} dBm".format(new_transmit_dbm))
    print("    New received power: {:.2f} dBm".format(new_received_dbm))
    print("    New SNR: {:.2f} dB ({:.0f} in linear scale)".format(new_snr_db, new_snr_linear))
    print("    New Shannon capacity: {:.2f} Mbps".format(new_capacity / 1e6))

if __name__ == "__main__":
    main()
