import pandas as pd
from pathlib import Path

class ApplicationProcessor:
    def __init__(self, csv_path):
        self.csv_path = Path(csv_path)
        self.applications = None
        
    def load_applications(self):
        """Load applications from CSV file"""
        try:
            # Read CSV with different encoding options if needed
            try:
                self.applications = pd.read_csv(self.csv_path)
            except UnicodeDecodeError:
                self.applications = pd.read_csv(self.csv_path, encoding='utf-8-sig')
            
            # Print column names for debugging
            print("Found columns:", self.applications.columns.tolist())
            
            # Map columns if they have different names
            column_mappings = {
                'Name': 'Name',
                'Application': 'Application',
                'Role': 'Role',
                # Add any alternative column names here
                'Position': 'Role',
                'Message': 'Application',
                'User': 'Name'
            }
            
            # Rename columns if they exist with different names
            self.applications = self.applications.rename(columns=column_mappings)
            
            required_columns = {'Name', 'Application', 'Role'}
            if not required_columns.issubset(self.applications.columns):
                raise ValueError(f"CSV must contain columns: {required_columns}")
            
            # Clean the data
            self.applications = self.applications.fillna('')
            return True
            
        except Exception as e:
            print(f"Error loading applications: {str(e)}")
            return False
    
    def get_application(self, index):
        """Get a single application by index"""
        if self.applications is None:
            raise ValueError("Applications not loaded. Call load_applications() first.")
        
        if index >= len(self.applications):
            raise IndexError("Application index out of range")
            
        application = self.applications.iloc[index]
        return {
            'name': application['Name'],
            'application': application['Application'],
            'role': application['Role']
        }
    
    def get_all_applications(self):
        """Get all applications"""
        if self.applications is None:
            raise ValueError("Applications not loaded. Call load_applications() first.")
            
        return [
            {
                'name': row['Name'],
                'application': row['Application'],
                'role': row['Role']
            }
            for _, row in self.applications.iterrows()
        ] 