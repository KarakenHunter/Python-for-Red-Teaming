import subprocess as sp

cmd="whoami"
result=sp.run(cmd, capture_output=True, text=True)
resp=result.stdout
print(resp)