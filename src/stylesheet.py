css ="""
/* Base Styles */
QWidget {
    background-color: #2E2E2E;
    color: #EAEAEA;
    font-family: Arial, sans-serif;
    border: none;
}

/* Text Edit Fields */
QTextEdit {
    background-color: #3A3A3A;
    border: 1px solid #5A5A5A;
    padding: 5px;
}

/* Buttons */
QPushButton {
    background-color: #4A4A4A;
    border: 1px solid #6A6A6A;
    padding: 5px 10px;
    min-width: 80px;
    font-weight: bold;
}

QPushButton:hover {
    background-color: #5A5A5A;
}

QPushButton[checkable="true"]:checked {
    background-color: #181818; /* Adjust color as needed */
    border: 3px solid #721212;
}
/* Checkboxes */
QCheckBox {
    padding: 5px;
    spacing: 5px;
}

/* Group Boxes */
QGroupBox {
    border: 1px solid #5A5A5A;
    margin-top: 10px;
    padding: 10px;
}

QGroupBox::title {
    color: #B0B0B0;
    subcontrol-origin: margin;
    subcontrol-position: top left;
    padding: 0 5px 0 5px;
}

/* Scroll Areas */
QScrollArea {
    border: 1px solid #5A5A5A;
}

/* Tab Widget */
QTabWidget::pane {
    border: 1px solid #5A5A5A;
}

QTabBar::tab {
    background-color: #4A4A4A;
    padding: 5px 10px;
}

QTabBar::tab:selected {
    background-color: #3A3A3A;
}
QSplitter::handle {
    background-color: #3a3a3a;
}

QScrollArea {
    background-color: #1e1e1e; /* Set the desired color for the scroll area background */
}

/* Hide the arrows at the ends of the scroll bar */
QScrollBar::up-arrow, QScrollBar::down-arrow, QScrollBar::left-arrow, QScrollBar::right-arrow {
    background: none;
    border: none;
    width: 0;
    height: 0;
}

/* Set the appearance of the scroll bar handle (the part that you drag) */
QScrollBar::handle {
    background: #3e3e3e;
}

/* Set the appearance of the scroll bar groove (the track behind the handle) */
QScrollBar::groove {
    background: #1e1e1e;
}

/* Optional: Set the appearance of the scroll bar add-page and sub-page (the regions you can click to page up/down or left/right) */
QScrollBar::add-page, QScrollBar::sub-page {
    background: #1e1e1e;
}

QScrollArea {
    background-color: #1e1e1e; /* Set the desired color for the scroll area background */
}
"""
