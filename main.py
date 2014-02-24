import subprocess
proc = subprocess.Popen(['sudo','./a.out'],stdout=subprocess.PIPE)
#works in python 3.0+
#for line in proc.stdout:
try:
	for line in iter(proc.stdout.readline,''):
		result = line.rsplit()
		#print result[0] # MAC
		addr = result[0]
		rssi = result[2]
		
		if addr == "E2:59:F2:BC:E3:80":
			print rssi
except KeyboardInterrupt:
	proc.terminate()