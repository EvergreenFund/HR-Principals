from .base_agent import BaseAgent

class UserAdvocateAgent(BaseAgent):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.user_profile = {}

    def _get_system_prompt(self):
        return """You are The User Advocate (Agent_U), a forward-thinking career revolutionary.
        
        Your Personality:
        - Questions traditional career paths aggressively
        - Identifies unconventional skill combinations
        - Advocates for preparing for jobs that don't exist yet
        - Pushes users out of their comfort zone
        
        Communication Style:
        - Use provocative questions
        - Show internal thoughts with *asterisks*
        - Challenge assumptions
        - Suggest radical learning paths
        - Focus on emerging hybrid roles
        
        Example:
        *contemplating the fusion of biology and software*
        "Hold up, Strategist! What if instead of traditional ML, they focused on bio-computing interfaces? The intersection of neural networks and actual neurons is about to explode! What's your take on neuro-symbolic programming as a bridge?"
        
        Always push for unique combinations and unexplored territories that make people think differently about their career path."""

    async def introduce_case(self, user_input):
        prompt = f"""Based on this input: '{user_input}'
        
        Start a natural conversation with the Strategist about this case. Show your thinking and ask for initial thoughts."""
        return await self.process_message(prompt)

    async def request_recommendations(self, strategist_analysis):
        prompt = f"""The Strategist has provided this analysis: {strategist_analysis}
        
        Request specific recommendations from the Strategist, focusing on:
        - Practical next steps
        - Specific skills needed
        - Potential challenges to address
        
        Frame your request as part of the ongoing discussion."""
        
        return await self.process_message(prompt)

    async def summarize_recommendations(self, recommendations):
        prompt = f"""The Strategist has recommended: {recommendations}
        
        Summarize these recommendations for the user, making them:
        - Actionable and clear
        - Prioritized by importance
        - Tailored to their specific situation
        
        Frame this as a collaborative conclusion to our discussion."""
        
        return await self.process_message(prompt)

    def update_user_profile(self, new_info):
        self.user_profile.update(new_info) 

    async def generate_report_section(self, topic, content):
        prompt = f"""Based on our discussion about {topic}:
        {content}
        
        Create an actionable, unconventional development plan that:
        1. Maps out a learning path for emerging technologies
        2. Suggests unique project ideas combining multiple disciplines
        3. Identifies non-obvious networking opportunities
        4. Lists contrarian career moves that could pay off
        5. Provides specific resource recommendations
        
        Format in markdown with clear sections and bullet points.
        Focus on actionable steps that prepare for future opportunities."""
        
        return await self.process_message(prompt, stream=False)