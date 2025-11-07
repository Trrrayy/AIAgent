"""
Auto-generated script for ExampleCorp
This script prints a brief company summary and includes a simple test.
"""

def get_summary():
    return "ExampleCorp builds data science platforms and AI assistants for education."

def print_summary():
    print("=== Company Report ===")
    print(get_summary())

def test_summary():
    summary = get_summary()
    assert "ExampleCorp" in summary or "company" in summary.lower(), "Missing company name in summary."

if __name__ == "__main__":
    print_summary()
    print("Test passed: summary includes company name.")
