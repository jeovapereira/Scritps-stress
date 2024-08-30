import os
import shutil

def limpar_cache(caminho):
    if os.path.exists(caminho):
        try:
            shutil.rmtree(caminho)
            print(f"{caminho} limpo com sucesso!")
        except Exception as e:
            print(f"Erro ao limpar {caminho}: {e}")
    else:
        print(f"{caminho} não encontrado.")

# Caminho para as pastas do FiveM e GTA V (substitua pelos caminhos corretos)
fivem_dir = os.path.join(os.getenv('LOCALAPPDATA'), 'FiveM', 'FiveM.app', 'data')
gtav_dir = r'A:\SteamLibrary\steamapps\common\Grand Theft Auto V'

# Limpando o cache do FiveM
print("Limpando cache do FiveM...")
limpar_cache(os.path.join(fivem_dir, 'cache'))
limpar_cache(os.path.join(fivem_dir, 'server-cache'))
limpar_cache(os.path.join(fivem_dir, 'server-cache-priv'))
limpar_cache(os.path.join(fivem_dir, 'caches.xml'))

# Limpando o cache injetado no GTA V (modifique os caminhos conforme necessário)
print("Limpando cache injetado no GTA V...")
limpar_cache(os.path.join(gtav_dir, 'mods'))
limpar_cache(os.path.join(gtav_dir, 'scripts'))
limpar_cache(os.path.join(gtav_dir, 'cache'))
limpar_cache(os.path.join(gtav_dir, 'caches.xml'))

print("Processo de limpeza concluído!")