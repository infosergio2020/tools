#!/usr/bin/python

import PySimpleGUI as sg

from controler_XML import XML_controller

"""
    Allows you to "browse" through the Theme settings.  Click on one and you'll see a
    Popup window using the color scheme you chose.  It's a simple little program that also demonstrates
    how snappy a GUI can feel if you enable an element's events rather than waiting on a button click.
    In this program, as soon as a listbox entry is clicked, the read returns.
"""

sg.theme('Dark Brown')


layout = [[sg.Text('Theme Browser')],
          [sg.Text('Click a Theme color to see demo window')],
          [
            [sg.Text('Browse to a file'), sg.Input(key='-FILE-', visible=False, enable_events=True), sg.FileBrowse()]
          ],
          [sg.Button('GO')],
          [sg.Button('Exit')]]

window = sg.Window('WF-duplicados', layout)

while True:  # Event Loop
    event, values = window.read()
    if event in ('GO'):
          ctrl_XML = XML_controller( values["-FILE-"])
          ctrl_XML.printWorkflows();
    if event in (sg.WIN_CLOSED, 'Exit'):
          break

    print(f'You clicked {event} with value { values["-FILE-"] }')

window.close()

# avances logrados 
# 1) interface para poder seleccionar un file
# 2) instancia de obj controller para manipulacion de XML