#!/usr/bin/env python3
import os
import sys
from pysubs2 import SSAFile, SSAError

def convert_ass_to_srt(ass_file_path):
    try:
        # Load the .ass file
        subs = SSAFile.load(ass_file_path)
        
        # Convert to .srt format
        srt_content = subs.to_string(format="srt")
        
        # Save to .srt file with the same name
        srt_file_path = os.path.splitext(ass_file_path)[0] + ".srt"
        with open(srt_file_path, "w", encoding="utf-8") as srt_file:
            srt_file.write(srt_content)

        print(f"Converted {ass_file_path} to {srt_file_path}")

    except FileNotFoundError:
        print(f"Error: File {ass_file_path} not found.")
    except SSAError:
        print(f"Error: Invalid or corrupted .ass file: {ass_file_path}")
    except IOError as e:
        print(f"Error writing to .srt file: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    # The script expects the path to the .ass file or directory as the first argument
    if len(sys.argv) > 1:
        path = sys.argv[1]
        if os.path.isfile(path) and path.endswith('.ass'):
            convert_ass_to_srt(path)
        elif os.path.isdir(path):
            for file in os.listdir(path):
                if file.endswith('.ass'):
                    convert_ass_to_srt(os.path.join(path, file))
        else:
            print(f"Invalid path or not an .ass file: {path}")
    else:
        print("No path provided.")
