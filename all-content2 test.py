from datetime import datetime
start = datetime.now()

content = ""
for _ in range(20):
    with open(r'C:\Users\User\School-Work\shit\MegaPak - Official 10.orcbrew', 'r', encoding="UTF-8") as file:
        content += file.read()
print(f"opened {datetime.now() - start}")

start = datetime.now()
content = content.split()
print(f"split {datetime.now() - start} {len(content)} items")

start = datetime.now()
content.sort()
print(f"sorted {datetime.now() - start}")

start = datetime.now()
with open(r'C:\Users\User\School-Work\shit\MegaPak - Official 11.orcbrew', 'w+', encoding="UTF-8") as file:
    file.writelines(content)
print(f"writen {datetime.now() - start}")

