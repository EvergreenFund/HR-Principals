from openai import OpenAI
from openai import APIError
from src.config import OPENAI_API_KEY, MODEL_NAME
from src.utils.config_loader import ConfigLoader
from src.utils.prompt_loader import PromptLoader
import asyncio
from rich.console import Console

console = Console()

class BaseAgent:
    def __init__(self, config_name):
        config = ConfigLoader().load_agent_config(config_name)
        
        self.name = config['name']
        self.role = config['role']
        self.icon = config['icon']
        self.color = config['color']
        self.personality = config['personality']
        self.system_prompt = config['system_prompt']
        self.functions = config['functions']
        
        self.client = OpenAI(api_key=OPENAI_API_KEY)
        self.conversation_history = []
        self.max_retries = 3
        self.retry_delay = 1

    def _get_system_prompt(self):
        return self.system_prompt

    async def process_message(self, message, context=None, stream=True):
        """Process a message using the OpenAI API with streaming support"""
        try:
            messages = [
                {"role": "system", "content": self._get_system_prompt()},
                *self.conversation_history
            ]
            
            if context:
                messages.append({"role": "system", "content": f"Context: {context}"})
                
            messages.append({"role": "user", "content": message})
            
            response = await self._get_completion(messages, stream)
            return response
            
        except APIError as e:
            return self._handle_api_error(e)

    async def _async_iterate(self, iterator):
        """Helper method to iterate over sync iterator asynchronously"""
        for item in iterator:
            yield item
            await asyncio.sleep(0)

    async def generate_report_section(self, topic, content):
        """Generate a formatted report section"""
        prompt = f"""Create a detailed but concise report section about {topic} based on our discussion:
        {content}
        
        Format it in markdown with:
        - Clear headings
        - Bullet points for key insights
        - Code snippets or technical details where relevant
        - Timeline estimates
        - Risk factors
        
        Focus on unconventional, forward-thinking insights."""
        
        return await self.process_message(prompt, stream=False)

    async def _get_completion(self, messages, stream=True):
        """Handle API completion with streaming support"""
        try:
            response = await asyncio.get_event_loop().run_in_executor(
                None,
                lambda: self.client.chat.completions.create(
                    model=MODEL_NAME,
                    messages=messages,
                    stream=stream
                )
            )

            if stream:
                full_response = ""
                async for chunk in self._async_iterate(response):
                    if hasattr(chunk.choices[0].delta, 'content') and chunk.choices[0].delta.content:
                        content = chunk.choices[0].delta.content
                        full_response += content
                        console.print(content, end="", markup=False)
                
                console.print()  # New line after streaming
                self.conversation_history.append({"role": "user", "content": messages[-1]["content"]})
                self.conversation_history.append({"role": "assistant", "content": full_response})
                return full_response
            else:
                content = response.choices[0].message.content
                self.conversation_history.append({"role": "user", "content": messages[-1]["content"]})
                self.conversation_history.append({"role": "assistant", "content": content})
                return content

        except Exception as e:
            return self._handle_api_error(e)

    def _handle_api_error(self, error):
        """Handle API errors gracefully"""
        error_message = str(error)
        if 'insufficient_quota' in error_message:
            return "I apologize, but I'm currently unable to process requests due to API quota limitations."
        return f"Error: {error_message}"

    def _get_role_specific_prompt(self, role_name, candidate_data):
        """Get role-specific evaluation prompt"""
        prompt_loader = PromptLoader()
        role_data = prompt_loader.load_role_prompt(role_name)
        return prompt_loader.get_agent_prompt(
            self.role.lower(),
            role_data,
            candidate_data
        )

    async def evaluate_candidate(self, resume_data):
        """Evaluate candidate with role-specific prompts"""
        role_prompt = self._get_role_specific_prompt(
            resume_data['role'],
            {
                'name': resume_data['name'],
                'application': resume_data['application']
            }
        )
        return await self.process_message(role_prompt)

    async def generate_evaluation_report(self, evaluation_data):
        """Generate a detailed evaluation report"""
        raise NotImplementedError