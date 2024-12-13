# Contributing to $PNET HR Team

## Getting Started
1. Fork the repository
2. Create a new branch for your feature
3. Make your changes
4. Submit a pull request

## Development Setup
```bash
# Clone your fork
git clone https://github.com/YOUR_USERNAME/HR-Principals.git
cd HR-Principals

# Create virtual environment
python -m venv venv
source venv/bin/activate  # or `venv\Scripts\activate` on Windows

# Install dependencies
pip install -r requirements.txt

# Set up pre-commit hooks
pre-commit install
```

## Project Structure
- `src/agents/`: AI agent implementations
- `src/utils/`: Utility functions and helpers
- `prompts/`: YAML configuration files
- `examples/`: Example data and templates

## Adding New Features

### New Agent Types
1. Create a new agent class in `src/agents/`
2. Implement the required methods
3. Add corresponding YAML config in `prompts/`
4. Update documentation

### New Role Templates
1. Add YAML file in `prompts/roles/`
2. Follow existing template structure
3. Add example usage

### Visualization Improvements
1. Add new visualization class/method
2. Implement in `src/utils/visualizer.py`
3. Add tests

## Code Style
- Follow PEP 8 guidelines
- Use type hints
- Write docstrings
- Add tests for new features

## Pull Request Process
1. Update documentation
2. Add tests
3. Update CHANGELOG.md
4. Get review from maintainers

## Community
- Join discussions
- Help others
- Be respectful 