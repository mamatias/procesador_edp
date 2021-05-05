import os
import shutil

in_dir = './files_in'
out_dir = '{0}/{1}'.format(in_dir, 'procesados')

# Primero, chequear si existe el directorio de trabajo
if not os.path.isdir(in_dir):
    print('El directorio de entrada [{0}] no exsite'.format(in_dir))

# Segundo, borrar el directorio de salida
if os.path.isdir(out_dir):
    shutil.rmtree(out_dir)

# Tercero, crear el directorio de salida
os.mkdir(out_dir)

print(os.listdir())