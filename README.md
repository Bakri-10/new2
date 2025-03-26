# Tableau Data Extractor

A tool to extract failure data from Tableau databases, validate its structure, and prepare it for further analysis.

## Requirements

- Python 3.6+
- Ansible 2.10+
- Tableau server access

## Installation

1. Clone this repository
2. Install dependencies:
   ```
   pip install -r requirements.txt
   ```

## Configuration

1. Edit `config/tableau_config.yml` with your Tableau server details
2. Set environment variables for authentication:
   ```
   export TABLEAU_USERNAME=your-username
   export TABLEAU_PASSWORD=your-password
   ```

## Usage

Run the extraction playbook: