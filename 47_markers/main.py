import os
import sys
import platform


print(f'os_name: {os.name}')
print(f'sys_platform: {sys.platform}')
print(f'platform_release: {platform.release()}')
print(f'implementation_name: {sys.implementation.name}')
print(f'platform_machine: {platform.machine()}')
print(f'platform_python_implementation: {platform.python_implementation()}')
      