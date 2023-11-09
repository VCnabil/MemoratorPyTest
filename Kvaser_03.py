import time
from canlib import canlib, Frame

def send_frames():
    with canlib.openChannel(0) as ch:  # Replace 0 with your actual channel number
        ch.busOn()
        
        for i in range(10):
            frame_id = 0x18FFAA00
            data_bytes = [i, 0, 0, 0, ord('a'), ord('b'), ord('c'), ord('d')]
            
            frame = Frame(id_=frame_id, data=data_bytes, flags=canlib.MessageFlag.EXT)
            ch.write(frame)
            
            print(f"Sent frame {i+1}: ID={frame_id}, Data={data_bytes}")
            
            time.sleep(0.2)  # 200 ms interval between messages

        ch.busOff()

if __name__ == "__main__":
    send_frames()