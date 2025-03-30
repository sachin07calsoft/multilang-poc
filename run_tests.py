import subprocess

# Run unit tests
def run_unit_tests():
    subprocess.run(["mvn", "test"])

# Run functional tests (Cucumber)
def run_functional_tests():
    subprocess.run(["mvn", "test", "-Dcucumber.options='--tags @functional'"])

# Run integration tests
def run_integration_tests():
    subprocess.run(["mvn", "test", "-Dtest=ApplicationTests"])

if __name__ == "__main__":
   # run_unit_tests()
   # run_functional_tests() // Ran Sucessfully
   # run_integration_tests() // Ran Sucessfully
