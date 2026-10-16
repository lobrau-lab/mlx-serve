import sys

with open("app/Sources/MLXServe/Services/ChatStore.swift", "r") as f:
    content = f.read()

import re

# We want our HEAD version which fixes the unterminated string literal bug.
content = re.sub(r'<<<<<<< HEAD\n(.*?)\n=======\n.*?\n>>>>>>> origin/main', r'\1', content, flags=re.DOTALL)

with open("app/Sources/MLXServe/Services/ChatStore.swift", "w") as f:
    f.write(content)
print("Fixed Swift")
