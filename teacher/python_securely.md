
The link to the video: https://www.youtube.com/watch?v=YZOKnvisJpw

### **Bandit: Static Code Analysis**

Bandit helps you find security vulnerabilities in your own Python code.

  * **Installation:**

    ```bash
    pip install bandit
    ```

  * **Basic Usage:**
    To check a single file, run the command followed by the file path.

    ```bash
    bandit your_script.py
    ```

  * **Checking a Directory:**
    To recursively scan an entire directory, use the `-r` flag.

    ```bash
    bandit -r your_project_folder/
    ```

  * **Filtering Output:**
    You can filter the output by the severity of the issues using the `-l` flag.

      * Low: `-l`
      * Medium: `-ll`
      * High: `-lll`
        For example, to only show high-severity issues:

    <!-- end list -->

    ```bash
    bandit -lll your_script.py
    ```

  * **Ignoring Specific Issues:**
    To tell Bandit to ignore a specific security issue in your code, add a `noqa` comment followed by the issue code (e.g., `no sec b105`).

    ```python
    # Bad practice: Hardcoded password
    password = "mysecretpassword"  # noqa: B105
    ```

-----

### **Safety: Dependency Security**

Safety checks your project's dependencies for known security vulnerabilities.

  * **Installation:**

    ```bash
    pip install safety
    ```

  * **Basic Usage:**
    Run the command to check all installed packages in your current environment.

    ```bash
    safety check
    ```

  * **Checking Requirements:**
    To check the packages listed in a `requirements.txt` file, use the `-r` flag.

    ```bash
    safety check -r requirements.txt
    ```

  * **Viewing Full Report:**
    Use the `--full-report` flag to get a detailed report for any found vulnerabilities, including the CVE ID and a link to more information.

    ```bash
    safety check --full-report
    ```

  * **Ignoring Specific Vulnerabilities:**
    To ignore a specific vulnerability by its ID (e.g., `51111`), use the `-i` flag. This is useful when you have a valid reason not to fix a specific issue.

    ```bash
    safety check -i 51111
    ```