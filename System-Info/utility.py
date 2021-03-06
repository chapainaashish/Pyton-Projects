# System Utilize which shows system information in GUI
from tkinter import Tk, Label
from tkinter.constants import LEFT
import psutil


# Customizing root window
root = Tk()
root.geometry("588x493")
root.configure(background="black")
root.title("System Viewer")

# Adding header
root_text = Label(root, text="System Info Viewer", background="black",
                  fg="white", font=("Ubuntu", 20, "bold"))
root_text.pack(anchor="s")

# Initializing Label
sys_info = Label(root, anchor="w", background="black",
                 foreground="white", justify=LEFT, font=("Ubuntu", 10,))
sys_info.pack(anchor="w")


def fetchinfo():
    # getting info of system
    # Getting CPU usage as percentage
    # time interval should be passed to calculate cpu utilization over period of time
    cpu_percentage = psutil.cpu_percent(interval=1)

    # To get processors count
    total_cpu = psutil.cpu_count()

    # Getting CPU Frequency
    cpu_frequency = psutil.cpu_freq()

    # Getting Memory usage
    memory = psutil.virtual_memory()

    # Getting swap memory
    swap = psutil.swap_memory()

    # Getting disk usage
    # As a argument we should pass a directory
    # In case of here we are passing root directory as argument
    disk = psutil.disk_usage("/")

    # # Getting process_name
    # process_name = psutil.Process()
    # print(process_name)

    whole_data = f"""
    CPU Usage\t\t\t\t{cpu_percentage} %
    Total Processors\t\t\t{total_cpu}
    Current CPU Frequency\t\t\t{cpu_frequency[0]}
    Minimum CPU Frequency\t\t\t{cpu_frequency[1]}
    Maximum CPU Frequency\t\t{cpu_frequency[2]}

    Memory Usage\t\t\t\t{memory[2]} %
    Total Memory\t\t\t\t{(memory[0]//1024)//1024} MiB
    Used Memory\t\t\t\t{(memory[3]//1024)//1024} MiB
    Available Memory\t\t\t{(memory[1]//1024)//1024} MiB
    Cached Memory\t\t\t\t{(memory[8]//1024)//1024} MiB

    Swap Usage\t\t\t\t{swap[3]} %
    Total Swap Memory\t\t\t{(swap[0]//1024)//1024} MiB
    Used Swap Memory\t\t\t{(swap[1]//1024)//1024} MiB
    Available Swap Memory\t\t\t{(swap[2]//1024)//1024} MiB

    Disk Usage\t\t\t\t{disk[3]} %
    Total Disk\t\t\t\t{((disk[0]//1024)//1024)//1024} GiB
    Used Disk\t\t\t\t{((disk[1]//1024)//1024)//1024} GiB
    Available Disk\t\t\t\t{((disk[2]//1024)//1024)//1024} GiB
    """
    return whole_data


def update_info():
    data = fetchinfo()
    sys_info.config(text=data,)
    sys_info.after(1, update_info)
    sys_info.update()


update_info()
root.mainloop()