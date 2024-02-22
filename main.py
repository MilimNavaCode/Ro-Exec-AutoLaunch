import os
import subprocess
import time
import psutil
from tqdm import tqdm

directory_cocaine = r'KRAMPUS DIRECTORY HERE'
os.chdir(directory_cocaine)

def find_exe_files(directory):
    """WARNING! Find all .exe files in the specified directory. dont add this to your Desktop please"""
    return [f for f in os.listdir(directory) if f.endswith('.exe') and f.lower() != 'robloxplayerbeta.exe']

def is_process_running(process_name):
    """Check if there is any running process that contains the given name."""
    for proc in psutil.process_iter(['name']):
        try:
            if process_name.lower() in proc.info['name'].lower():
                return True
        except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
            pass
    return False

def execute_exes(exe_files, directory):
    """Execute all .exe files in the provided list but start them minimized."""
    for exe in exe_files:
        try:
            subprocess.Popen(f'start /min {os.path.join(directory, exe)}', shell=True, cwd=directory)
            print(f"Launched: {exe}")
            print("Injecting... please wait 26 seconds. Please visit https://loader.live/dashboard/ro-exec for the Executor")
            
            for i in tqdm(range(26), desc="Injecting"):
                time.sleep(1)
            
            print("Successfully Injected!")
        except Exception as e:
            print(f"Failed to launch {exe}: {e}")


def monitor_and_execute(directory):
    roblox_running = False
    roblox_was_opened = False
    initial_prompt = True
    message_printed = False

    while True:
        exe_files = find_exe_files(directory)
        if is_process_running('RobloxPlayerBeta.exe'):
            if not roblox_running:
                if initial_prompt:
                    print("RobloxPlayerBeta.exe is running. Launching other EXE files...")
                    initial_prompt = False
                roblox_running = True
                roblox_was_opened = True
                message_printed = False
                execute_exes(exe_files, directory)
        else:
            if roblox_running:
                roblox_running = False
                if not message_printed and roblox_was_opened:
                    print("Please open Roblox again")
                    message_printed = True
            elif initial_prompt:
                print("Please open Roblox")
                initial_prompt = False
        time.sleep(5)


if __name__ == "__main__":
    directory = os.getcwd()
    monitor_and_execute(directory)
