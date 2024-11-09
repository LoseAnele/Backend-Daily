# Mail Merge Project

This project is designed to automate the process of creating personalized letters for a list of invited guests. It reads a list of names from a text file, merges each name into a template letter, and saves the resulting letters in a new directory.

**How to Use**

1. Ensure the project directory structure is as follows:
   - `mail merge`
     - `input`
       - `Names`
         - `invited_names.txt` (list of names, one per line)
       - `letters`
         - `starting_letter.docx` (template letter with [name] placeholder)
     - `ReadyToSend` (directory where the generated letters will be saved)
2. Run the `main.py` script to generate the letters.
3. The script will create a new letter for each name in `invited_names.txt`, replacing the [name] placeholder with the actual name, and save it in the `ReadyToSend` directory.

**Error Handling**

The script includes error handling for common issues such as file not found errors and OS errors. If an error occurs, it will print an error message indicating the problem and the file or directory affected.

**Dependencies**

This project requires the `os` module, which is part of the Python standard library. No additional dependencies need to be installed.

**Notes**

- The script assumes the project directory structure is as described above. If the directory structure is different, the script will need to be modified accordingly.
- The script does not modify the original template letter or the list of names. It only generates new letters based on the template and saves them in a new directory.
- The script does not handle cases where the same name appears multiple times in the list of invited names. Each name will result in a unique letter being generated.
