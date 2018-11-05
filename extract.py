import os, zipfile

rootdir = r'C:\EPNWA1'
destdir = r'C:\xml'

for subdir in os.listdir(rootdir):
 z = zipfile.ZipFile(rootdir+'\\'+subdir)
 f = subdir.replace('.zip','.xml')
 z.extract(f, path=destdir)
