# Amazon Q Code Generation Demo

A Python project demonstrating Amazon Q's code generation capabilities with user data processing functions.

## Overview

This project contains sample code that showcases Amazon Q's ability to generate Python code suggestions. It includes functions for processing user data, specifically working with lists of user objects containing names, cities, and states.

## Features

- User data processing functions
- List manipulation and filtering
- Name and city extraction utilities
- AWS SDK integration (boto3) ready

## Prerequisites

- Python 3.7 or higher
- pip package manager

## Installation

1. Clone this repository:
```bash
git clone <repository-url>
cd <project-directory>
```

2. Install the required dependencies:
```bash
pip install -r requirements.txt
```

## Usage

Run the main script to see the demo functions in action:

```bash
python AmazonQ_generate_suggestion-copy.py
```

### Functions Available

- `listnames(users)` - Prints all user names from a list of user objects
- `list_name_and_city(users)` - Returns a list of tuples containing name and city pairs

### Sample Data

The project includes sample user data with the following structure:
```python
{
    "name": "User Name",
    "id": "user_id",
    "city": "City Name",
    "state": "State Code"
}
```

## Dependencies

- **boto3** (1.35.83) - AWS SDK for Python
- **requests** (2.32.4) - HTTP library for Python
- **botocore** - Core functionality for AWS SDK
- Additional supporting libraries (see requirements.txt)

## Development

This project is set up to work with Amazon Q for code generation. To use Amazon Q suggestions:

1. Place your cursor at the end of a line
2. Press Enter to generate suggestions
3. Press Tab to accept suggestions

## Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Submit a pull request

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Support

For questions or issues, please open an issue in the repository or contact the maintainers.