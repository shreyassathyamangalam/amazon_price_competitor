# Amazon Price Competitor

**Version:** 0.1.0  
**Python Version Required:** >= 3.13

## Overview

The Amazon Price Competitor project is designed to help users track and analyze product prices on Amazon. It employs various dependencies to provide features such as integration with OpenAI's language models, data management, and user-friendly interface options through Streamlit.

## Features

- **Product Price Tracking:** Monitor Amazon product prices over time.
- **Data Storage:** Utilizes TinyDB for efficient data storage and retrieval.
- **User Interface:** A web-based UI created using Streamlit for easy interaction and visual representation of data.
- **Environment Configuration:** Supports environment variable management with Python Dotenv.
- **File Watching:** Reacts to changes in the target data files to keep information up to date.

## Getting Started

### Prerequisites

Before you begin, ensure you have met the following requirements:

- Python 3.13 or higher
- pip (Python package manager)

### Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/yourusername/amazon_price_competitor.git
   ```

2. Navigate to the project directory:

   ```bash
   cd amazon_price_competitor
   ```

3. Install the required dependencies:

   ```bash
   pip install -r requirements.txt
   ```

   Alternatively, you can install dependencies using `pyproject.toml`:

   ```bash
   pip install .
   ```

### Usage

To run the application, execute the following command:

```bash
streamlit run main.py
```

This will start a local web server, and you can interact with the application via your web browser at `http://localhost:8501`.

### File Structure

The repository contains the following files:

- **.gitignore:** Specifies files to be ignored by Git.
- **.python-version:** Used to define the Python version for the project.
- **README.md:** Project documentation file.
- **data.json:** Data file for storing product information (structure to be defined).
- **main.py:** Main entry point for the application.
- **pyproject.toml:** Project dependencies and metadata.
- **src:** Directory containing the source code.
- **uv.lock:** Dependency lock file used by the `uv` dependency manager.

## Dependencies

The project relies on the following libraries:

- `langchain >= 0.3.27`
- `langchain-openai >= 0.3.35`
- `openai >= 2.2.0`
- `python-dotenv >= 1.1.1`
- `streamlit >= 1.50.0`
- `tinydb >= 4.8.2`
- `watchdog >= 6.0.0`

These libraries are handled via the Poetry dependency manager as specified in the `pyproject.toml`.

## Contributing

Contributions are welcome! Please follow these steps to contribute:

1. Fork the repository.
2. Create a new branch (`git checkout -b feature-YourFeature`).
3. Make your changes and commit them (`git commit -m "Add some feature"`).
4. Push to the branch (`git push origin feature-YourFeature`).
5. Create a new Pull Request.

## License

This project is licensed under the MIT License. See the LICENSE file for more details.

## Contact

For inquiries or issues, please open an issue in this repository or reach out via my email: [your-email@example.com].

---

Feel free to customize any part of this README to better fit your project's specifics!