#!/usr/bin/python3
import requests, argparse, socket

parser = argparse.ArgumentParser(description="This is a Tool")

parser.add_argument("-host", type=str, help="Enter Host", required=True)
parser.add_argument("-port", type=str, help="Enter Port", required=True)
a = parser.parse_args()

host = a.host
port = int(a.port)

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
ss = socket.socket()

def scan_port(port):
	try:
		ss.connect((host, port))
		return True
	except:
		return False
try:
	sock.connect((host, port))
	if scan_port(port):
		print("Port is Open")
		e = sock.recv(1024)
		if e is not None:
			print("Banner : ", e)
		else:
			print("Banner not Present, Change Domain")
	else:
		print("Port is Closed")
except ConnectionRefusedError as ee:
	print("Error : ", ee)

sock.close()
