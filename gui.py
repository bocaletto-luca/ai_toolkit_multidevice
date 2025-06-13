# gui.py
import PySimpleGUI as sg
from tasks.summarizer    import summarize
from tasks.qa            import answer
from tasks.transcription import transcribe
from tasks.image_caption import caption_image

def run_gui():
    sg.theme('LightGreen')
    # Tabs
    tab_sum = [
        [sg.Text('Text file:'), sg.Input(key='-SUM_FILE-'), sg.FileBrowse(file_types=(('TXT','*.txt'),))],
        [sg.Button('Summarize', key='-SUMMARIZE-')],
        [sg.Multiline('', size=(80,8), key='-SUM_OUT-')]
    ]
    tab_qa = [
        [sg.Text('Question:'), sg.Input(key='-QA_QUESTION-')],
        [sg.Text('Context file:'), sg.Input(key='-QA_FILE-'), sg.FileBrowse(file_types=(('TXT','*.txt'),))],
        [sg.Button('Answer', key='-QA_RUN-')],
        [sg.Multiline('', size=(80,8), key='-QA_OUT-')]
    ]
    tab_trans = [
        [sg.Text('Audio file:'), sg.Input(key='-AUD_FILE-'), sg.FileBrowse(file_types=(('Audio','*.mp3;*.wav'),))],
        [sg.Button('Transcribe', key='-TRANSCRIBE-')],
        [sg.Multiline('', size=(80,8), key='-TRANS_OUT-')]
    ]
    tab_cap = [
        [sg.Text('Image file:'), sg.Input(key='-IMG_FILE-'), sg.FileBrowse(file_types=(('Image','*.jpg;*.png'),))],
        [sg.Button('Caption', key='-CAPTION-')],
        [sg.Multiline('', size=(80,8), key='-CAP_OUT-')]
    ]

    layout = [
        [sg.TabGroup([[sg.Tab('Summarize', tab_sum),
                       sg.Tab('Q&A', tab_qa),
                       sg.Tab('Transcribe', tab_trans),
                       sg.Tab('Caption', tab_cap)]])],
        [sg.Button('Exit')]
    ]

    window = sg.Window('AI Toolkit GUI', layout, finalize=True)

    while True:
        event, vals = window.read()
        if event in (sg.WIN_CLOSED, 'Exit'):
            break
        if event == '-SUMMARIZE-':
            try:
                txt = open(vals['-SUM_FILE-'], encoding='utf-8').read()
                window['-SUM_OUT-'].update(summarize(txt))
            except Exception as e:
                window['-SUM_OUT-'].update(f"Error: {e}")
        if event == '-QA_RUN-':
            try:
                ctx = open(vals['-QA_FILE-'], encoding='utf-8').read()
                window['-QA_OUT-'].update(answer(vals['-QA_QUESTION-'], ctx))
            except Exception as e:
                window['-QA_OUT-'].update(f"Error: {e}")
        if event == '-TRANSCRIBE-':
            try:
                window['-TRANS_OUT-'].update(transcribe(vals['-AUD_FILE-']))
            except Exception as e:
                window['-TRANS_OUT-'].update(f"Error: {e}")
        if event == '-CAPTION-':
            try:
                window['-CAP_OUT-'].update(caption_image(vals['-IMG_FILE-']))
            except Exception as e:
                window['-CAP_OUT-'].update(f"Error: {e}")

    window.close()
