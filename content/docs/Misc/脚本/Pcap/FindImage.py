import pyshark

cap = pyshark.FileCapture('lx100.pcap')

count = 0  

for packet in cap:
    if "UDP" in packet and int(packet['udp'].srcport) == 65415:
        count = count + 1
        udp_bytes = bytearray.fromhex(packet.data.data[packet.data.data.find('ffd8ffdb'):])
        file_out = open('out_files/' + str(count) + '_packet.jpg', 'wb')
        file_out.write(udp_bytes)