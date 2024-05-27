import winreg
import os


def add_dll_path_to_path(dll_path):
    # Открываем ключ реестра, содержащий переменные среды
    key = winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE, r"SYSTEM\CurrentControlSet\Control\Session Manager\Environment", 0,
                         winreg.KEY_ALL_ACCESS)

    # Получаем текущее значение переменной PATH
    path_value, _ = winreg.QueryValueEx(key, "Path")

    # Добавляем путь к папке с DLL-файлами, если его еще нет
    if dll_path not in path_value:
        path_value += ";" + dll_path

        # Обновляем значение переменной PATH в реестре
        winreg.SetValueEx(key, "Path", 0, winreg.REG_EXPAND_SZ, path_value)

        # Закрываем ключ реестра
        winreg.CloseKey(key)

        print(f"Added {dll_path} to PATH for all users.")
    else:
        print(f"{dll_path} is already in PATH.")


if __name__ == "__main__":
    # Путь к папке с вашими DLL-файлами
    dll_path = r"D:\repo\pyllt\lib\freeglut-3.4.0\bin\Release"

    # Вызываем функцию для добавления пути к папке с DLL-файлами в переменную PATH
    add_dll_path_to_path(dll_path)
