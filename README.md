# Define the content for the README.md file
readme_content = """
# Online Bookstore Project

This Online Bookstore project is developed using Django, incorporating both frontend templates and backend API functionalities using Django Rest Framework.

## Project Overview

The goal of this project is to create an interactive web interface allowing users to browse, search, and purchase books. It involves building both frontend and backend components.

### Backend (Django and DRF)
...

### Frontend (Django)
...

### Integration
...

## Getting Started

To set up and run this project locally, follow these steps:

1. Clone the repository.

2. Set up a virtual environment.
```
python -m venv new_env
source new_env/bin/activate  # On macOS/Linux 
.\new_env\Scripts\activate    # On Windows
deactivate # deactivate the venv
```

3. Install dependencies.
```
pip install -r requirements.txt
pip list # verify installed packages
```

3. Run migrations to set up the database.
4. Start the Django server.
5. Access the application through the provided URL.


## Contributing

Contributions are welcome! If you want to contribute to this project, feel free to open issues or submit pull requests.

## License

This project is licensed under the [License Name] - see the [LICENSE](link) file for details.
"""

# Write the content to README.md file with UTF-8 encoding
with open('README.md', 'w', encoding='utf-8') as readme_file:
    readme_file.write(readme_content)

print("README.md file has been generated successfully.")
