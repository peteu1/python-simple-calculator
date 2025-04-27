from typing import Union, List, Tuple
from math import pi
from tkinter import messagebox

# Constants
ERROR_RETURN = -1

class ShapeCalculator:
    """Class containing methods for calculating geometric properties."""
    
    @staticmethod
    def calculate_area(shape_name: str, dimensions: dict) -> float:
        """Calculate area of 2D shapes.
        
        Args:
            shape_name: Name of the shape (rectangle, square, triangle, circle)
            dimensions: Dictionary containing relevant dimensions (length, breadth, height, radius)
            
        Returns:
            float: Area of the shape or ERROR_RETURN if shape not supported
        """
        shape_name = shape_name.lower()
        
        try:
            if shape_name == "rectangle":
                return dimensions["length"] * dimensions["breadth"]
            elif shape_name == "square":
                return dimensions["length"] ** 2
            elif shape_name == "triangle":
                return 0.5 * dimensions["breadth"] * dimensions["height"]
            elif shape_name == "circle":
                return pi * dimensions["radius"] ** 2
            else:
                return ERROR_RETURN
        except KeyError:
            return ERROR_RETURN

    @staticmethod
    def calculate_volume(shape_name: str, dimensions: dict) -> float:
        """Calculate volume of 3D shapes.
        
        Args:
            shape_name: Name of the shape (sphere, cube, cone, cuboid, cylinder)
            dimensions: Dictionary containing relevant dimensions (length, breadth, height, radius)
            
        Returns:
            float: Volume of the shape or ERROR_RETURN if shape not supported
        """
        shape_name = shape_name.lower()
        
        try:
            if shape_name == "sphere":
                return 4/3 * pi * dimensions["radius"] ** 3
            elif shape_name == "cube":
                return dimensions["length"] ** 3
            elif shape_name == "cone":
                return pi * dimensions["radius"] ** 2 * dimensions["height"] / 3
            elif shape_name == "cuboid":
                return dimensions["length"] * dimensions["breadth"] * dimensions["height"]
            elif shape_name == "cylinder":
                return pi * dimensions["radius"] ** 2 * dimensions["height"]
            else:
                return ERROR_RETURN
        except KeyError:
            return ERROR_RETURN


class ConditionChecker:
    """Class containing methods for checking various mathematical conditions."""

    @staticmethod
    def check_pythagorean_triplet(a: float, b: float, c: float) -> bool:
        """Check if three numbers form a Pythagorean triplet.
        
        Args:
            a: First number
            b: Second number
            c: Third number (hypotenuse)
            
        Returns:
            bool: True if numbers form a Pythagorean triplet, False otherwise
        """
        return abs(a**2 + b**2 - c**2) < 1e-10  # Using small epsilon for float comparison

    @staticmethod
    def get_complementary_supplementary(angle: float) -> Tuple[Union[float, str], Union[float, str]]:
        """Calculate complementary and supplementary angles.
        
        Args:
            angle: Original angle in degrees
            
        Returns:
            tuple: (complementary angle, supplementary angle)
                  Returns "error" string for invalid cases
        """
        complementary = "error"
        supplementary = "error"
        
        if 0 <= angle <= 90:
            complementary = 90 - angle
            supplementary = 180 - angle
        elif angle <= 180:
            supplementary = 180 - angle

        return complementary, supplementary

    @staticmethod
    def show_angle_results(angle: float) -> List[Union[float, str]]:
        """Display and return complementary and supplementary angles.
        
        Args:
            angle: Original angle in degrees
            
        Returns:
            list: [complementary angle, supplementary angle]
        """
        comp_angle, supp_angle = ConditionChecker.get_complementary_supplementary(angle)
        
        messagebox.showinfo("Complementary Angle", comp_angle)
        messagebox.showinfo("Supplementary Angle", supp_angle)
        
        return [comp_angle, supp_angle]