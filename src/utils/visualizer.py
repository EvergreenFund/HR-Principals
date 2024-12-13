from rich.table import Table
from rich.progress import Progress, SpinnerColumn, BarColumn, TextColumn
from rich.console import Console
from rich.layout import Layout
from rich.panel import Panel
from rich import box
from datetime import datetime
import math
import asyncio
from rich.live import Live

class ResultVisualizer:
    def __init__(self):
        self.console = Console()

    def create_score_table(self, scores, title="Evaluation Scores"):
        """Create a rich table for scores"""
        table = Table(title=title, box=box.DOUBLE_EDGE, show_header=True, header_style="bold magenta")
        
        table.add_column("Category", style="cyan", justify="left")
        table.add_column("Score", justify="center")
        table.add_column("Rating", justify="right")
        table.add_column("Confidence", justify="center")
        
        for category, score in scores.items():
            rating = self._get_rating_symbol(score['overall'])
            confidence = self._get_confidence_bar(score['confidence'])
            table.add_row(
                category.replace('_', ' ').title(),
                f"{score['overall']}/10",
                rating,
                confidence
            )
        
        return table

    def create_skill_radar(self, skills):
        """Create an ASCII radar chart for skills"""
        # Simplified ASCII radar chart
        chart = []
        max_len = max(len(skill) for skill in skills.keys())
        
        for skill, value in skills.items():
            bars = '█' * int(value * 10)
            spaces = ' ' * (max_len - len(skill))
            chart.append(f"{skill}{spaces} │ {bars} {value:.1f}/10")
        
        return Panel('\n'.join(chart), title="Skills Radar", border_style="cyan")

    def create_timeline(self, milestones):
        """Create a visual timeline"""
        timeline = []
        for date, milestone in milestones.items():
            timeline.append(f"[cyan]{date}[/cyan]")
            timeline.append(f"└─ {milestone}")
            timeline.append("")
        
        return Panel('\n'.join(timeline), title="Development Timeline", border_style="green")

    def create_comparison_chart(self, candidate_scores, market_benchmarks):
        """Create a comparison chart between candidate and market"""
        chart = []
        for metric, scores in candidate_scores.items():
            candidate = scores['score']
            benchmark = market_benchmarks[metric]
            
            chart.append(f"{metric}:")
            chart.append(f"Candidate: {'█' * int(candidate * 10)} {candidate:.1f}")
            chart.append(f"Market   : {'█' * int(benchmark * 10)} {benchmark:.1f}")
            chart.append("")
        
        return Panel('\n'.join(chart), title="Market Comparison", border_style="blue")

    def _get_rating_symbol(self, score):
        if score >= 9:
            return "🌟 Exceptional"
        elif score >= 8:
            return "✨ Strong"
        elif score >= 7:
            return "✅ Good"
        else:
            return "⚠️ Needs Work"

    def _get_confidence_bar(self, confidence):
        bars = math.floor(confidence * 10)
        return f"[{'green' if confidence > 0.7 else 'yellow'}]{'█' * bars}{'░' * (10-bars)}[/]"

    async def animate_analysis(self, message, duration=3):
        """Show an animated progress bar during analysis"""
        with Progress(
            SpinnerColumn(),
            TextColumn("[progress.description]{task.description}"),
            BarColumn(),
            TextColumn("[progress.percentage]{task.percentage:>3.0f}%"),
        ) as progress:
            task = progress.add_task(message, total=100)
            
            while not progress.finished:
                await asyncio.sleep(duration/100)
                progress.update(task, advance=1) 

    async def create_animated_radar(self, skills):
        """Create an animated radar chart"""
        points = []
        for skill, value in skills.items():
            angle = (len(points) * 2 * math.pi) / len(skills)
            r = value * 10
            x = r * math.cos(angle)
            y = r * math.sin(angle)
            points.append((x, y))
            
        # Animate radar chart drawing
        with Live(refresh_per_second=20) as live:
            for i in range(len(points)):
                # Draw partial radar
                chart = self._draw_radar(points[:i+1])
                live.update(Panel(chart))
                await asyncio.sleep(0.2)