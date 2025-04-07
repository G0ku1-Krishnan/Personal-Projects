import os
import tarfile
import time
import shutil
import subprocess
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

# Set your directory to monitor
WATCH_DIRECTORY = "C:/Users/gokvenug/Desktop/logan/apk"
WAIT_TIME = 5  # Time (seconds) to check file size stability

class TgzFileHandler(FileSystemEventHandler):
    def on_created(self, event):
        """Triggered when a new .tgz file is created in the directory."""
        if event.is_directory:
            return
        
        filepath = event.src_path
        if filepath.lower().endswith(".tgz"):
            print(f"New .tgz file detected: {filepath}")
            self.wait_for_download(filepath)
            self.extract_tgz(filepath)

    def wait_for_download(self, filepath):
        """Waits until the .tgz file is fully downloaded by checking its size stability."""
        print(f"Waiting for {filepath} to finish downloading...")
        while True:
            try:
                current_size = os.path.getsize(filepath)
                #print(filepath)
                print("Current File Size (in KB): ", current_size)
                if current_size > 0:  # File size hasn't changed
                    print(f"File Download is complete. {filepath}")
                    break
                time.sleep(WAIT_TIME)  # Wait before checking again
            except FileNotFoundError:
                print(f"File {filepath} not found. It may have been removed.")
                return  # Exit if file disappears

    def extract_tgz(self, filepath):
        """Extracts the .tgz file in the same directory once it is fully downloaded."""
        extract_dir = os.path.splitext(filepath)[0]  # Remove .tgz extension
        print("Extracting build file to the location: ", WATCH_DIRECTORY)
        try:
            #if os.path.exists(extract_dir):
             #   shutil.rmtree(extract_dir)  # Remove existing folder
            #os.makedirs(extract_dir, exist_ok=True)  # Ensure we have write permissions
            
            # Extract the tgz file
            with tarfile.open(filepath, "r:gz") as tar:
                tar.extractall(path=WATCH_DIRECTORY, numeric_owner=True)
            print(f"Extracted: {filepath} to {WATCH_DIRECTORY}")

            # Execute flashimage.py if it exists
            #folderName = os.path.basename(os.getcwd())
            #print(folderName)
            flashimage_path = os.path.join(extract_dir, "flashimage.py")
            print("flashimage_path: ", flashimage_path)
            if os.path.exists(flashimage_path):
                print(f"Executing {flashimage_path}...")
                self.run_flashimage(flashimage_path, extract_dir)
            else:
                print(f"flashimage.py not found in {extract_dir}")
                
        except PermissionError:
            print(f"Error: Permission denied when extracting {filepath}. Try running with admin rights.")
        except Exception as e:
            print(f"Extraction error: {e}")

    def run_flashimage(self, script_path, extract_dir):
        """Runs the flashimage.py script."""
        try:
            # Assuming you want to run with the same Python interpreter as this script
            #folderName = os.path.basename(os.getcwd())
            #print(folderName)
            #os.system("cd {folderName}")
            #os.system("cd {folderName}")
            #print("cwd: ", os.getcwd())
            img_path = os.path.join(extract_dir, "image_files")
            print("ImagePath: ", img_path)
            os.chdir(img_path)
            print("Current Path: ", os.getcwd())
            subprocess.run(["python", script_path], check=True)
            print(f"Successfully executed {script_path}")
        except subprocess.CalledProcessError as e:
            print(f"Error executing {script_path}: {e}")
        except Exception as e:
            print(f"Unexpected error running the script: {e}")

if __name__ == "__main__":
    event_handler = TgzFileHandler()
    observer = Observer()
    observer.schedule(event_handler, WATCH_DIRECTORY, recursive=False)
    print(f"Monitoring {WATCH_DIRECTORY} for .tgz files...")
    observer.start()
    try:
        while True:
            time.sleep(5)  # Keeps the script running
    except KeyboardInterrupt:
        observer.stop()
        print("Stopping script...")

    observer.join()
