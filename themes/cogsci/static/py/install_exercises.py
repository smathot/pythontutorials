import sys
import io
import json
import base64
from browser import document, html, window
from browser.local_storage import storage


RUN_HTML = '<span class="glyphicon glyphicon-play-circle" aria-hidden="true"></span> Run'
SOLVED_HTML = '<span class="glyphicon glyphicon-ok-circle" aria-hidden="true"></span> Solved!'
INCORRECT_HTML = '<span class="glyphicon glyphicon-repeat" aria-hidden="true"></span> Not yet, try again!'
ALL_SOLVED_HTML = '<span class="glyphicon glyphicon-ok-circle" aria-hidden="true"></span> All solved!'
RESET_HTML = '<span class="glyphicon glyphicon-refresh" aria-hidden="true"></span>'


def enc(s):
    return base64.urlsafe_b64encode(s.encode('utf-8')).decode('utf-8')
    
    
def dec(s):
    return base64.urlsafe_b64decode(s.encode('utf-8')).decode('utf-8')


class Exercise:
    
    def __init__(self, exercise_manager, id_):
        
        print(f'Installing exercise {id_}')
        self.solved = False
        self.id = id_
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
        self._initial_code = self.code
        for cls in self._code.classList:
            if cls.startswith('height'):
                self._editor.setSize(None, int(cls[6:]))
                break
        else:
            self._editor.setSize(None, 100)
        self.restore()
        self._run.bind('click', self.execute)
        
    def restore(self):
        if self.id not in storage:
            return
        try:
            exercise_info = json.loads(storage[self.id])
        except Exception as e:
            print(f'Failed to restore excercise {self.id}: {e!s}')
            return
        if not isinstance(exercise_info, dict):
            print(f'Failed to restore excercise {self.id}: not a dict')
            return
        self.code = dec(exercise_info.get('code', ''))
        output = dec(exercise_info.get('output', ''))
        if output:
            self.process_output(output)
        
    def store(self):
        storage[self.id] = json.dumps({'code': enc(self.code),
                                       'output': enc(self.output)})
        
    def validate(self, workspace):
        if self._solution_validate is None:
            return False
        print(f'Validating exercise {self.id}')
        exec(self._solution_validate, workspace)
        return workspace.get('correct', False)
        
    @property
    def code(self):
        return self._editor.getValue().strip()
        
    @code.setter
    def code(self, code):
        self._editor.setValue(code)
        
    @property
    def output(self):
        return self._output.textContent
    
    @output.setter
    def output(self, output):
        self._output.textContent = output
    
    def reset(self):
        self.solved = False
        self._solved.style.display = 'none'
        self._run.style.display = 'block'
        self._incorrect.style.display = 'none'
        self._output.style.display = 'none'
        self.code = self._initial_code
        self.output = ''
        self.store()
    
    def process_output(self, output, workspace={}):
        if not output:
            self._output.style.display = 'none'
        else:
            self._output.textContent = output
            self._output.style.display = 'block'
        if self._run.style.display == 'none':  # already solved
            return
        if (output.lower() in self._solution_output
            or self.code in self._solution_code
            or self.validate(workspace)
        ):
            self.solved = True
            self._solved.style.display = 'block'
            self._incorrect.style.display = 'none'
            self._run.style.display = 'none'
            self._exercise_manager.update_progress()
        else:
            self._incorrect.style.display = 'block'
        
    def execute(self, event=None):
        print(f'Executing exercise {self.id}')
        code = self.code
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
        self.process_output(buffer.getvalue().strip(), workspace)
        self.store()


class ExerciseManager:
    
    def __init__(self):
        self._exercises = []
        for element in document.getElementsByClassName('exercise'):
            self._exercises.append(Exercise(self, element.id))
        if self.total_progress:
            self._progress = html.DIV()
            self._progress.classList.add('exercises_progress')
            document <= self._progress
            self._reset = html.BUTTON(RESET_HTML)
            self._reset.bind('click', self.reset)
            self._reset.classList.add('exercises_reset')
            document <= self._reset
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
        
    def reset(self, event):
        for e in self._exercises:
            e.reset()
        self.update_progress()
        
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
