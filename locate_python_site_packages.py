# 
import site

site_packages =site.getsitepackages()
for path in site_packages:
    print("Site packages directory:",path)