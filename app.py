from flask import Flask, render_template, request
import os
import ast
import re

app = Flask(__name__)

class PythonExplanationParser:
    
    def __init__(self, explanations_path):
        self.explanations_path = explanations_path
        self.concepts = self._discover_concepts()
    
    def _discover_concepts(self):
        concepts = {}
        for item in os.listdir(self.explanations_path):
            item_path = os.path.join(self.explanations_path, item)
            if os.path.isdir(item_path):
                concepts[item] = self._get_concept_files(item_path)
        return concepts
    
    def _get_concept_files(self, concept_path):
        files = []
        for file in os.listdir(concept_path):
            if file.endswith('.py') or file.endswith('.md'):
                files.append(file)
        return sorted(files)
    
    def parse_python_file(self, concept, filename):
        file_path = os.path.join(self.explanations_path, concept, filename)
        
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        explanations = []
        code_examples = []
        
        docstring_pattern = r'"""(.*?)"""'
        docstrings = re.findall(docstring_pattern, content, re.DOTALL)
        explanations.extend([doc.strip() for doc in docstrings])
        
        code_parts = re.split(docstring_pattern, content, flags=re.DOTALL)
        for i, part in enumerate(code_parts):
            if i % 2 == 0:
                code_part = part.strip()
                if code_part and not code_part.startswith('"""'):
                    code_examples.append(code_part)
        
        return {
            'explanations': explanations,
            'code_examples': code_examples,
            'raw_content': content
        }
    
    def parse_markdown_file(self, concept, filename):
        file_path = os.path.join(self.explanations_path, concept, filename)
        
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        return {
            'markdown_content': content,
            'raw_content': content
        }

parser = PythonExplanationParser('explanations')

@app.route('/')
def home():
    return render_template('home.html', concepts=parser.concepts.keys())

@app.route('/concept/<concept_name>')
def concept_overview(concept_name):
    if concept_name not in parser.concepts:
        return "Concept not found", 404
    
    files = parser.concepts[concept_name]
    return render_template('concept_overview.html', 
                         concept_name=concept_name, 
                         files=files,
                         concepts=parser.concepts.keys())

@app.route('/concept/<concept_name>/<filename>')
def explanation_detail(concept_name, filename):
    if concept_name not in parser.concepts:
        return "Concept not found", 404
    
    if filename not in parser.concepts[concept_name]:
        return "File not found", 404
    
    if filename.endswith('.py'):
        content = parser.parse_python_file(concept_name, filename)
        return render_template('python_explanation.html',
                             concept_name=concept_name,
                             filename=filename,
                             content=content,
                             concepts=parser.concepts.keys())
    elif filename.endswith('.md'):
        content = parser.parse_markdown_file(concept_name, filename)
        return render_template('markdown_explanation.html',
                             concept_name=concept_name,
                             filename=filename,
                             content=content,
                             concepts=parser.concepts.keys())
    
    return "Unsupported file type", 400



if __name__ == '__main__':
    app.run(debug=True, port=5000)