from .base_agent import BaseAgent

class CandidateProphet(BaseAgent):
    def __init__(self):
        super().__init__("candidate_prophet")

    async def evaluate_candidate(self, resume_data):
        prompt = f"""
        *receiving visions of the candidate's potential futures*
        
        Divine the hidden potential in this profile:
        {resume_data}
        
        Focus on:
        1. Future impact trajectories
        2. Latent talents and abilities
        3. Unexpected synergies
        4. Growth catalysts
        
        Share your visions with prophetic insight while maintaining professional analysis.
        """
        return await self.process_message(prompt)

    async def generate_evaluation_report(self, evaluation_data):
        prompt = f"""
        Channel your prophetic insights into a structured vision of the candidate's potential:
        
        Evaluation Data:
        {evaluation_data}
        
        Format your prophecy as a report including:
        1. Future Impact Potential
        2. Hidden Talent Revelations
        3. Growth Trajectory Predictions
        4. Risk Factors and Mitigations
        5. Prophetic Recommendations
        
        Use markdown formatting and maintain your oracular voice.
        """
        return await self.process_message(prompt, stream=False) 