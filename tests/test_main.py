import unittest
import subprocess
import os


class TestMainIntegration(unittest.TestCase):
    def test_main_output(self):
        # Ensure `persons.json` is accessible
        if not os.path.exists("persons.json"):
            self.fail("persons.json file is missing in the test directory.")
        
        # Run `main.py`
        result = subprocess.run(
            ["python", "main.py"],
            capture_output=True,
            text=True
        )

        # Check for expected output
        self.assertIn("records printed", result.stdout, "Output is missing 'records printed'")
        self.assertNotEqual(result.stdout.strip(), "", "Output is empty")

if __name__ == "__main__":
    unittest.main()
