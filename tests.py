"""
Toma como argumento el directorio donde estan los modelos
"""
from testing.shell_non_blocking import ShellProc
import os
cores = 14
procs = []
try:
    from glob import glob
    for i,f in enumerate((y for x in os.walk("testing") for y in glob(os.path.join(x[0], '*.model')))):
        if not os.path.exists(f.replace(".model",".posta")):
            print('.', end='')
            while len(procs) >= cores:
                procs = [p for p in procs if p.is_running()]
            procs.append(ShellProc('python3 main.py "%s" > "%s"' % (f,f.replace(".model",".posta"))))
            
except KeyboardInterrupt:
    pass
    
