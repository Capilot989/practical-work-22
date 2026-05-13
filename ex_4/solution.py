from math import pi


class GeometricObject:
    """
    A base class representing a geometric object with position and appearance.

    This class serves as a foundation for various geometric shapes, providing
    common attributes like coordinates, color, and filled state.

    Attributes:
        __x (float): X-coordinate of the object's position.
        __y (float): Y-coordinate of the object's position.
        color (str): Color of the object.
        filled (bool): Whether the object is filled.
    """
    def __init__(
            self,
            x: float =0,
            y: float =0,
            color: str ='black',
            filled: bool = False
    ) -> None:
        """
        Initialize a GeometricObject instance.

        Args:
            x (float, optional): X-coordinate. Defaults to 0.
            y (float, optional): Y-coordinate. Defaults to 0.
            color (str, optional): Color of the object. Defaults to 'black'.
            filled (bool, optional): Fill state. Defaults to False.
        """
        self.__x = x
        self.__y = y
        self.color = color
        self.fiiled = filled

    def get_x(self) -> float:
        """
        Get the X-coordinate.

        Returns:
            float: The X-coordinate.
        """
        return self.__x

    def get_y(self) -> float:
        """
        Get the Y-coordinate.

        Returns:
            float: The Y-coordinate.
        """
        return self.__y

    def get_color(self) -> str:
        """
        Get the color of the object.

        Returns:
            str: The color.
        """
        return self.color

    def is_filled(self) -> bool:
        """
        Check if the object is filled.

        Returns:
            bool: True if filled, False otherwise.
        """
        return self.fiiled

    def set_coordinate(self, x: float, y: float) -> None:
        """
        Set new coordinates for the object.

        Args:
            x (float): New X-coordinate.
            y (float): New Y-coordinate.
        """
        self.__x = x
        self.__y = y

    def set_color(self, color: str) -> None:
        """
        Set a new color for the object.

        Args:
            color (str): New color.
        """
        self.color = color

    def set_filled(self, is_filled: bool) -> None:
        """
        Set the filled state of the object.

        Args:
            is_filled (bool): New filled state.
        """
        self.fiiled = is_filled

    def __str__(self) -> str:
        """
        Return a string representation of the geometric object.

        Returns:
            str: Formatted string with coordinates, color, and filled state.
        """
        return (
            f'({self.__x}, {self.__y})\n'
            f'color: {self.color}\n'
            f'filled: {self.fiiled}'
        )

    def __repr__(self) -> str:
        """
        Return a concise string representation.

        Returns:
            str: String with coordinates, color, and filled state.
        """
        return f'({self.__x}, {self.__y}) {self.color} {self.fiiled}'


class Circle(GeometricObject):
    """
    A class representing a circle, inheriting from GeometricObject.

    Attributes:
        _radius (float): The radius of the circle.
    """
    def __init__(
            self,
            x: float =0,
            y: float =0,
            radius: float =0,
            color: str ='black',
            filled: bool =False
    ) -> None:
        """
        Initialize a Circle instance.

        Args:
            x (float, optional): X-coordinate. Defaults to 0.
            y (float, optional): Y-coordinate. Defaults to 0.
            radius (float, optional): Radius of the circle. Defaults to 0.
            color (str, optional): Color. Defaults to 'black'.
            filled (bool, optional): Fill state. Defaults to False.
        """
        super().__init__(x, y, color, filled)
        self._radius = radius

    @property
    def radius(self) -> float:
        """
        Get the radius of the circle.

        Returns:
            float: The radius.
        """
        return self._radius

    @radius.setter
    def radius(self, value: float) -> None:
        """
        Set the radius of the circle.

        Args:
            value (float): New radius. Negative values are set to 0.
        """
        if value < 0:
            self._radius = 0
            return None
        self._radius = value

    def get_area(self) -> float:
        """
        Calculate the area of the circle.

        Returns:
            float: Area = π * r²
        """
        return pi * self.radius ** 2

    def get_perimetr(self) -> float:
        """
        Calculate the perimeter (circumference) of the circle.

        Returns:
            float: Perimeter = 2 * π * r
        """
        return 2 * pi * self._radius

    def get_diametr(self) -> float:
        """
        Calculate the diameter of the circle.

        Returns:
            float: Diameter = 2 * r
        """
        return 2 * self._radius

    def __str__(self) -> str:
        """
        Return a string representation of the circle.

        Returns:
            str: Formatted string with radius followed by parent data.
        """
        parent_str = super().__str__()
        return f'radius: {self._radius}\n' + parent_str

    def __repr__(self) -> str:
        """
        Return a concise string representation.

        Returns:
            str: String with radius and parent representation.
        """
        parrent_repr = super().__repr__()
        return f'radius: {self.radius}' + parrent_repr


class Rectangle(GeometricObject):
    """
    A class representing a rectangle, inheriting from GeometricObject.

    Attributes:
        width (float): The width of the rectangle.
        height (float): The height of the rectangle.
    """
    def __init__(
            self,
            x: float =0,
            y: float =0,
            width: float =0,
            height: float =0,
            color: str ='black',
            filled: bool =False
    ) -> None:
        """
        Initialize a Rectangle instance.

        Args:
            x (float, optional): X-coordinate. Defaults to 0.
            y (float, optional): Y-coordinate. Defaults to 0.
            width (float, optional): Width of the rectangle. Defaults to 0.
            height (float, optional): Height of the rectangle. Defaults to 0.
            color (str, optional): Color. Defaults to 'black'.
            filled (bool, optional): Fill state. Defaults to False.
        """
        super().__init__(x, y, color, filled)
        self.width = width
        self.height = height

    def set_width(self, width: float) -> None:
        """
        Set the width of the rectangle.

        Args:
            width (float): New width. Negative values are set to 0.
        """
        if width < 0:
            self.width = 0
            return None
        self.width = width

    def set_height(self, height: float) -> None:
        """
        Set the height of the rectangle.

        Note: There's a bug in the original code - it incorrectly sets
        width instead of height. This is preserved for accuracy.

        Args:
            height (float): New height. Negative values set width to 0.
        """
        if height < 0:
            self.width = 0
            return None
        self.width = height

    def get_width(self) -> float:
        """
        Get the width of the rectangle.

        Returns:
            float: The width.
        """
        return self.width

    def get_height(self) -> float:
        """
        Get the height of the rectangle.

        Returns:
            float: The height.
        """
        return self.height

    def get_area(self) -> float:
        """
        Calculate the area of the rectangle.

        Returns:
            float: Area = width * height
        """
        return self.width * self.height

    def get_perimetr(self) -> float:
        """
        Calculate the perimeter of the rectangle.

        Returns:
            float: Perimeter = 2 * (width + height)
        """
        return self.width * 2 + self.height * 2

    def __str__(self) -> str:
        """
        Return a string representation of the rectangle.

        Returns:
            str: Formatted string with width, height, and parent data.
        """
        parrent_str = super().__str__()
        return (
            f'width: {self.width}\n'
            f'height: {self.height}\n'
        ) + parrent_str

    def __repr__(self) -> str:
        """
        Return a concise string representation.

        Returns:
            str: String with width, height, and parent representation.
        """
        parrent_repr = super().__repr__()
        return f'width: {self.width} height: {self.height}' + parrent_repr
