import tkinter as tk
from tkinter import ttk
import subprocess

print ("Thanks for using this Snap insaller client. Readme and instruction found at github.com/tvp227")

class KuduSnapInstaller:
    def __init__(self, root):
        self.root = root
        self.root.title("Snap Installer")
        self.root.geometry("500x400")
        
        """Note these are what fills the packages. Once Snap is installed you can run a snap-find <catagory> to pull a list of apps in that field with their alias. This can be added to the arrays below."""
        """Alternativly just use the Custom tab within the GUI"""

        # MAIN PACKAGES
        self.snap_packages = {
            "Productivity": ["chromium", "firefox", "code --Classic", "slack"],
            "Development": ["go", "node", "docker", "postman"],
            "Utilities": ["vlc", "spotify", "obs-studio", "htop"],
            "System": ["canonical-livepatch", "bashtop", "snap-store"]
        }
        
        # SETUP TABS
        self.notebook = ttk.Notebook(root)
        self.notebook.pack(fill=tk.BOTH, expand=True, padx=10, pady=5)
        
        # STORE CHECKBOXES
        self.package_vars = {}
        
        # CREATE CATEGORY TABS
        for category, packages in self.snap_packages.items():
            frame = ttk.Frame(self.notebook, padding=10)
            self.notebook.add(frame, text=category)
            
            for i, package in enumerate(packages):
                var = tk.BooleanVar()
                self.package_vars[package] = var
                
                checkbox = ttk.Checkbutton(
                    frame, 
                    text=package,
                    variable=var,
                    command=self.generate_command
                )
                checkbox.grid(row=i, column=0, sticky="w")
        
        # CUSTOM TAB
        custom_tab = ttk.Frame(self.notebook, padding=10)
        self.notebook.add(custom_tab, text="Custom")
        
        # ENTRY FIELD
        self.custom_entry = ttk.Entry(custom_tab, width=20)
        self.custom_entry.pack(side="left", padx=5)
        
        add_button = ttk.Button(custom_tab, text="Add", command=self.add_custom_package)
        add_button.pack(side="left")
        
        # CUSTOM PACKAGES LIST
        self.custom_packages = []
        self.custom_listbox = tk.Listbox(custom_tab, height=8)
        self.custom_listbox.pack(fill="x", pady=5)
        
        remove_button = ttk.Button(custom_tab, text="Remove", command=self.remove_custom_package)
        remove_button.pack(anchor="w")
        
        # COMMAND DISPLAY
        self.output_text = tk.Text(root, height=4, wrap="word")
        self.output_text.pack(fill="x", padx=10, pady=5)
        
        # BUTTONS
        button_frame = ttk.Frame(root)
        button_frame.pack(fill="x", padx=10, pady=5)
        
        install_button = ttk.Button(button_frame, text="Install Now", command=self.run_command)
        install_button.pack(side="left", padx=5)
        
        clear_button = ttk.Button(button_frame, text="Clear All", command=self.clear_all)
        clear_button.pack(side="right", padx=5)
    
    def add_custom_package(self):
        package = self.custom_entry.get().strip()
        if package and package not in self.custom_packages:
            self.custom_packages.append(package)
            self.custom_listbox.insert(tk.END, package)
            self.custom_entry.delete(0, tk.END)
            self.generate_command()
    
    def remove_custom_package(self):
        if self.custom_listbox.curselection():
            index = self.custom_listbox.curselection()[0]
            self.custom_packages.pop(index)
            self.custom_listbox.delete(index)
            self.generate_command()
    
    def clear_all(self):
        for var in self.package_vars.values():
            var.set(False)
        self.custom_listbox.delete(0, tk.END)
        self.custom_packages.clear()
        self.generate_command()
    
    def generate_command(self):
        selected_packages = []
        
        # GET SELECTED PACKAGES
        for package, var in self.package_vars.items():
            if var.get():
                selected_packages.append(package)
        
        # ADD CUSTOM PACKAGES
        selected_packages.extend(self.custom_packages)
        
        if not selected_packages:
            self.output_text.delete(1.0, tk.END)
            self.output_text.insert(tk.END, "No packages selected.")
            return
        
        # MAKE COMMAND
        command = f"sudo snap install {' '.join(selected_packages)}"
        
        self.output_text.delete(1.0, tk.END)
        self.output_text.insert(tk.END, command)
    
    def run_command(self):
        command = self.output_text.get(1.0, tk.END).strip()
        if not command or command == "No packages selected.":
            return
            
        try:
            # ATTEMPT TO RUN IN SHELL
            process = subprocess.Popen(
                command,
                shell=True, # MUST USE shell=True
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE,
                text=True
            )
            
            # OUTPUT TEXT
            stdout, stderr = process.communicate()
            
            if stderr:
                self.output_text.delete(1.0, tk.END)
                self.output_text.insert(tk.END, f"Error: {stderr}")
            else:
                self.output_text.delete(1.0, tk.END)
                self.output_text.insert(tk.END, f"Command executed successfully\n{stdout}")
                
        except Exception as e:
            self.output_text.delete(1.0, tk.END)
            self.output_text.insert(tk.END, f"ERROR: {str(e)}")

if __name__ == "__main__":
    root = tk.Tk()
    app = KuduSnapInstaller(root)
    root.mainloop()