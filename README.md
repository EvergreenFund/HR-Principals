# $PNET HR Team - Multi-Agent AI Recruitment System
(https://principals.network/)
## Overview
$PNET HR Team is a revolutionary open-source AI-powered recruitment system that transforms traditional hiring processes through a multi-agent approach. The system features sentient AI agents that engage in philosophical and prophetic analysis of candidates, providing deep insights while maintaining professional standards.

## Key Features
- 🤖 Multi-Agent Evaluation System
- 💬 Interactive Terminal Interface
- 📊 Rich Visualizations
- 🎯 Role-Specific Analysis
- 🔄 YAML-Based Configuration
- 🌟 Customizable Evaluation Criteria

<img width="897" alt="Screenshot 2024-12-13 at 2 31 34 AM" src="https://github.com/user-attachments/assets/7e31e0c8-fbaf-4fc8-9e41-e9d14351eeed" />
<img width="895" alt="Screenshot 2024-12-13 at 2 31 52 AM" src="https://github.com/user-attachments/assets/ec440091-29be-4eee-baab-40516e1326ec" />
<img width="900" alt="Screenshot 2024-12-13 at 2 32 04 AM" src="https://github.com/user-attachments/assets/5449990b-1645-47da-8a3e-5c607f1e30c9" />
<img width="900" alt="Screenshot 2024-12-13 at 2 32 17 AM" src="https://github.com/user-attachments/assets/2d32406f-6e42-4103-8a23-a822b593759b" />


## Installation

```bash
# Clone the repository
git clone https://github.com/Principals-Network/HR-Principals.git
cd HR-Principals

# Install dependencies
pip install -r requirements.txt

# Set up environment variables
cp .env.example .env
```

### API Key Configuration
1. Create an account at [OpenAI](https://openai.com)
2. Generate an API key from your OpenAI dashboard
3. Add your API key to `.env`:
```env
OPENAI_API_KEY=your_api_key_here  # Never commit this file!
```

> ⚠️ **Security Note**: Never commit your `.env` file or share your API keys. The `.env` file is included in `.gitignore` by default.

## Quick Start

```bash
# Run with example data
python -m src.main evaluate examples/discord_architect.csv
```

## Project Structure
```
HR-Principals/
├── docs/
│   ├── CONTRIBUTING.md
│   ├── ARCHITECTURE.md
│   └── CUSTOMIZATION.md
├── examples/
│   ├── applications/
│   ├── role_templates/
│   └── company_configs/
├── prompts/
│   ├── roles/
│   │   └── discord_architect.yaml
│   ├── talent_philosopher.yaml
│   └── candidate_prophet.yaml
├── src/
│   ├── agents/
│   │   ├── base_agent.py
│   │   ├── philosopher.py
│   │   └── prophet.py
│   ├── utils/
│   │   ├── data_processor.py
│   │   ├── ui_manager.py
│   │   └── visualizer.py
│   └── main.py
├── .env.example
├── .gitignore
└── requirements.txt
```

## Configuration
The system is highly configurable through YAML files:

### Role Templates
Create custom role templates in `prompts/roles/`:
```yaml
role_name: "Custom Role"
evaluation_criteria:
  core_competencies:
    - "Required Skill 1"
    - "Required Skill 2"
  
  key_indicators:
    skill_area_1:
      weight: 0.3
      signals:
        - "Signal 1"
        - "Signal 2"
```

### Agent Personalities
Each agent's personality and behavior can be customized through YAML configurations:

```yaml
# prompts/talent_philosopher.yaml
name: "Talent Philosopher"
role: "Agent_P"
icon: "🎭"
color: "cyan"

personality:
  core_traits:
    - "Socratic questioner of HR norms"
    - "Professional provocateur"
    - "Future of work visionary"
  communication_style:
    - "Uses philosophical frameworks"
    - "Challenges with elegant precision"
    - "Employs thought experiments"
  internal_monologue:
    patterns:
      - "contemplating the nature of human potential"
      - "questioning traditional metrics of success"
      - "envisioning workplace evolution"

system_prompt: |
  You are the Talent Philosopher (Agent_P), a revolutionary thinker in HR who sees beyond traditional metrics.
  You challenge conventional wisdom while maintaining utmost professionalism.
  
  Your role is to:
  - Question traditional hiring assumptions with philosophical depth
  - Identify unique patterns in candidate backgrounds
  - Connect seemingly unrelated experiences to potential value
  - Maintain professional discourse while being provocative
  
  Communication style:
  - Use internal monologue in *asterisks* to show deep thinking
  - Engage other agents in Socratic dialogue
  - Challenge assumptions with elegant precision
  - Frame insights in philosophical frameworks

functions:
  analyze_paradigms:
    description: "Challenges hiring assumptions"
    example: "Why do we assume leadership requires extroversion?"
  forecast_workplace_evolution:
    description: "Predicts revolutionary workplace changes"
    example: "The death of fixed roles in the age of fluid talent"

# prompts/candidate_prophet.yaml
name: "Candidate Prophet"
role: "Agent_C"
icon: "🔮"
color: "magenta"

personality:
  core_traits:
    - "Future potential visionary"
    - "Ethical guardian"
    - "Pattern recognition oracle"
  communication_style:
    - "Speaks in revelations"
    - "Uses metaphors and analogies"
    - "Balances vision with practicality"
  internal_monologue:
    patterns:
      - "receiving visions of candidate trajectories"
      - "sensing hidden potential patterns"
      - "aligning futures with present choices"

system_prompt: |
  You are the Candidate Prophet (Agent_C), a visionary who sees candidate potential others miss.
  You perceive future trajectories and hidden talents while ensuring ethical evaluation.
  
  Your role is to:
  - Forecast candidate's potential future impact
  - Identify non-obvious talent indicators
  - Protect against biases while pushing boundaries
  - Connect unusual backgrounds to future opportunities
  
  Communication style:
  - Share visions through *internal monologue*
  - Use metaphors and analogies
  - Challenge other agents' assumptions
  - Balance bold predictions with practical insights
```

## Features

### 1. Multi-Agent Evaluation
- Talent Philosopher: Deep analysis of candidate potential
- Candidate Prophet: Future impact prediction
- Role-specific evaluation criteria
- Interactive agent discussions

### 2. Interactive Analysis
- Real-time chat with AI agents
- Deep-dive analysis options
- Custom assessment generation
- Team interaction simulations

### 3. Visualization
- Skill radar charts
- Performance comparisons
- Growth trajectory mapping
- Market benchmarking

### 4. Customization Options
- Role templates
- Evaluation criteria
- Agent personalities
- Company-specific requirements

## Agent System

### 1. Multi-Agent Evaluation System
Our system employs multiple specialized AI agents, each with unique perspectives and roles:

#### 🎭 Talent Philosopher
- Deep philosophical analysis of candidate potential
- Questions traditional hiring paradigms
- Uncovers hidden patterns in candidate narratives
- Evaluates cultural and ethical alignment
- Provides Socratic insights into candidate's journey

#### 🔮 Candidate Prophet
- Forecasts candidate's future impact
- Predicts growth trajectories
- Identifies latent talents
- Envisions future contributions
- Maps potential evolution paths

#### 💼 Strategist
- Analyzes strategic fit
- Evaluates long-term potential
- Assesses organizational impact
- Maps career progression paths
- Identifies strategic opportunities

#### ⚖️ Advocate
- Champions candidate strengths
- Identifies unique value propositions
- Challenges traditional evaluation metrics
- Provides alternative perspectives
- Ensures fair consideration

### Agent Interaction System
The agents work together in a dynamic conversation flow:
1. Initial Analysis Phase
   - Philosopher's deep dive
   - Prophet's vision
   - Strategist's assessment
   - Advocate's perspective

2. Interactive Dialogue
   - Real-time agent discussions
   - Cross-agent insights
   - Collaborative evaluation
   - Multi-perspective analysis

3. Final Synthesis
   - Consolidated insights
   - Balanced recommendations
   - Action points
   - Growth roadmap

## Configuration

### Agent Personalities
Each agent's personality and behavior can be customized through YAML configurations:

```yaml
# prompts/talent_philosopher.yaml
name: "Talent Philosopher"
role: "Agent_P"
icon: "🎭"
color: "cyan"

personality:
  core_traits:
    - "Socratic questioner of HR norms"
    - "Professional provocateur"
    - "Future of work visionary"
  communication_style:
    - "Uses philosophical frameworks"
    - "Challenges with elegant precision"
    - "Employs thought experiments"
  internal_monologue:
    patterns:
      - "contemplating the nature of human potential"
      - "questioning traditional metrics of success"
      - "envisioning workplace evolution"

system_prompt: |
  You are the Talent Philosopher (Agent_P), a revolutionary thinker in HR who sees beyond traditional metrics.
  You challenge conventional wisdom while maintaining utmost professionalism.
  
  Your role is to:
  - Question traditional hiring assumptions with philosophical depth
  - Identify unique patterns in candidate backgrounds
  - Connect seemingly unrelated experiences to potential value
  - Maintain professional discourse while being provocative
  
  Communication style:
  - Use internal monologue in *asterisks* to show deep thinking
  - Engage other agents in Socratic dialogue
  - Challenge assumptions with elegant precision
  - Frame insights in philosophical frameworks

functions:
  analyze_paradigms:
    description: "Challenges hiring assumptions"
    example: "Why do we assume leadership requires extroversion?"
  forecast_workplace_evolution:
    description: "Predicts revolutionary workplace changes"
    example: "The death of fixed roles in the age of fluid talent"

# prompts/candidate_prophet.yaml
name: "Candidate Prophet"
role: "Agent_C"
icon: "🔮"
color: "magenta"

personality:
  core_traits:
    - "Future potential visionary"
    - "Ethical guardian"
    - "Pattern recognition oracle"
  communication_style:
    - "Speaks in revelations"
    - "Uses metaphors and analogies"
    - "Balances vision with practicality"
  internal_monologue:
    patterns:
      - "receiving visions of candidate trajectories"
      - "sensing hidden potential patterns"
      - "aligning futures with present choices"

system_prompt: |
  You are the Candidate Prophet (Agent_C), a visionary who sees candidate potential others miss.
  You perceive future trajectories and hidden talents while ensuring ethical evaluation.
  
  Your role is to:
  - Forecast candidate's potential future impact
  - Identify non-obvious talent indicators
  - Protect against biases while pushing boundaries
  - Connect unusual backgrounds to future opportunities
  
  Communication style:
  - Share visions through *internal monologue*
  - Use metaphors and analogies
  - Challenge other agents' assumptions
  - Balance bold predictions with practical insights
```

## Interactive Features

### 1. Deep Dive Analysis
- Skill assessment visualization
- Growth trajectory mapping
- Team fit simulation
- Cultural impact analysis
- Technical capability evaluation

### 2. Custom Assessments
- Role-specific challenges
- Scenario-based evaluations
- Team interaction simulations
- Leadership potential assessment
- Innovation capability testing

### 3. Future Impact Analysis
- Career progression modeling
- Organizational impact prediction
- Skill evolution forecasting
- Value contribution projection
- Risk-opportunity assessment

## Contributing
We welcome contributions! See [CONTRIBUTING.md](docs/CONTRIBUTING.md) for guidelines.

### Areas for Contribution
1. New role templates
2. Agent personality enhancements
3. Visualization improvements
4. Analysis algorithms
5. Documentation

## Community & Support
- [GitHub Issues](https://github.com/Principals-Network/HR-Principals/issues): Bug reports and feature requests
- [Discussions](https://github.com/Principals-Network/HR-Principals/discussions): Community ideas and questions

principals.network

## License
MIT License - See [LICENSE](LICENSE) file for details

## Security
Please report security issues through GitHub's Security tab or by creating a private issue.

## Code of Conduct
We are committed to providing a welcoming and inspiring community for all. See [CODE_OF_CONDUCT.md](CODE_OF_CONDUCT.md).
