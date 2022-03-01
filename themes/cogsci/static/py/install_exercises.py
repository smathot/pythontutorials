import sys
import io
from browser import document, html, window


class Exercises():
    
    def __init__(self):
        self._total = 0
        self._solved = 0
        for element in document.getElementsByClassName('exercise'):
            self._install_exercise(element.id)
            self._total += 1
        if self._total:
            self._progress = html.DIV()
            self._progress.classList.add('exercises_progress')
            document <= self._progress
            self._update_progress()
        
    def _update_progress(self):
        if self._solved == self._total:
            self._progress.classList.add('all_solved')
            self._progress.html = \
                '<span class="glyphicon glyphicon-ok-circle" aria-hidden="true"></span> All solved!'
        else:
            self._progress.html = \
                f'{self._solved} / {self._total}'

    def _install_exercise(self, id_):
        def _execute(event):
            self._exercise_execute(editor, output, solution_output,
                                   solution_code, run, solved)
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
        output = html.PRE()
        output.classList.add('output')
        output.style.display = 'none'
        exercise <= output
        solution_code = None
        solution_output = None
        for element in exercise.children:
            if 'solution_code' in element.classList:
                solution_code = element.getInnerHTML().strip()
            elif 'solution_output' in element.classList:
                solution_output = element.getInnerHTML().strip()
            elif 'code' in element.classList:
                code = element
        editor = window.CodeMirror.fromTextArea(code, {'lineNumbers': True,
                                                       'theme': 'monokai'})
        editor.setSize(None, 120)
        exercise.bind('click', _execute)

    def _exercise_execute(self, editor, output, solution_output, solution_code,
                          run, solved):
        code = editor.getValue().strip()
        buffer = io.StringIO()
        sys.stdout = buffer
        try:
            exec(code)
        except Exception as e:
            print(e)
        sys.stdout = sys.__stdout__
        output_value = buffer.getvalue().strip()
        if not output_value:
            output.style.display = 'none'
            return
        output.textContent = output_value
        output.style.display = 'block'
        if run.style.display != 'none' and (
                solution_output == output_value
                or solution_code == code):
            solved.style.display = 'block'
            run.style.display = 'none'
            self._solved += 1
            self._update_progress()


exercises = Exercises()
