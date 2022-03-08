import sys
import io
from browser import document, html, window


RUN_HTML = '<span class="glyphicon glyphicon-play-circle" aria-hidden="true"></span> Run'
SOLVED_HTML = '<span class="glyphicon glyphicon-ok-circle" aria-hidden="true"></span> Solved!'
INCORRECT_HTML = '<span class="glyphicon glyphicon-repeat" aria-hidden="true"></span> Not yet, try again!'
ALL_SOLVED_HTML = '<span class="glyphicon glyphicon-ok-circle" aria-hidden="true"></span> All solved!'

class Exercise:
    
    def __init__(self, exercise_manager, id_):
        
        print(f'Installing exercise {id_}')
        self.solved = False
        self._id = id_
        self._exercise_manager = exercise_manager
        self._exercise = document[id_]
        self.progress = 'no-progress' not in self._exercise.classList
        self._run = html.BUTTON(RUN_HTML)
        self._run.classList.add('btn')
        self._run.classList.add('btn-default')
        self._exercise <= self._run
        self._solved = html.DIV(SOLVED_HTML)
        self._solved.classList.add('solved')
        self._solved.style.display = 'none'
        self._exercise <= self._solved
        self._incorrect = html.DIV(INCORRECT_HTML)
        self._incorrect.classList.add('incorrect')
        self._incorrect.style.display = 'none'
        self._exercise <= self._incorrect
        self._output = html.PRE()
        self._output.classList.add('output')
        self._output.style.display = 'none'
        self._exercise <= self._output
        self._solution_code = []
        self._solution_output = []
        self._solution_validate = None
        self._solution_prevalidate = None
        for element in self._exercise.children:
            if 'solution_code' in element.classList:
                lines = []
                for line in element.innerHTML.strip().splitlines():
                    if not line.strip().startswith('#') and line.strip():
                        lines.append(line)
                self._solution_code.append('\n'.join(lines))
            elif 'solution_output' in element.classList:
                self._solution_output.append(element.innerHTML.strip().lower())
            elif 'solution_prevalidate' in element.classList:
                self._solution_prevalidate = element.innerHTML.strip()
            elif 'solution_validate' in element.classList:
                self._solution_validate = element.innerHTML.strip()
            elif 'code' in element.classList:
                self._code = element
        self._editor = window.CodeMirror.fromTextArea(self._code,
                                                      {'theme': 'monokai'})
        for cls in self._code.classList:
            if cls.startswith('height'):
                self._editor.setSize(None, int(cls[6:]))
                break
        else:
            self._editor.setSize(None, 100)
        self._run.bind('click', self.execute)
        
    def validate(self, workspace):
        if self._solution_validate is None:
            return False
        print(f'Validating exercise {self._id}')
        exec(self._solution_validate, workspace)
        return workspace.get('correct', False)
        
    def execute(self, event=None):
        print(f'Executing exercise {self._id}')
        code = self._editor.getValue().strip()
        buffer = io.StringIO()
        sys.stdout = buffer
        workspace = {}
        if self._solution_prevalidate is not None:
            exec(self._solution_prevalidate, workspace)
        try:
            exec(code, workspace)
        except Exception as e:
            print(e)
        sys.stdout = sys.__stdout__
        output_value = buffer.getvalue().strip()
        if not output_value:
            self._output.style.display = 'none'
        else:
            self._output.textContent = output_value
            self._output.style.display = 'block'
        if self._run.style.display == 'none':  # already solved
            return
        if (output_value.lower() in self._solution_output
            or code in self._solution_code
            or self.validate(workspace)
        ):
            self.solved = True
            self._solved.style.display = 'block'
            self._incorrect.style.display = 'none'
            self._run.style.display = 'none'
            self._exercise_manager.update_progress()
        else:
            incorrect.style.display = 'block'
    

class ExerciseManager:
    
    def __init__(self):
        self._exercises = []
        for element in document.getElementsByClassName('exercise'):
            self._exercises.append(Exercise(self, element.id))
        if self.total_progress:
            self._progress = html.DIV()
            self._progress.classList.add('exercises_progress')
            document <= self._progress
            self.update_progress()
        else:
            self._progress = None
    
    @property
    def total_progress(self):
        return sum(e.progress for e in self._exercises)
        
    @property
    def total_solved(self):
        return sum(e.solved for e in self._exercises if e.progress)
        
    @property
    def all_solved(self):
        return all(e.solved for e in self._exercises if e.progress)
        
    def update_progress(self):
        if not self.total_progress:
            return
        print('Updating progress')
        if self.all_solved:
            self._progress.classList.add('all_solved')
            self._progress.html = ALL_SOLVED_HTML
        else:
            self._progress.html = \
                f'{self.total_solved} / {self.total_progress}<br /><small>solved</small>'


ExerciseManager()
