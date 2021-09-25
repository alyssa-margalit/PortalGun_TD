import socket  # Import socket module
import os
import re
    
s = socket.socket()
port = 8000
    
s.connect(('localhost', port))
x = 0
    
st = str(x)
byt = st.encode()
s.send(byt)
    
   # send message for hundred times
while x<100:
    st = str(x)
    byt = st.encode()
    s.send(byt)
    
    print(x)
    
    while True:
        data = s.recv(1024)
        if data:
            print(data)
            x += 1
            break
    
        else:
            print('no data received')
    
    
    
print('closing')
s.close()
    