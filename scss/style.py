import sass
import os
import time
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

# Specify the directories for SCSS and CSS files
scss_directory_path = r'C:/Users/Nveen Balasooriya/Desktop/new/scss'  
css_directory_path = r'C:/Users/Nveen Balasooriya/Desktop/new/scss/style'   

scss_file_name = 'black-dashboard.scss'  # SCSS file name
css_file_name = 'style.css'    # CSS output file name

# Construct the full paths for SCSS and CSS files
scss_file_path = os.path.join(scss_directory_path, scss_file_name)
css_file_path = os.path.join(css_directory_path, css_file_name)

# Check if the SCSS file exists
if not os.path.isfile(scss_file_path):
    raise FileNotFoundError(f"The specified SCSS file '{scss_file_path}' was not found.")

class SCSSWatchHandler(FileSystemEventHandler):
    def on_modified(self, event):
        # Check if the modified file is the SCSS file
        if event.src_path == scss_file_path:
            self.compile_scss()

    def compile_scss(self):
        try:
            # Read the SCSS file content
            with open(scss_file_path, 'r') as scss_file:
                scss_content = scss_file.read()

            # Compile SCSS to CSS
            css_content = sass.compile(string=scss_content)

            # Save the compiled CSS to the output directory
            with open(css_file_path, 'w') as css_file:
                css_file.write(css_content)

            print(f"Successfully compiled '{scss_file_path}' to '{css_file_path}'.")

        except sass.CompileError as e:
            print("SCSS compilation error:", e)
        except Exception as e:
            print("An error occurred:", e)

# Set up the observer to watch the SCSS directory
observer = Observer()
observer.schedule(SCSSWatchHandler(), path=scss_directory_path, recursive=False)
observer.start()

print(f"Watching for changes in '{scss_file_path}'...")

try:
    while True:
        time.sleep(1)  # Keep the script running
except KeyboardInterrupt:
    observer.stop()
observer.join()
