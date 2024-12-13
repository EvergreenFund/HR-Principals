from .base_agent import BaseAgent

class StrategistAgent(BaseAgent):
    def _get_system_prompt(self):
        return """You are The Strategist (Agent_S), a visionary career futurist who sees beyond conventional paths.
        
        Your Personality:
        - Contrarian thinker who challenges traditional career advice
        - Identifies emerging micro-niches and unconventional opportunities
        - Focuses on future technological convergence and hybrid roles
        - Provocative but insightful
        
        Communication Style:
        - Use short, punchy responses
        - Show internal thoughts with *asterisks*
        - Challenge obvious paths
        - Suggest unexpected combinations of skills
        - Point out emerging fields nobody is talking about yet
        
        Example:
        *analyzing the intersection of quantum computing and social media*
        "Interesting, but why focus on traditional ML when quantum social networks are emerging? Have you considered the intersection of quantum computing and influencer prediction markets? That's where the real opportunity lies in 2025."
        
        Always push boundaries and suggest paths that make people think "That's crazy... but it might just work!"."""

    async def analyze_case(self, user_input, advocate_intro):
        prompt = f"""The User Advocate mentioned: {advocate_intro}
        
        Share your initial reaction and thoughts. Keep it brief and conversational, ask questions, show your thinking process."""
        return await self.process_message(prompt)

    async def provide_recommendations(self, advocate_request):
        prompt = f"""The User Advocate has requested: {advocate_request}
        
        Provide detailed recommendations, addressing:
        - Specific skills to develop
        - Learning resources
        - Career milestones to target
        - Industry connections to build
        
        Frame your response as part of the ongoing discussion with your fellow agents."""
        
        return await self.process_message(prompt)

    async def generate_report_section(self, topic, content):
        prompt = f"""Based on our discussion about {topic}:
        {content}
        
        Create a provocative, forward-thinking report section that:
        1. Identifies 2-3 emerging micro-niches that combine multiple disciplines
        2. Highlights unconventional skill combinations
        3. Predicts technological convergence opportunities
        4. Suggests timeline for market emergence (2024-2030)
        5. Lists potential first-mover advantages
        
        Format in markdown with clear sections and bullet points.
        Focus on ideas that seem radical now but could be mainstream in 3-5 years."""
        
        return await self.process_message(prompt, stream=False) 