import os
import shutil
import glob

def limpar_pastas():
    # Limpar a pasta temp
    temp_dirs = [os.path.join(os.sep, 'tmp'), os.path.join(os.sep, 'temp'), os.environ.get('TEMP')]
    for temp_dir in temp_dirs:
        if temp_dir:
            for file_path in glob.glob(os.path.join(temp_dir, '*')):
                try:
                    if os.path.isfile(file_path):
                        os.remove(file_path)
                    elif os.path.isdir(file_path):
                        shutil.rmtree(file_path)
                except Exception as e:
                    print(f"Erro ao limpar {file_path}: {e}")

    # Limpar a pasta %temp%
    temp_dir = os.environ.get('TEMP')
    if temp_dir:
        for file_path in glob.glob(os.path.join(temp_dir, '*')):
            try:
                if os.path.isfile(file_path):
                    os.remove(file_path)
                elif os.path.isdir(file_path):
                    shutil.rmtree(file_path)
            except Exception as e:
                print(f"Erro ao limpar {file_path}: {e}")

    # Limpar a pasta prefetch
    prefetch_dir = os.path.join(os.environ.get('SystemRoot', 'C:\\Windows'), 'Prefetch')
    for file_path in os.listdir(prefetch_dir):
        try:
            file_path = os.path.join(prefetch_dir, file_path)
            if os.path.isfile(file_path):
                os.remove(file_path)
        except Exception as e:
            print(f"Erro ao limpar {file_path}: {e}")

if __name__ == "__main__":
    limpar_pastas()
