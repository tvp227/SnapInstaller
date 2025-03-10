# Kudu Snap Installer

A simple GUI application to streamline the installation of Snap packages on Linux systems.

![image](https://github.com/user-attachments/assets/3934f94a-c6d8-4107-915a-f62ea7d30ac3)

## Overview

Kudu Snap Installer provides a user-friendly graphical interface for installing Snap packages on Linux. It categorizes common applications and utilities, allowing users to select packages for installation with simple checkboxes. The tool also offers a custom package option for installing packages not included in the predefined categories.

## Features

- **Categorized Package Selection**: Browse and select packages from predefined categories:
  - Productivity (Chromium, Firefox, VS Code, Slack)
  - Development (Go, Node.js, Docker, Postman)
  - Utilities (VLC, Spotify, OBS Studio, htop)
  - System (Canonical Livepatch, Bashtop, Snap Store)

- **Custom Package Installation**: Add any Snap package not listed in the categories

- **Command Preview**: View the complete installation command before execution

- **One-Click Installation**: Install all selected packages with a single button click

- **Clean Interface**: Simple, intuitive user interface that requires no technical knowledge

## Prerequisites

- A Linux distribution with Snap support
- Python 3.x
- Tkinter library
- Administrative (sudo) privileges for package installation

## Installation

1. Clone the repository:
   ```
   git clone https://github.com/tvp227/kudu-snap-installer.git
   ```

2. Navigate to the project directory:
   ```
   cd kudu-snap-installer
   ```

3. Run the application:
   ```
   python3 snap_installer.py
   ```

## Usage

### Installing Predefined Packages

1. Launch the application
2. Navigate through the category tabs (Productivity, Development, Utilities, System)
3. Check the boxes next to the packages you want to install
4. Review the generated command in the text area at the bottom
5. Click "Install Now" to execute the installation

### Installing Custom Packages

1. Go to the "Custom" tab
2. Enter the name of the Snap package in the text field
3. Click "Add" to add it to the installation list
4. Repeat for any additional custom packages
5. Click "Install Now" to execute the installation

### Managing Selections

- Use the "Clear All" button to reset all selections
- On the Custom tab, select a package and click "Remove" to remove it from the list

## Extending Package Lists

You can easily extend the predefined package lists by modifying the `snap_packages` dictionary in the code:

```python
self.snap_packages = {
    "Productivity": ["chromium", "firefox", "code --Classic", "slack"],
    "Development": ["go", "node", "docker", "postman"],
    "Utilities": ["vlc", "spotify", "obs-studio", "htop"],
    "System": ["canonical-livepatch", "bashtop", "snap-store"]
}
```

To find additional Snap packages for a specific category, use the following command in your terminal:
```
snap find <category>
```

## Notes

- When installing packages that require the `--classic` flag (like VS Code), make sure to include it in the package name as shown in the predefined lists
- The application uses `sudo` to install packages, so you may be prompted for your password during installation
- Check the output area for any error messages if installation fails

## Troubleshooting

- **"Command executed successfully" but packages not installed**: Ensure Snap is properly installed on your system
- **Package not found**: Verify the package name exists in the Snap store



## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Author

- **TVP227** - [GitHub Profile](https://github.com/tvp227)
- **Linkdln** - [Thomas Porter](www.linkedin.com/in/thomasvporter)

## Acknowledgments

- The Snap package system and its developers
- The Python and Tkinter communities

- Biggest aknowledgement goes to https://packagepicker.co/pm/apt. A great peice of software that achives a very similar principle for additional packages. Plus they are web hosted.
