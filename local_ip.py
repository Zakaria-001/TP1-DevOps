import socket

hostname = socket.gethostname()
ip_locale = socket.gethostbyname(hostname)
print("IP locale :", ip_locale)

