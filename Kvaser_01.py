#Kvaser_02.py:
from canlib import canlib, Frame

data_array = [22, 17, 14, 0x22, 0x17, 0x14]
data_bad = [72, 69, 76, 76, 79, 33]

def check_overrun_status(ch):
    status = ch.readStatus()
    
    # Assuming that HW_OVERRUN and SW_OVERRUN are the flags for hardware and software overruns
    if status & canlib.Stat.HW_OVERRUN:
        print("Hardware buffer overrun detected.")
        
    if status & canlib.Stat.SW_OVERRUN:
        print("Software buffer overrun detected.")

def runWriteCanPythonicCh1(can_id):
    with canlib.openChannel(0) as ch_a:
        ch_a.busOn()
        
        # Check for overrun before writing
        check_overrun_status(ch_a)
        
        frame = Frame(can_id, data=data_array, flags=canlib.MessageFlag.EXT)
        ch_a.write(frame)
        
        # Check for overrun after writing
        check_overrun_status(ch_a)
        
        msg = ch_a.read(timeout=500)
        print(msg)
        
def testfunc(): 
    print("should this print?")   
    runWriteCanPythonicCh1(0x18FFFA11)

if __name__ == "__main__":
    testfunc()
