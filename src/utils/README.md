# Utilities Module

[![Build Status](https://img.shields.io/github/actions/workflow/status/Durban-University-of-Technology-DUT/git-basics-starter/build.yml?branch=main)](https://github.com/Durban-University-of-Technology-DUT/git-basics-starter/actions)
[![License](https://img.shields.io/github/license/Durban-University-of-Technology-DUT/git-basics-starter)](https://github.com/Durban-University-of-Technology-DUT/git-basics-starter/blob/main/LICENSE)
[![GitHub Issues](https://img.shields.io/github/issues/Durban-University-of-Technology-DUT/git-basics-starter)](https://github.com/Durban-University-of-Technology-DUT/git-basics-starter/issues)

---

## Overview

The `utils` modules in the **Git Basics Starter** repository contain utility functions for both the Java and Python components of the project. These utilities are designed to handle common tasks such as file manipulation, data processing, and other reusable functions that are shared across different parts of the project.

- **Java Utilities**: Located in `src/main/java/utils/`, these utilities provide essential helper methods for Java-based operations.
- **Python Utilities**: Found in `src/main/python/utils/`, these utilities offer similar functionality for Python-based tasks.

---

## Directory Structure

```plaintext
src/
├── main/
│   ├── java/
│   │   ├── utils/
│   │   │   ├── JavaHelper.java  # Utility functions for Java
│   │   │   └── README.md        # Documentation for Java utils
│   └── python/
│       ├── utils/
│       │   ├── helpers.py       # Utility functions for Python
│       │   └── README.md        # Documentation for Python utils
```

### Java Utilities: `src/main/java/utils/`

- **`JavaHelper.java`**: 
  - **Purpose**: Contains utility functions that are commonly used throughout the Java application. These include methods for printing messages, manipulating strings, or handling other repetitive tasks.
  - **Example Function**: 
    ```java
    public class JavaHelper {
        public static void printMessage(String message) {
            System.out.println(message);
        }
    }
    ```

### Python Utilities: `src/main/python/utils/`

- **`helpers.py`**: 
  - **Purpose**: Provides utility functions that support the main Python application. These include functions for file handling, data processing, and other common operations.
  - **Example Function**: 
    ```python
    def print_message(message):
        print(message)
    ```

---

## Usage

### Using Java Utilities

To use the utilities provided in `JavaHelper.java`, simply import the class into your Java application:

```java
import utils.JavaHelper;

public class Main {
    public static void main(String[] args) {
        JavaHelper.printMessage("Hello from JavaHelper!");
    }
}
```

### Using Python Utilities

To use the functions in `helpers.py`, import them into your Python scripts as needed:

```python
from utils.helpers import print_message

print_message("Hello from helpers.py!")
```

### Functions Overview

#### `JavaHelper.java`

- **`printMessage(String message)`**:
  - **Description**: Prints the given message to the console.
  - **Usage**: Useful for logging or providing user feedback.

#### `helpers.py`

- **`print_message(message: str) -> None`**:
  - **Description**: Prints the given message to the console.
  - **Usage**: Ideal for simple logging or debug output.

---

## Contributing

We welcome contributions to the `utils` modules! If you have a utility function that could benefit either the Java or Python components of the project, feel free to submit a pull request. Please ensure that your code is well-documented and adheres to the project’s coding standards.

### Steps to Contribute

1. **Fork the Repository**: Start by forking the main repository to your GitHub account.
2. **Create a Branch**: Create a new branch for your feature or bugfix.
3. **Make Changes**: Write your code and add appropriate tests.
4. **Submit a Pull Request**: Push your changes to your forked repository and open a pull request against the main branch.

Please refer to the main [CONTRIBUTING.md](https://github.com/Durban-University-of-Technology-DUT/git-basics-starter/blob/main/CONTRIBUTING.md) file for more detailed guidelines.

---

## License

This project is licensed under the MIT License - see the [LICENSE](https://github.com/Durban-University-of-Technology-DUT/git-basics-starter/blob/main/LICENSE) file for details.

---

## Additional Resources

For more information on how to use or extend these utilities, check out the following resources:

- [Java Documentation](https://docs.oracle.com/en/java/)
- [Python Standard Library](https://docs.python.org/3/library/index.html)
- [GitHub Actions](https://docs.github.com/en/actions)

---

## Contact

If you have any questions or need further assistance, please open an issue on the GitHub repository, or reach out directly via [info@skunkworks.africa](mailto:info@skunkworks.africa).


### Key Updates:

- **Repository Paths**: References to `src/main/java/utils/` and `src/main/python/utils/` are included, clearly distinguishing the Java and Python utilities.
- **Java and Python Examples**: Provided specific examples for both the Java and Python utilities, ensuring users know how to utilize these functions in their respective environments.
- **Consistent Structure**: Maintains a clean and organized format, with sections for usage, contributions, and additional resources, making it easy to follow.

> This `README.md` provides a comprehensive guide for users and contributors, tailored to the dual-language nature of your project.
