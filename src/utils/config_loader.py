import yaml
from pathlib import Path

class ConfigLoader:
    def __init__(self, config_dir="prompts"):
        self.config_dir = Path(config_dir)
        self.configs = {}
        
    def load_agent_config(self, agent_type):
        """Load agent configuration from YAML file"""
        config_path = self.config_dir / f"{agent_type}.yaml"
        
        if not config_path.exists():
            raise FileNotFoundError(f"Configuration file not found: {config_path}")
            
        with open(config_path, 'r') as f:
            config = yaml.safe_load(f)
            
        return config
    
    def load_company_config(self, company_name):
        """Load company-specific configuration"""
        config_path = self.config_dir / "companies" / f"{company_name}.yaml"
        
        if not config_path.exists():
            # Load default config if company-specific doesn't exist
            config_path = self.config_dir / "custom_company.yaml"
            
        with open(config_path, 'r') as f:
            config = yaml.safe_load(f)
            
        return config 