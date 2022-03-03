import sys
import io
from browser import document, html, window


class Exercises():
    
    def __init__(self, progress_indicator=True):
        self._total = 0
        self._solved = 0
        for element in document.getElementsByClassName('exercise'):
            self._install_exercise(element.id)
            if 'no-progress' in element.classList:
                continue
            self._total += 1
        if self._total and progress_indicator:
            self._progress = html.DIV()
            self._progress.classList.add('exercises_progress')
            document <= self._progress
            self._update_progress()
        else:
            self._progress = None
        
    def _update_progress(self):
        if self._progress is None:
            return
        print('Updating progress')
        if self._solved == self._total:
            self._progress.classList.add('all_solved')
            self._progress.html = \
                '<span class="glyphicon glyphicon-ok-circle" aria-hidden="true"></span> All solved!'
        else:
            self._progress.html = \
                f'{self._solved} / {self._total}<br /><small>solved</small>'

    def _install_exercise(self, id_):
        def _execute(event):
            self._exercise_execute(editor, output, solution_output,
                                   solution_code, solution_validate, run,
                                   solved, incorrect)
        print(f'Installing exercise {id_}')
        exercise = document[id_]
        run = html.BUTTON('<span class="glyphicon glyphicon-play-circle" aria-hidden="true"></span> Run')
        run.classList.add('btn')
        run.classList.add('btn-default')
        exercise <= run
        solved = html.DIV('<span class="glyphicon glyphicon-ok-circle" aria-hidden="true"></span> Solved!')
        solved.classList.add('solved')
        solved.style.display = 'none'
        exercise <= solved
        incorrect = html.DIV('<span class="glyphicon glyphicon-repeat" aria-hidden="true"></span> Not yet, try again!')
        incorrect.classList.add('incorrect')
        incorrect.style.display = 'none'
        exercise <= incorrect
        output = html.PRE()
        output.classList.add('output')
        output.style.display = 'none'
        exercise <= output
        solution_code = None
        solution_output = None
        solution_validate = None
        for element in exercise.children:
            if 'solution_code' in element.classList:
                lines = []
                for line in element.innerHTML.strip().splitlines():
                    if not line.strip().startswith('#') and line.strip():
                        lines.append(line)
                solution_code = '\n'.join(lines)
            elif 'solution_output' in element.classList:
                solution_output = element.innerHTML.strip().lower()
            elif 'solution_validate' in element.classList:
                solution_validate = element.innerHTML.strip()
            elif 'code' in element.classList:
                code = element
        editor = window.CodeMirror.fromTextArea(code, {'theme': 'monokai'})
        editor.setSize(None, 100)
        run.bind('click', _execute)
        
    def _validate(self, solution_validate, workspace):
        if solution_validate is None:
            return False
        print('validating solution')
        print(solution_validate)
        exec(solution_validate, workspace)
        print(workspace)
        return workspace.get('correct', False)

    def _exercise_execute(self, editor, output, solution_output, solution_code,
                          solution_validate, run, solved, incorrect):
        print('Executing code')
        code = editor.getValue().strip()
        buffer = io.StringIO()
        sys.stdout = buffer
        workspace = {}
        try:
            exec(code, workspace)
        except Exception as e:
            print(e)
        sys.stdout = sys.__stdout__
        output_value = buffer.getvalue().strip()
        if not output_value:
            output.style.display = 'none'
        else:
            output.textContent = output_value
            output.style.display = 'block'
        if run.style.display == 'none':  # already solved
            return
        if (solution_output == output_value.lower()
            or solution_code == code
            or self._validate(solution_validate, workspace)
        ):
            solved.style.display = 'block'
            incorrect.style.display = 'none'
            run.style.display = 'none'
            self._solved += 1
            self._update_progress()
        else:
            incorrect.style.display = 'block'


exercises = Exercises()
