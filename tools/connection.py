#to check if system is connected or not

def is_connected():
    import socket

    try:
        socket.create_connection(('8.8.8.8', 53), timeout=3)
        return True
    
    except OSError:
        return False    