import platform
import os
import sys

try:
    print(sys.platform())
    print(os.name())
    print(platform.platform())
    print(platform.uname())
except Exception:
    pass
