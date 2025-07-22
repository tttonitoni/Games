logo = r"""
     _  _       ___                  _                _   
    | || |     / _ \  ___ __      __(_) _ __   _ __  | |_ 
    | || |_   / /_\/ / _ \\ \ /\ / /| || '_ \ | '_ \ | __|
    |__   _| / /_\\ |  __/ \ V  V / | || | | || | | || |_ 
       |_|   \____/  \___|  \_/\_/  |_||_| |_||_| |_| \__|                                                    
"""

# ANSI color codes for a gradient effect
colors = [
    "\033[91m",  # Red
    "\033[93m",  # Yellow
    "\033[92m",  # Green
    "\033[96m",  # Cyan
    "\033[94m",  # Blue
    "\033[95m",  # Magenta
]

# Split the logo into lines
logo_lines = logo.splitlines()

# Print each line in a different color
for i, line in enumerate(logo_lines):
    if line.strip():  # Skip empty lines
        color = colors[i % len(colors)]
        print(f"{color}{line}\033[0m")  # Reset color after each line
    else:
        print(line)