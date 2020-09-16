from tkinter import *
import pandas as pd

# Function for submitting data to the excel file
def submit_fields():
    # The path to the output file
    path = "excel.xlsx"

    # Read the excel file and assign the series
    df1 = pd.read_excel(path)
    SeriesA = df1["Date"]
    SeriesB = df1["School"]

    # Get the user entires and assign+append them to the Series
    A = pd.Series(entry1.get())
    B = pd.Series(entry2.get())
    SeriesA = SeriesA.append(A)
    SeriesB = SeriesB.append(B)

    # Put the data back into a data frame and write to back to the file
    df2 = pd.DataFrame({"Date": SeriesA, "School": SeriesB})
    df2.to_excel(path, index=False)

    # Remove entries from widget
    entry1.delete(0, END)
    entry2.delete(0, END)


# Creates a tkinter widget
master = Tk()

# Labels the widget
Label(master, text="Date").grid(row=0)
Label(master, text="School").grid(row=1)

# Create the entires
entry1 = Entry(master)
entry2 = Entry(master)

# Position entires on the widget
entry1.grid(row=0, column=1)
entry2.grid(row=1, column=1)

# Assign actions to buttons and position them
Button(master, text="Quit", command=master.quit).grid(row=3, column=0, pady=4)
Button(master, text="Submit", command=submit_fields).grid(row=3, column=1, pady=4)

mainloop()
