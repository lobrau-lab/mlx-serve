import re

with open(".github/workflows/release.yml", "r") as f:
    content = f.read()

replacement = """      - name: Import signing certificate
        if: ${{ secrets.APPLE_CERTIFICATE_BASE64 != '' }}
        env:
          APPLE_CERTIFICATE_BASE64: ${{ secrets.APPLE_CERTIFICATE_BASE64 }}
          APPLE_CERTIFICATE_PASSWORD: ${{ secrets.APPLE_CERTIFICATE_PASSWORD }}"""

content = content.replace("""      - name: Import signing certificate
        if: ${{ env.APPLE_CERTIFICATE_BASE64 != '' }}
        env:
          APPLE_CERTIFICATE_BASE64: ${{ secrets.APPLE_CERTIFICATE_BASE64 }}
          APPLE_CERTIFICATE_PASSWORD: ${{ secrets.APPLE_CERTIFICATE_PASSWORD }}""", replacement)

with open(".github/workflows/release.yml", "w") as f:
    f.write(content)
