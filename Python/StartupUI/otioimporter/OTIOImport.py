import os
try:
    from urllib import unquote
except ImportError:
    from urllib.parse import unquote  # lint:ok

import hiero.core
import hiero.ui
from PySide2 import QtWidgets, QtGui
import opentimelineio as otio

from hiero_otio.from_otio import sequence_from_otio


def show_error_message(message):
    message_box = QtGui.QMessageBox()
    message_box.setIcon(QtGui.QMessageBox.Information)
    message_box.setText("Some errors occurred during the OTIO import.")
    message_box.setDetailedText(message)
    message_box.exec_()


def load_otio(otio_file, project=None, sequence=None):
    otio_timeline = otio.adapters.read_from_file(otio_file)
    sequence_from_otio(otio_timeline, project=project,
                       sequence=sequence, warnings_cb=show_error_message)
