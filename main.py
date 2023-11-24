import sys

from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QHBoxLayout, QLabel, QPushButton, QTextEdit, QFrame
from PyQt5.QtCore import Qt

# Liste mit den unterstützten Münzen vorbereiten
coins = [0.05, 0.1, 0.2, 0.5, 1, 2, 5]

# Liste der Tickets vorbereiten (Tickets sind dictionaries)
tickets = [
    {
        "id": 1,
        "name": 'Kurzstrecke',
        "price": 2.1
    }, {
        "id": 2,
        "name": 'Langstrecke',
        "price": 3.5
    }, {
        "id": 3,
        "name": 'Ermässigt',
        "price": 1.8
    }, {
        "id": 4,
        "name": 'Zonenbefreit',
        "price": 9.8
    }
]

# Neues Dictionary für die Transaktionsinformation (gewähltes Ticket und ausstehender Betrag)
transaction = {
    'received_coins': [],
    'remaining_amount': 0.0
}


# # # UI Elements
# Ticket Layout Elemente
# Für die Tickets werden einzelne Buttons und ein Stornieren-Button erstellt
def add_ticket_options(p_layout):
    # Überschrift für Ticketwahl
    ticket_choice_label = QLabel("Bitte wählen Sie ihr Ticket:")
    font = QFont()
    font.setBold(True)
    font.setPointSize(16)
    ticket_choice_label.setFont(font)
    p_layout.addWidget(ticket_choice_label)

    font.setBold(False)
    # Buttons für jedes Ticket erstellen
    for ticket in tickets:
        ticket_option = QPushButton(f"{ticket.get('name')} - CHF {ticket.get('price'):.2f}")
        ticket_option.setFixedHeight(50)
        ticket_option.setFont(font)
        # Hinzufügen, dass die Funktion "choose_ticket" aufgerufen, wenn auf den Button geklickt wird
        ticket_option.clicked.connect(lambda _, ticket_id=ticket.get('id'): choose_ticket(ticket_id))
        p_layout.addWidget(ticket_option)
        ticket_options.append(ticket_option)

    # Button für das Stornieren erstellen
    cancel_button.setText('Ticket stornieren')
    font.setBold(True)
    cancel_button.setFixedHeight(50)
    cancel_button.setFont(font)
    p_layout.addWidget(cancel_button)


# Element für die Ticketauswahl Anzeige
def add_ticket_choice(p_layout):
    ticket_choice.setReadOnly(True)
    font = QFont("Courier New", 16)
    ticket_choice.setFont(font)
    ticket_choice.setFixedSize(300, 110)
    ticket_choice.setPlainText('Keine Auswahl getroffen')
    ticket_choice.setAlignment(Qt.AlignCenter)

    p_layout.addWidget(ticket_choice)


# Element für die Ticketausgabe hinzufügen
def add_ticket_output(p_layout):
    ticket_output_label = QLabel("Ticketausgabe:")
    font = QFont()
    font.setBold(True)
    font.setPointSize(16)
    ticket_output_label.setFont(font)
    p_layout.addWidget(ticket_output_label)

    ticket_output.setReadOnly(True)
    font = QFont("Courier New", 16)
    ticket_output.setFont(font)
    ticket_output.setFixedSize(300, 200)
    ticket_output.setAlignment(Qt.AlignCenter)
    p_layout.addWidget(ticket_output)


# Coin Layout Elemente
# Für die Münzen werden einzelne Buttons erstellt
def add_coin_buttons(p_layout):
    # Überschrift für Münzwahl
    coin_buttons_label = QLabel("Nutzen Sie die Buttons um Geld einzuwerfen:")
    font = QFont()
    font.setBold(True)
    font.setPointSize(16)
    coin_buttons_label.setFont(font)
    coin_buttons_label.setAlignment(Qt.AlignBottom)
    p_layout.addWidget(coin_buttons_label)

    font.setBold(False)
    # Buttons für jede Münze erstellen
    for coin in coins:
        coin_button = QPushButton(f"CHF {coin:.2f}")
        coin_button.setFixedHeight(50)
        coin_button.setFont(font)
        coin_buttons.append(coin_button)
        p_layout.addWidget(coin_button)

    # Dieses Label wurde für eine Korrektur der Abstände im Layout hinzugefügt
    p_layout.addWidget(QLabel())


# Element für die Ausgabe des Rückgelds hinzufügen
def add_change_output(p_layout):
    # Überschrift für die Ausgabe des Rückgelds
    change_output_label = QLabel("Ihr Rückgeld:")
    font = QFont()
    font.setBold(True)
    font.setPointSize(16)
    change_output_label.setFont(font)
    p_layout.addWidget(change_output_label)

    # Konfiguration des Textfelds für das Rückgeld
    change_output.setReadOnly(True)
    font = QFont("Courier New", 16)
    change_output.setFont(font)
    change_output.setFixedSize(300, 200)
    p_layout.addWidget(change_output)


# Schliessen-Button hinzufügen
def add_close_button(p_layout):
    close_button = QPushButton('Schliessen')
    close_button.clicked.connect(sys.exit)
    close_button.setFixedHeight(50)
    font = QFont()
    font.setBold(True)
    font.setPointSize(16)
    close_button.setFont(font)
    # Der Schliessen-Button soll unten rechts platziert werden
    p_layout.addWidget(close_button, alignment=Qt.AlignBottom | Qt.AlignRight)


# # # Generische UI Elemente
# Eine Funktion, um einen Trennstrich erzeugen zu können (hat noch keine Ausrichtung)
def get_divider():
    divider = QFrame()
    divider.setFrameShadow(QFrame.Sunken)
    divider.setLineWidth(2)
    return divider


# # # Funktionen
# Mit einer Ticket ID aus der Ticketliste ein Ticket auswählen und zurückgeben
def get_ticket_by_id(ticket_id):
    for ticket in tickets:
        if ticket.get('id') == ticket_id:
            return ticket


# Die Ticketauswahl speichern
def choose_ticket(ticket_id):
    # Ticket anhand der ID ermitteln
    ticket = get_ticket_by_id(ticket_id)

    # Ticketwahl ausgeben
    ticket_choice.setPlainText(
        f"Ihre Ticket Auswahl:\
		\n\r-- {ticket.get('name').upper()} --\
		\n\rBitte werfen Sie CHF {ticket.get('price'):.2f} ein.")

    # In der Transaktion das ticket hinterlegen und den erwarteten Betrag
    transaction['requested_ticket'] = ticket
    transaction['remaining_amount'] = ticket.get('price')


def show_ui():
    # Zuerst wird das Fenster konfiguriert
    window.setWindowTitle('Ticketautomat')
    window.move(100, 100)

    # Die drei Hauptlayouts definieren
    main_layout = QVBoxLayout()
    interaction_layout = QHBoxLayout()
    control_layout = QHBoxLayout()

    # Links sollen die Interaktionen und Ausgaben zu den Tickets sein, rechts die zu den Münzen.
    # In der Mitte ein Trennstrich
    ticket_layout = QVBoxLayout()

    divider_layout = QVBoxLayout()
    v_divider = get_divider()
    # Ausrichtung des Trennstrichs setzen
    v_divider.setFrameShape(QFrame.VLine)
    divider_layout.addWidget(v_divider)

    coin_layout = QVBoxLayout()

    # Die Elemente zum Ticketlayout hinzufügen
    add_ticket_options(ticket_layout)
    add_ticket_choice(ticket_layout)
    th_divider = get_divider()
    th_divider.setFrameShape(QFrame.HLine)
    ticket_layout.addWidget(th_divider)
    add_ticket_output(ticket_layout)

    # Die Elemente zum Coinlayout hinzufügen
    add_coin_buttons(coin_layout)
    ch_divider = get_divider()
    ch_divider.setFrameShape(QFrame.HLine)
    coin_layout.addWidget(ch_divider)
    add_change_output(coin_layout)

    # Den Schliessen-Button zum Controllayout hinzufügen
    add_close_button(control_layout)

    # Die einzelnen Layouts zur Ticketauswahl und zur Münzwahl / Bezahlung dem Interactionlayout hinzufügen
    interaction_layout.addLayout(ticket_layout)
    interaction_layout.addLayout(divider_layout)
    interaction_layout.addLayout(coin_layout)

    # Das Interaktionslayout und das Layout mit dem Schliessen-Button dem Hauptlayout hinzufügen
    main_layout.addLayout(interaction_layout)
    main_layout.addLayout(control_layout)

    # Das Layout mit allen unterlayouts für unser Fenster festlegen
    window.setLayout(main_layout)
    # Das Fenster anzeigen
    window.show()


# Wir haben das if statement zu main entfernt, es hatte keine Auswirkungen
# Applikation vorbereiten
app = QApplication(sys.argv)

# Alle global verfügbaren UI Element vorbereiten
# Diese UI Elemente werden von mehreren Funktionen benötigt, deswegen haben wir sie global definiert
window = QWidget()
# Liste für die Buttons der Auswahlmöglichkeiten zu den Tickets
ticket_options = []
# Anzeige des gewählten Tickets
ticket_choice = QTextEdit()
# Stornieren Button
cancel_button = QPushButton()
# Ausgabe des Tickets
ticket_output = QTextEdit()
# Liste für die Buttons der Auswahlmöglichkeiten zu den Münzen
coin_buttons = []
# Ausgabe des Rückgelds
change_output = QTextEdit()

# Nach der Definition soll das UI angezeigt werden
show_ui()
# Das Programm wird beendet, wenn die QApplication ausläuft
sys.exit(app.exec_())