from rich.live import Live
from rich.layout import Layout
from rich.panel import Panel
from rich.console import Console
from rich.table import Table
from rich.progress import Progress, SpinnerColumn, BarColumn, TextColumn
from rich.syntax import Syntax
from rich import box
import asyncio

class InteractiveUI:
    def __init__(self):
        self.console = Console()
        self.layout = Layout()
        
    async def show_welcome_animation(self):
        """Show an animated welcome screen"""
        # Clear screen
        self.console.clear()
        
        # ASCII art using simple characters
        logo = """
╔═══════════════════════════════════════╗
║             $PNET HR TEAM             ║
╚═══════════════════════════════════════╝
        """
        
        # Animate logo
        for line in logo.split('\n'):
            self.console.print(f"[cyan]{line}[/cyan]")
            await asyncio.sleep(0.1)
        
        # Animated tagline
        tagline = "The Future of Recruitment is Sentient"
        with self.console.status("[bold cyan]Initializing AI Agents...", spinner="dots"):
            for char in tagline:
                self.console.print(f"[bold magenta]{char}[/bold magenta]", end="")
                await asyncio.sleep(0.05)
            await asyncio.sleep(1)
    
    def create_dashboard_layout(self):
        """Create a multi-panel dashboard layout"""
        self.layout.split_column(
            Layout(name="header", size=3),
            Layout(name="body"),
            Layout(name="footer", size=3)
        )
        
        self.layout["body"].split_row(
            Layout(name="main_content", ratio=2),
            Layout(name="sidebar", ratio=1)
        )
        
        return self.layout

    async def animate_agent_thinking(self, agent_name, color="cyan"):
        """Show an animated thinking process for agents"""
        thoughts = [
            "analyzing patterns",
            "processing insights",
            "synthesizing data",
            "exploring possibilities",
            "connecting dots"
        ]
        
        with Progress(
            SpinnerColumn(),
            TextColumn("[progress.description]{task.description}"),
            BarColumn(),
            TextColumn("[progress.percentage]{task.percentage:>3.0f}%"),
            expand=True
        ) as progress:
            task = progress.add_task(f"[{color}]{agent_name} is thinking...", total=100)
            
            for thought in thoughts:
                progress.update(task, advance=20, description=f"[{color}]{agent_name} is {thought}...")
                await asyncio.sleep(0.5)

    def show_interactive_menu(self, options):
        """Show an interactive menu with hover effects"""
        table = Table(show_header=False, box=box.ROUNDED)
        table.add_column("Option", style="cyan", justify="left")
        
        for idx, option in enumerate(options, 1):
            table.add_row(f"[{idx}] {option}")
        
        return Panel(table, title="[bold]Choose Your Action", border_style="cyan")

    async def show_evaluation_progress(self, steps):
        """Show evaluation progress with animations"""
        with Progress(
            SpinnerColumn(),
            TextColumn("[progress.description]{task.description}"),
            BarColumn(),
            TextColumn("[progress.percentage]{task.percentage:>3.0f}%"),
            expand=True
        ) as progress:
            task = progress.add_task("Evaluating Candidate", total=len(steps))
            for step in steps:
                self.console.print(f"[cyan]➤ {step}[/cyan]")
                await asyncio.sleep(0.5)
                progress.advance(task)

    def create_score_visualization(self, scores):
        """Create an animated score visualization"""
        table = Table(title="Evaluation Scores", box=box.DOUBLE_EDGE)
        table.add_column("Category", style="cyan")
        table.add_column("Score", justify="center")
        table.add_column("Visualization", justify="left")
        
        for category, score in scores.items():
            bar = "█" * int(score * 10)
            table.add_row(
                category,
                f"{score:.1f}/10",
                f"[{'green' if score >= 7 else 'yellow' if score >= 5 else 'red'}]{bar}[/]"
            )
        
        return table