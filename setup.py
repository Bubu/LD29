#!/usr/bin/env python3
from cx_Freeze import setup, Executable
import sys, os, stat
PROGRAM_NAME = 'game'

# Dependencies are automatically detected, but it might need
# fine tuning.
buildOptions = dict(packages = [],
                    excludes = [],
                    include_files = ["res","settings.txt"],
                    includes = [],
                    compressed = True,
                    optimize = 2)
if sys.platform == "win32":
#    buildOptions['includes'].append('OpenGL.platform.win32')
    buildOptions['include_files'] += [('C:\\Python33\\Lib\\site-packages\\pygame\\libogg.dll',''), ('C:\\Python33\\Lib\\site-packages\\pygame\\libvorbis.dll',''),('C:\\Python33\\Lib\\site-packages\\pygame\\libvorbisfile.dll','')]
#if sys.platform.startswith("linux"):
#    buildOptions['includes'].append('OpenGL.platform.glx')
#if sys.platform.startswith("darwin"):
#    buildOptions['includes'].append('OpenGL.platform.darwin')
                    
base = 'Console'

executables = [
    Executable(PROGRAM_NAME + '.py', base=base)
]

setup(name='Game of Roots',
      version = '0.1',
      description = 'Ludum Dare 29 Game by Stephan Waeldchen, Eric Zimmermann and Marcus Hoffmann',
      options = dict(build_exe = buildOptions),
      executables = executables)
      
if sys.platform == "win32":
    f = open('build\start.bat', 'w')
    print('cd "exe.win-amd64-3.3"\nstart ' + PROGRAM_NAME, file = f)
    f.close()
else:
    f = open('build/start.sh', 'w')
    print('#!/bin/sh\ncd "exe.linux-x86_64-3.3"\n./' + PROGRAM_NAME, file = f)
    f.close()
    os.chmod('build/start.sh', os.stat('build/start.sh').st_mode | stat.S_IXUSR | stat.S_IXGRP| stat.S_IXOTH)
