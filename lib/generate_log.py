from datetime import datetime

def generate_log(entries):
    """
    Creates a timestamped log file and writes the provided entries.

    Args:
        entries (list): List of strings to write to the log file.

    Returns:
        str: Name of the created log file.

    Raises:
        ValueError: If entries is not a list.
    """

    if not isinstance(entries, list):
        raise ValueError("Input must be a list.")

    filename = f"log_{datetime.now().strftime('%Y%m%d')}.txt"

    with open(filename, "w") as file:
        for entry in entries:
            file.write(f"{entry}\n")

    print(f"Log file created: {filename}")

    return filename


# Example usage
if __name__ == "__main__":
    sample_logs = [
        "Task added",
        "Task completed",
        "User logged out"
    ]

    generate_log(sample_logs)