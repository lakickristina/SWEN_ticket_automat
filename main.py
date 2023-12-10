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
    # Font Definition durch die neue get_font Funktion ersetzen
    font = get_font(16, True)
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
    # Funktion zum Stornieren mit dem Stornieren-Button verbinden
    cancel_button.clicked.connect(cancel_ticket_choice)
    # Stornieren deaktivieren beim Programmstart
    set_buttons_state([cancel_button], False)
    p_layout.addWidget(cancel_button)


# Element für die Ticketauswahl Anzeige
def add_ticket_choice(p_layout):
    ticket_choice.setReadOnly(True)
    # Font Definition durch die neue get_font Funktion ersetzen
    font = get_font(16, False, 'Courier New')
    ticket_choice.setFont(font)
    ticket_choice.setFixedSize(320, 110)
    ticket_choice.setPlainText('Keine Auswahl getroffen')
    ticket_choice.setAlignment(Qt.AlignCenter)

    p_layout.addWidget(ticket_choice)

# Element für für die Anzeige des Restbetrags hinzufügen
def add_remaining_amount(p_layout):
    font = get_font(14, True)
    font.setFamily("Courier New")
    remaining_amount_output.setFont(font)
    p_layout.addWidget(remaining_amount_output)

# Element für die Ticketausgabe hinzufügen
def add_ticket_output(p_layout):
    ticket_output_label = QLabel("Ticketausgabe:")
    font = get_font(16, True)
    ticket_output_label.setFont(font)
    p_layout.addWidget(ticket_output_label)

    ticket_output.setReadOnly(True)
    # Font Definition durch die neue get_font Funktion ersetzen
    font = QFont("Courier New", 16)
    ticket_output.setFont(font)
    ticket_output.setFixedSize(320, 200)
    ticket_output.setAlignment(Qt.AlignCenter)
    p_layout.addWidget(ticket_output)


# Coin Layout Elemente
# Für die Münzen werden einzelne Buttons erstellt
def add_coin_buttons(p_layout):
    # Überschrift für Münzwahl
    coin_buttons_label = QLabel("Nutzen Sie die Buttons um Geld einzuwerfen:")
    # Font Definition durch die neue get_font Funktion ersetzen
    font = get_font(16, True)
    coin_buttons_label.setFont(font)
    coin_buttons_label.setAlignment(Qt.AlignBottom)
    p_layout.addWidget(coin_buttons_label)

    font.setBold(False)
    # Buttons für jede Münze erstellen
    for coin in coins:
        coin_button = QPushButton(f"CHF {coin:.2f}")
        coin_button.setFixedHeight(50)
        coin_button.setFont(font)
        # Funktion zum Münzeinwurf mit den jeweiligen Münz-Button verbinden
        coin_button.clicked.connect(lambda _, value=coin: receive_coin(value))
        coin_buttons.append(coin_button)
        p_layout.addWidget(coin_button)

    # Coin Buttons deaktivieren beim Programmstart
    set_buttons_state(coin_buttons, False)
    # Dieses Label wurde für eine Korrektur der Abstände im Layout hinzugefügt
    p_layout.addWidget(QLabel())


# Element für die Ausgabe des Rückgelds hinzufügen
def add_change_output(p_layout):
    # Überschrift für die Ausgabe des Rückgelds
    change_output_label = QLabel("Ihr Rückgeld:")
    # Font Definition durch die neue get_font Funktion ersetzen
    font = get_font(16, True)
    change_output_label.setFont(font)
    p_layout.addWidget(change_output_label)

    # Konfiguration des Textfelds für das Rückgeld
    change_output.setReadOnly(True)
    # Font Definition durch die neue get_font Funktion ersetzen
    font = get_font(16, False, 'Courier New')
    change_output.setFont(font)
    change_output.setFixedSize(320, 200)
    p_layout.addWidget(change_output)


# Schliessen-Button hinzufügen
def add_close_button(p_layout):
    close_button = QPushButton('Schliessen')
    close_button.clicked.connect(sys.exit)
    close_button.setFixedHeight(50)
    # Font Definition durch die neue get_font Funktion ersetzen
    font = get_font(16, True)
    close_button.setFont(font)
    # Der Schliessen-Button soll unten rechts platziert werden
    p_layout.addWidget(close_button, alignment=Qt.AlignBottom | Qt.AlignRight)


# # # Generische UI Elemente
# Neue Funktion, um eine Liste an Buttons zu deaktivieren (verwendet für die UI Steuerung)
def set_buttons_state(buttons, state):
    # state ist True oder False, je nachdem die Buttons aktiviert (True) oder deaktiviert (False)
    button: QPushButton
    for button in buttons:
        if state:
            button.setEnabled(True)
        else:
            button.setDisabled(True)

# Neue Funktion für die Generierung von Font-Elementen
def get_font(size, bold, family=''):
    font = QFont()
    font.setPointSize(size)
    font.setBold(bold)
    if family != '':
        font.setFamily(family)

    return font

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
    # Bei Ticketwahl: Ticketbuttons deaktivieren, Coin-Buttons aktivieren und Stornieren-Button aktivieren
    set_buttons_state(coin_buttons, True)
    set_buttons_state(ticket_options, False)
    set_buttons_state([cancel_button], True)
    transaction['remaining_amount'] = ticket.get('price')

    # Anzeige zum erwarteten Betrag aktualisieren
    remaining_amount_output.setText(f"Restbetrag: CHF {ticket.get('price'):.2f}")
    # Ticketausgabe zurücksetzen
    ticket_output.setText('')
    # Rückgeldausgabe zurücksetzen
    change_output.setText('')

# Neue Funktion für das Stornieren von Tickets
def cancel_ticket_choice():
    # Im Ticketwahl-Feld die Stornierung bestätigen
    ticket_choice.setText('Ticket storniert')
    ticket_choice.setAlignment(Qt.AlignCenter)

    # Ticket aus der Transaktion löschen
    del transaction['requested_ticket']

    # Bei Stornierung: Coin-Buttons und Stornierungs-Button deaktivieren, Ticket-Buttons aktivieren
    set_buttons_state(ticket_options, True)
    set_buttons_state(coin_buttons, False)
    set_buttons_state([cancel_button], False)

    # Erwarteten Betrag zurücksetzen
    remaining_amount_output.setText('')

    # Eingeworfenes Geld zurückgeben
    if len(transaction.get('received_coins')) > 0:
        for received_coin in sorted(transaction.get('received_coins')):
            change_output.insertPlainText(f'CHF {received_coin:.2f}\n')

        transaction['received_coins'] = []


# Neue Funktion um den Münzeinwurf (Button-Click auf Coin-Button) abzubilden
def receive_coin(value):
    # Münze den eingeworfenen Münzen hinzufügen
    transaction['received_coins'].append(value)

    # Eingeworfene Münze vom erwarteten Betrag abziehen
    transaction['remaining_amount'] = round(transaction['remaining_amount'] - round(float(value), 2), 2)

    # Abfrage ob Betrag bereits bezahlt wurde (wenn nicht, erwarteten Betrag reduzieren in der Anzeige)
    # Wenn doch (remaining_amount < 0) wurde das Ticket bezahlt
    if transaction['remaining_amount'] > 0:
        remaining_amount_output.setText(f"Restbetrag: CHF {transaction['remaining_amount']:.2f}")
    else:
        ticket = transaction['requested_ticket']
        # Zeichenlänge einer Zeile ermitteln
        count_name = len(ticket['name'])
        count_price = len(str(ticket['price'])) + 1
        total_length = 15 + count_name + count_price
        # Ticketangaben in ticket_output drucken
        ticket_output.insertPlainText(f"{'*' * total_length}\n")
        ticket_output.insertPlainText(f"{'*' + ' ' * (total_length - 2) + '*'}\n")
        ticket_output.insertPlainText(f"*  {ticket['name']} für CHF {ticket['price']:.2f}  *\n")
        ticket_output.insertPlainText(f"{'*' + ' ' * (total_length - 2) + '*'}\n")
        ticket_output.insertPlainText(f"{'*' * total_length}")

        # Leere Liste für das Rückgeld anlegen
        change = []
        #Saldo zugunsten des*der Kund*in ausrechnen
        balance = round(transaction['remaining_amount'] * -1, 2)
        # So lange Kund*innensaldo nicht 0 beträgt, wird die grösstmöglich Münze vom Saldo abgezogen
        while balance > 0:
            for coin in reversed(coins):
                coin = round(coin, 2)
                if coin <= balance:
                    # Saldo aktualisieren
                    balance = round(balance - coin, 2)
                    # Ausgewählte Münze dem Rückgeld hinzufügen
                    change.append(coin)
                    break

        # Das Rückgeld-Textfeld zuürcksetzen
        change_output.setText('')

        # Dasa aktuelle Rückgeld ausgeben
        for coin in change:
            change_output.insertPlainText(f'CHF {coin:.2f}\n')

        # Die Transaktionsdaten zurücksetzen (Ticket, erwarteter Betrag, erhaltenes Geld)
        del transaction['requested_ticket']
        transaction['remaining_amount'] = 0
        transaction['received_coins'] = []

        # Nach dem Ticketbezug: Stornierung-Button und Coin-Buttons deaktivieren, Ticket-Buttons aktivieren
        set_buttons_state(coin_buttons, False)
        set_buttons_state(ticket_options, True)
        set_buttons_state([cancel_button], False)

        remaining_amount_output.setText(f"Restbetrag: CHF 0.00")


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
    # Neu: Label hinzufügen für den erwarteten Betrag im Ticket Layout
    add_remaining_amount(ticket_layout)
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
# Label vorbereiten für den Restbetrag
remaining_amount_output = QLabel()
# Ausgabe des Rückgelds
change_output = QTextEdit()

# Nach der Definition soll das UI angezeigt werden
show_ui()
# Das Programm wird beendet, wenn die QApplication ausläuft
sys.exit(app.exec_())