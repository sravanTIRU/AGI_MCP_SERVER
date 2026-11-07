from mcp.server.mcpserver import MCPServer

mcp = MCPServer("Hello MCP")


# Tool 1: Greeting (original)
@mcp.tool()
def get_greeting(name: str) -> str:
    """Return a greeting for a student."""
    return f"Hello, {name}! Your first MCP tool works."


# Tool 2: Addition (original)
@mcp.tool()
def add_numbers(a: int, b: int) -> int:
    """Add two numbers."""
    return a + b


# Tool 3: Multiplication
@mcp.tool()
def multiply_numbers(a: float, b: float) -> float:
    """Multiply two numbers."""
    return a * b


# Tool 4: Student information
@mcp.tool()
def get_student_info(name: str, course: str) -> str:
    """Return a student's name and course."""
    return f"Student: {name} | Course: {course}"


# Tool 5: Grade calculator
@mcp.tool()
def calculate_grade(marks: float, total: float = 100) -> str:
    """Calculate percentage and grade from obtained and total marks."""

    if total <= 0:
        return "Error: Total marks must be greater than zero."

    if marks < 0 or marks > total:
        return "Error: Marks must be between zero and total marks."

    percentage = (marks / total) * 100

    if percentage >= 90:
        grade = "A"
    elif percentage >= 75:
        grade = "B"
    elif percentage >= 60:
        grade = "C"
    elif percentage >= 40:
        grade = "D"
    else:
        grade = ("F",)

    return f"Percentage: {percentage:.2f}% | Grade: {grade}"


# Tool 6: Even or odd checker
@mcp.tool()
def check_even_odd(number: int) -> str:
    """Check whether an integer is even or odd."""

    if number % 2 == 0:
        return f"{number} is even."

    return f"{number} is odd."


if __name__ == "__main__":
    mcp.run()
