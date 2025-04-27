from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from MyMath import ShapeCalculator, ConditionChecker

class CalculatorApp:
    """Main calculator application class."""

    # GUI Constants 
    WINDOW_SIZE = "500x500"
    BG_COLOR = "light blue"
    DARK_BG = "Dark blue"
    BUTTON_COLOR = "red"
    ENTRY_BG = "orange"
    FONT = ("Helvetica", 20)

    def __init__(self):
        """Initialize the calculator application."""
        self.root = Tk()
        self.setup_root_window()
        
        # Initialize state variables
        self.shapes = StringVar(value="Select")
        self.solidshape = StringVar(value="Select")
        self.conditions = StringVar(value="Select")
        
        # Create notebook and frames
        self.notebook = self.create_notebook()
        self.area_frame = self.create_area_tab()
        self.volume_frame = self.create_volume_tab()
        self.condition_frame = self.create_condition_tab()

        # Initialize calculators
        self.shape_calc = ShapeCalculator()
        self.condition_checker = ConditionChecker()

    def setup_root_window(self) -> None:
        """Set up the main window properties."""
        self.root.title('MyMath')
        self.root.geometry(self.WINDOW_SIZE)
        self.root.configure(background=self.BG_COLOR)

    def create_notebook(self) -> ttk.Notebook:
        """Create and return the main notebook widget."""
        notebook = ttk.Notebook(self.root)
        notebook.pack(pady=5)
        return notebook

    def create_entry_with_label(self, parent: Frame, label_text: str) -> Entry:
        """Create a labeled entry widget."""
        Label(parent, text=label_text, bg=self.BG_COLOR).pack()
        entry = Entry(parent, font=self.FONT, bg=self.ENTRY_BG)
        entry.pack()
        return entry

    def create_area_tab(self) -> Frame:
        """Create and set up the area calculator tab."""
        frame = Frame(self.notebook, width=300, height=300, bg=self.DARK_BG)
        frame.pack(fill="both", expand=1)
        self.notebook.add(frame, text="Area Calculator")

        # Area shape selector
        shapes = ["Circle", "Square", "Triangle", "Rectangle"]
        OptionMenu(frame, self.shapes, *shapes).pack()
        Button(frame, text="Select shape", command=lambda: self.show_selection(frame, self.shapes),
               bg=self.BG_COLOR).pack()

        # Create entries
        self.radius_entry = self.create_entry_with_label(frame, "Enter radius or side in m")
        self.height_entry = self.create_entry_with_label(frame, 
            "Enter height or width in m if applicable else enter 0")

        # Create calculate button
        self.create_button_frame(frame, self.calculate_area)
        
        return frame

    def create_volume_tab(self) -> Frame:
        """Create and set up the volume calculator tab."""
        frame = Frame(self.notebook, width=300, height=300, bg=self.DARK_BG)
        frame.pack(fill="both", expand=1)
        self.notebook.add(frame, text="Volume Calculator")

        # Volume shape selector
        shapes = ["Cone", "Sphere", "Cylinder", "Cube", "Cuboid"]
        OptionMenu(frame, self.solidshape, *shapes).pack()
        Button(frame, text="Select shape", command=lambda: self.show_selection(frame, self.solidshape),
               bg=self.BG_COLOR).pack()

        # Create entries
        self.radius_entry2 = self.create_entry_with_label(frame, "Enter radius or side in m")
        self.height_entry2 = self.create_entry_with_label(frame, 
            "Enter height in m if applicable else enter 0")
        self.width_entry = self.create_entry_with_label(frame,
            "Enter breadth in m if applicable else enter 0")

        # Create calculate button
        self.create_button_frame(frame, self.calculate_volume)
        
        return frame

    def create_condition_tab(self) -> Frame:
        """Create and set up the condition checker tab."""
        frame = Frame(self.notebook, width=300, height=300, bg=self.DARK_BG)
        frame.pack(fill="both", expand=1)
        self.notebook.add(frame, text="Condition Checker")

        # Condition selector
        conditions = ["Pythagorean Triplet Checker", "Complimentary&Supplementary Angles"]
        OptionMenu(frame, self.conditions, *conditions).pack()
        Button(frame, text="Select condition", command=lambda: self.show_selection(frame, self.conditions),
               bg=self.BG_COLOR).pack()

        # Create entries
        self.side1_entry = self.create_entry_with_label(frame, "Enter first number")
        self.side2_entry = self.create_entry_with_label(frame, "Enter second number")
        self.side3_entry = self.create_entry_with_label(frame, "Enter third number")
        self.angle_entry = self.create_entry_with_label(frame, "Enter angle in degrees")

        # Create calculate button
        self.create_button_frame(frame, self.check_condition)
        
        return frame

    def create_button_frame(self, parent: Frame, command: callable) -> None:
        """Create a frame with a calculate button."""
        button_frame = Frame(parent)
        button_frame.pack()
        Button(button_frame, text="Calculate", command=command,
               bg=self.BUTTON_COLOR).grid(row=0, column=0, padx=10)

    def show_selection(self, frame: Frame, var: StringVar) -> None:
        """Show the selected option."""
        Label(frame, text=var.get()).pack()

    def get_entry_value(self, entry: Entry, default: float = 0) -> float:
        """Safely get a numeric value from an entry widget."""
        try:
            return float(entry.get() or default)
        except ValueError:
            return default

    def calculate_area(self) -> None:
        """Handle area calculation."""
        shape = self.shapes.get()
        dimensions = {
            "radius": self.get_entry_value(self.radius_entry),
            "length": self.get_entry_value(self.radius_entry),
            "breadth": self.get_entry_value(self.height_entry),
            "height": self.get_entry_value(self.height_entry)
        }
        
        result = self.shape_calc.calculate_area(shape, dimensions)
        
        if result != -1:
            messagebox.showinfo(f"Area {shape}", result)
        else:
            messagebox.showwarning("Invalid Input", "Shape is not available")

    def calculate_volume(self) -> None:
        """Handle volume calculation."""
        shape = self.solidshape.get()
        dimensions = {
            "radius": self.get_entry_value(self.radius_entry2),
            "length": self.get_entry_value(self.radius_entry2),
            "breadth": self.get_entry_value(self.width_entry),
            "height": self.get_entry_value(self.height_entry2)
        }
        
        result = self.shape_calc.calculate_volume(shape, dimensions)
        
        if result != -1:
            messagebox.showinfo(f"Volume {shape}", result)
        else:
            messagebox.showwarning("Invalid Input", "Shape is not available")

    def check_condition(self) -> None:
        """Handle condition checking."""
        condition = self.conditions.get()
        
        if condition == "Pythagorean Triplet Checker":
            a = self.get_entry_value(self.side1_entry)
            b = self.get_entry_value(self.side2_entry)
            c = self.get_entry_value(self.side3_entry)
            
            is_triplet = self.condition_checker.check_pythagorean_triplet(a, b, c)
            result = "This is" if is_triplet else "This is not"
            messagebox.showinfo("Check", f"{result} a Pythagorean Triplet.")
            
        elif condition == "Complimentary&Supplementary Angles":
            angle = self.get_entry_value(self.angle_entry)
            self.condition_checker.show_angle_results(angle)

    def run(self) -> None:
        """Start the application main loop."""
        self.root.mainloop()


if __name__ == "__main__":
    app = CalculatorApp()
    app.run()