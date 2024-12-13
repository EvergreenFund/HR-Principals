import yaml
from pathlib import Path

class PromptLoader:
    def __init__(self, prompts_dir="prompts"):
        self.prompts_dir = Path(prompts_dir)
        
    def load_role_prompt(self, role_name):
        """Load role-specific prompts and evaluation criteria"""
        role_file = self.prompts_dir / "roles" / f"{role_name.lower().replace(' ', '_')}.yaml"
        
        if not role_file.exists():
            role_file = self.prompts_dir / "roles" / "default.yaml"
            
        with open(role_file, 'r') as f:
            return yaml.safe_load(f)
            
    def get_agent_prompt(self, agent_type, role_data, candidate_data):
        """Generate role-specific prompt for an agent"""
        base_prompt = role_data[f"{agent_type}_prompt_template"]
        
        return f"""
        Role Context:
        {role_data['role_name']} at {role_data['organization']}
        
        Evaluation Focus:
        {yaml.dump(role_data['evaluation_criteria'], default_flow_style=False)}
        
        Candidate Data:
        {yaml.dump(candidate_data, default_flow_style=False)}
        
        {base_prompt}
        """ 