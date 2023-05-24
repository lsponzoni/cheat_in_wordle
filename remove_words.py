import sys
import subprocess
fname = sys.argv[1]

#to_remove_words = list(input("Words"))
to_remove_words = ['anana', 'tanan', 'hanch', 'alant', 'antra', 'ranal', 'tacan', 'hanna', 'annat', 'canch', 'ratan', 'tanna', 'allan', 'antal', 'thana', 'antar', 'ancha', 'catan', 'thatn', 'cacan']

for word in to_remove_words:
    cmd =f"sed -i '/^{word}$/d' {fname}" 
    print(cmd)
    subprocess.call(cmd, shell = True)
