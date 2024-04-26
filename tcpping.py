import socket
import time

def tcp_ping(host, port):
    try:
        start_time = time.time()
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.connect((host, port))
        end_time = time.time()
        print(f"TCP Ping to {host}:{port} successful. Time taken: {end_time - start_time} seconds")
    except Exception as e:
        print(f"TCP Ping to {host}:{port} failed. Error: {e}")
    finally:
        sock.close()

host = '8.8.8.8'
port = 53

tcp_ping(host, port)
