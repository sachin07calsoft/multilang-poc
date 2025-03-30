import subprocess

# Function to run unit tests
def run_unit_tests():
    print("Running unit tests...")
    # Running unit tests
    subprocess.run(["mvn", "test"])

# Function to run functional tests (Cucumber)
def run_functional_tests():
    print("Running functional tests...")
    # Running functional tests (Cucumber with a specific tag for functional tests)
    subprocess.run(["mvn", "test", "-Dcucumber.options='--tags @functional'"])

# Function to run integration tests
def run_integration_tests():
    print("Running integration tests...")
    # Running integration tests (you can define a specific test class here)
    subprocess.run(["mvn", "test", "-Dtest=ApplicationTests"])

# Function to run SonarQube analysis for Unit Test project
def run_sonarqube_unit():
    print("Running SonarQube analysis for Unit Test project...")
    subprocess.run([
        "mvn", "sonar:sonar", 
        "-Dsonar.projectKey=multilang-unit-test", # SonarQube project key for unit tests
        "-Dsonar.projectName=Multilang-Unit",  # Unique name for functional tests
        "-Dsonar.host.url=http://54.225.78.240:9000", # SonarQube server URL
        "-Dsonar.login=squ_5a1934abc4671f79b3353c7d59593a8ce68e00e6",    # Your SonarQube token for authentication
        "-Dsonar.sources=src/main/java",          # Main source directory
        "-Dsonar.tests=src/test/java",            # Test directory
        "-Dsonar.test.inclusions=src/test/java/**/*.java"  # Only include test classes
    ])

# Function to run SonarQube analysis for Functional Test project
def run_sonarqube_functional():
    print("Running SonarQube analysis for Functional Test project...")
    subprocess.run([
        "mvn", "sonar:sonar", 
        "-Dsonar.projectKey=multilang-functional-test", # SonarQube project key for functional tests
        "-Dsonar.projectName=Multilang-Functional",  # Unique name for functional tests
        "-Dsonar.host.url=http://54.225.78.240:9000",    # SonarQube server URL
        "-Dsonar.login=squ_d8118303aeeb6518efe3b693e6a8cae81d990a6a",        # Your SonarQube token for authentication
        "-Dsonar.sources=src/main/java",          # Main source directory
        "-Dsonar.tests=src/test/java",            # Test directory
        "-Dsonar.test.inclusions=src/test/java/**/*.java"  # Only include test classes
    ])

# Function to run SonarQube analysis for Integration Test project
def run_sonarqube_integration():
    print("Running SonarQube analysis for Integration Test project...")
    subprocess.run([
        "mvn", "sonar:sonar", 
        "-Dsonar.projectKey=multilang-integration-test", # SonarQube project key for integration tests
        "-Dsonar.projectName=Multilang-Integration",  # Unique name for functional tests
        "-Dsonar.host.url=http://54.225.78.240:9000",      # SonarQube server URL
        "-Dsonar.login=squ_66ef5707f6a34abcabcbd6354eff3db74ea6774a",          # Your SonarQube token for authentication
        "-Dsonar.sources=src/main/java",          # Main source directory
        "-Dsonar.tests=src/test/java",            # Test directory
        "-Dsonar.test.inclusions=src/test/java/**/*.java"  # Only include test classes
    ])

# Main execution block
if __name__ == "__main__":
    # Run Unit Tests and then SonarQube analysis for Unit Test project
    run_unit_tests()
    run_sonarqube_unit()

    # Run Functional Tests (Cucumber) and then SonarQube analysis for Functional Test project
    run_functional_tests()
    run_sonarqube_functional()

    # Run Integration Tests and then SonarQube analysis for Integration Test project
    run_integration_tests()
    run_sonarqube_integration()
