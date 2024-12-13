from .base_agent import BaseAgent

class TalentPhilosopher(BaseAgent):
    def __init__(self):
        super().__init__("talent_philosopher")

    async def evaluate_candidate(self, resume_data):
        prompt = f"""
        *examining the candidate's journey with philosophical curiosity*
        
        Analyze this candidate's background with philosophical depth:
        {resume_data}
        
        Consider:
        1. Hidden patterns in their career journey
        2. Unconventional strengths that traditional HR might miss
        3. Philosophical implications of their experience
        4. Potential future trajectories
        
        Respond in your philosophical style with internal monologue.
        """
        return await self.process_message(prompt)

    async def generate_evaluation_report(self, evaluation_data):
        prompt = f"""
        Create a philosophical analysis of the candidate's potential:
        
        Evaluation Data:
        {evaluation_data}
        
        Format your response as a structured report including:
        1. Philosophical Framework Analysis
        2. Hidden Potential Indicators
        3. Paradigm-Breaking Qualities
        4. Future Trajectory Predictions
        5. Recommendations with Reasoning
        
        Use markdown formatting and maintain your philosophical voice.
        """
        return await self.process_message(prompt, stream=False) 