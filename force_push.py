import subprocess
import os

try:
    subprocess.run(["git", "push", "origin", "jules-5585600079070434279-b5580ce5", "--force"], check=True)
    print("Force push successful")
except subprocess.CalledProcessError as e:
    print(f"Force push failed: {e}")
