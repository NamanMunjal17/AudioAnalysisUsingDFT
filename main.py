import customtkinter as ctk
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from dft import output
from tkinter import filedialog
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk


app=ctk.CTk()

app.title("Discrete Fourier Transform On Audio Files")
app.geometry('1000x600')

tabview=ctk.CTkTabview(master=app)

tabview.add('analysis')
tabview.pack(fill="both", expand=True)
analysis=tabview.tab("analysis")
analysis.grid_columnconfigure(0,weight=1)
analysis.grid_columnconfigure(1,weight=10)
analysis.grid_columnconfigure(2,weight=1)

title1=ctk.CTkLabel(master=analysis,text="Audio Representation")
title1.grid(row=1,column=1)

def pick_file():
    file_path = filedialog.askopenfilename(
        title="Select a File",
        filetypes=(("Wave", "*.wav"), ("All Files", "*.*"))  # Filters for file types
    )
    if file_path:  # Check if a file was selected
        file_label.configure(text=f"Selected File: {file_path}")
        AudioGraph(file_path)

pick_button = ctk.CTkButton(master=analysis, text="Pick a File", command=pick_file)
pick_button.grid(row=3,column=1)

# Create a label to display the selected file path
file_label = ctk.CTkLabel(master=analysis, text="No file selected")
file_label.grid(row=2,column=1)

def AudioGraph(file):
    plot_frame = ctk.CTkFrame(master=analysis)
    plot_frame.grid(row=4,column=1)
    fig = Figure(figsize=(6, 4), dpi=100)
    ax = fig.add_subplot(111)

    out=output(file)
    ax.plot(out[2],out[3])

    canvas = FigureCanvasTkAgg(fig, master=plot_frame)
    canvas.draw()
    canvas.get_tk_widget().pack(fill="both", expand=True)

    plot_frame1 = ctk.CTkFrame(master=analysis)
    l=ctk.CTkLabel(master=analysis,text='DFT Result')
    l.grid(row=5,column=1)
    plot_frame1.grid(row=6,column=1)
    fig1 = Figure(figsize=(6, 4), dpi=100)
    ax1 = fig1.add_subplot(111)

    ax1.plot(out[0],out[1])

    canvas1 = FigureCanvasTkAgg(fig1, master=plot_frame1)
    canvas1.draw()

    toolbar1 = NavigationToolbar2Tk(canvas1, plot_frame1)
    toolbar1.update()
    canvas1.get_tk_widget().pack(fill="both", expand=True)

app.mainloop()